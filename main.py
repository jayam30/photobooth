from src.models.face_recognition import FaceRecognitionModel
from src.models.embedding_manager import FaissEmbeddingManager
from src.services.face_service import FaceService
from config import FAISS_INDEX_FILE

def main():
    # Initialize models
    face_recognition_model = FaceRecognitionModel()
    embedding_manager = FaissEmbeddingManager.load(FAISS_INDEX_FILE)
    
    # Initialize service
    face_service = FaceService(face_recognition_model, embedding_manager)
    
    print("\nFace Recognition System initialized!")
    print("\nAvailable commands:")
    print("1. Process new images")
    print("2. Search for faces")
    print("3. List events")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            image_path = input("Enter image path: ")
            event_name = input("Enter event name: ")
            result = face_service.process_image(image_path, event_name)
            print(result)
        
        elif choice == '2':
            image_path = input("Enter image path: ")
            event_name = input("Enter event name (or press Enter for all events): ").strip()
            event_name = event_name if event_name else None
            result = face_service.search_image(image_path, event_name)
            print(result)
        
        elif choice == '3':
            result = face_service.list_events()
            print(result)
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()