from facenet_pytorch import InceptionResnetV1, MTCNN
import torch
from PIL import Image
from config import DEVICE, FACE_DETECTION_CONFIG
from src.utils.image_utils import ImagePreprocessor

class FaceRecognitionModel:
    def __init__(self):
        self.device = DEVICE
        self.preprocessor = ImagePreprocessor()
        self.mtcnn = MTCNN(
            image_size=FACE_DETECTION_CONFIG['image_size'],
            margin=FACE_DETECTION_CONFIG['margin'],
            min_face_size=FACE_DETECTION_CONFIG['min_face_size'],
            keep_all=FACE_DETECTION_CONFIG['keep_all'],
            device=self.device
        )
        self.embedding_model = InceptionResnetV1(pretrained='vggface2').eval().to(self.device)
    
    def detect_and_align(self, image):
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        try:
            # Use preprocessed image for detection
            preprocessed_image = self.preprocessor.preprocess(image)
            
            faces, probs = self.mtcnn(preprocessed_image, return_prob=True)
            
            if faces is None:
                return []
                
            if isinstance(faces, torch.Tensor):
                faces = [faces] if faces.dim() == 3 else [face for face in faces]
            
            return faces
        except Exception as e:
            print(f"Error in face detection: {str(e)}")
            return []
    
    def generate_embeddings(self, faces, augment=False):
        """
        Generate face embeddings with optional augmentation
        
        Args:
            faces (list): List of detected face tensors
            augment (bool): Whether to use data augmentation
        
        Returns:
            list: Face embeddings
        """
        embeddings = []
        for face in faces:
            # Convert face to PIL Image for preprocessing
            face_image = Image.fromarray(
                (face.permute(1, 2, 0).numpy() * 255).astype(np.uint8)
            )
            
            # Preprocess with optional augmentation
            processed_faces = self.preprocessor.preprocess(face_image, augment=augment)
            
            # Ensure processed_faces is a list for augmentation
            if not isinstance(processed_faces, list):
                processed_faces = [processed_faces]
            
            for processed_face in processed_faces:
                processed_face = processed_face.unsqueeze(0).to(self.device)
                
                with torch.no_grad():
                    embedding = self.embedding_model(processed_face).cpu().numpy().flatten()
                embeddings.append(embedding)
        
        return embeddings