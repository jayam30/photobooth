import os
import uuid
import numpy as np
from PIL import Image
from config import BASE_IMAGE_FOLDER, FAISS_INDEX_FILE

class FaceService:
    def __init__(self, face_recognition_model, embedding_manager):
        self.face_recognition_model = face_recognition_model
        self.embedding_manager = embedding_manager

    def process_image(self, image_path, event_name, augment=True):
        try:
            image = Image.open(image_path)
            faces = self.face_recognition_model.detect_and_align(image)
            
            if len(faces) == 0:
                return {"error": f"No faces detected in {image_path}"}
            
            # Generate embeddings with optional augmentation
            embeddings = self.face_recognition_model.generate_embeddings(faces, augment=augment)
            
            event_folder = os.path.join(BASE_IMAGE_FOLDER, event_name)
            os.makedirs(event_folder, exist_ok=True)
            
            saved_paths = []
            for face, embedding in zip(faces, embeddings):
                face_image = Image.fromarray(
                    (face.permute(1, 2, 0).numpy() * 255).astype(np.uint8)
                )
                
                face_filename = f"{event_name}_{uuid.uuid4()}.jpg"
                face_path = os.path.join(event_folder, face_filename)
                face_image.save(face_path)
                
                self.embedding_manager.add_embedding(embedding, face_path, event_name)
                saved_paths.append(face_path)
            
            self.embedding_manager.save(FAISS_INDEX_FILE)
            
            return {
                "message": f"Added {len(faces)} face(s) to the database",
                "saved_paths": saved_paths
            }
        except Exception as e:
            return {"error": f"Error processing image: {str(e)}"}