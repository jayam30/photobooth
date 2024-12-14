# # import os
# # import uuid
# # from fastapi import FastAPI, File, UploadFile, Form
# # from fastapi.responses import JSONResponse
# # from fastapi.middleware.cors import CORSMiddleware
# # from PIL import Image

# # # Import your existing face recognition components
# # from src.models.face_recognition import FaceRecognitionModel
# # from src.models.embedding_manager import FaissEmbeddingManager
# # from src.services.face_service import FaceService
# # from config import FAISS_INDEX_FILE, BASE_IMAGE_FOLDER

# # # Initialize face recognition components
# # face_recognition_model = FaceRecognitionModel()
# # embedding_manager = FaissEmbeddingManager.load(FAISS_INDEX_FILE)
# # face_service = FaceService(face_recognition_model, embedding_manager)

# # # Create FastAPI application
# # app = FastAPI(
# #     title="Face Recognition Service",
# #     description="API for processing and searching faces",
# #     version="1.0.0"
# # )

# # # Add CORS middleware
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],  # Allows all origins
# #     allow_credentials=True,
# #     allow_methods=["*"],  # Allows all methods
# #     allow_headers=["*"],  # Allows all headers
# # )

# # @app.post("/process-image/")
# # async def process_image(
# #     file: UploadFile = File(...), 
# #     event_name: str = Form(...)
# # ):
# #     try:
# #         # Ensure the uploaded file is an image
# #         with Image.open(file.file) as img:
# #             # Save the uploaded image temporarily
# #             temp_filename = os.path.join(
# #                 BASE_IMAGE_FOLDER, 
# #                 f"temp_{uuid.uuid4()}.jpg"
# #             )
# #             img.save(temp_filename)
        
# #         # Process the image
# #         result = face_service.process_image(temp_filename, event_name)
        
# #         # Remove the temporary file
# #         os.remove(temp_filename)
        
# #         return result
# #     except Exception as e:
# #         return JSONResponse(
# #             status_code=500, 
# #             content={"error": str(e)}
# #         )

# # @app.post("/search-image/")
# # async def search_image(
# #     file: UploadFile = File(...), 
# #     event_name: str = Form(None)
# # ):
# #     try:
# #         # Ensure the uploaded file is an image
# #         with Image.open(file.file) as img:
# #             # Save the uploaded image temporarily
# #             temp_filename = os.path.join(
# #                 BASE_IMAGE_FOLDER, 
# #                 f"temp_{uuid.uuid4()}.jpg"
# #             )
# #             img.save(temp_filename)
        
# #         # Search for faces
# #         result = face_service.search_image(temp_filename, event_name)
        
# #         # Remove the temporary file
# #         os.remove(temp_filename)
        
# #         return result
# #     except Exception as e:
# #         return JSONResponse(
# #             status_code=500, 
# #             content={"error": str(e)}
# #         )

# # @app.get("/list-events/")
# # async def list_events():
# #     try:
# #         return face_service.list_events()
# #     except Exception as e:
# #         return JSONResponse(
# #             status_code=500, 
# #             content={"error": str(e)}
# #         )

# # # Startup event to load models
# # @app.on_event("startup")
# # async def startup_event():
# #     print("Face Recognition Service is starting up...")
# #     print(f"Using device: {face_recognition_model.device}")


# import os
# import uuid
# from fastapi import FastAPI, File, UploadFile, Form
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# from PIL import Image

# # Import your existing face recognition components
# from .models.face_recognition import FaceRecognitionModel
# from .models.embedding_manager import FaissEmbeddingManager
# from .services.face_service import FaceService
# from config import FAISS_INDEX_FILE, BASE_IMAGE_FOLDER

# # Initialize face recognition components
# face_recognition_model = FaceRecognitionModel()
# embedding_manager = FaissEmbeddingManager.load(FAISS_INDEX_FILE)
# face_service = FaceService(face_recognition_model, embedding_manager)

# # Create FastAPI application
# app = FastAPI(
#     title="Face Recognition Service",
#     description="API for processing and searching faces",
#     version="1.0.0"
# )

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# @app.post("/process-image/")
# async def process_image(
#     file: UploadFile = File(...), 
#     event_name: str = Form(...)
# ):
#     try:
#         # Ensure the uploaded file is an image
#         with Image.open(file.file) as img:
#             # Save the uploaded image temporarily
#             temp_filename = os.path.join(
#                 BASE_IMAGE_FOLDER, 
#                 f"temp_{uuid.uuid4()}.jpg"
#             )
#             img.save(temp_filename)
        
#         # Process the image
#         result = face_service.process_image(temp_filename, event_name)
        
#         # Remove the temporary file
#         os.remove(temp_filename)
        
#         return result
#     except Exception as e:
#         return JSONResponse(
#             status_code=500, 
#             content={"error": str(e)}
#         )

# @app.post("/search-image/")
# async def search_image(
#     file: UploadFile = File(...), 
#     event_name: str = Form(None)
# ):
#     try:
#         # Ensure the uploaded file is an image
#         with Image.open(file.file) as img:
#             # Save the uploaded image temporarily
#             temp_filename = os.path.join(
#                 BASE_IMAGE_FOLDER, 
#                 f"temp_{uuid.uuid4()}.jpg"
#             )
#             img.save(temp_filename)
        
#         # Search for faces
#         result = face_service.search_image(temp_filename, event_name)
        
#         # Remove the temporary file
#         os.remove(temp_filename)
        
#         return result
#     except Exception as e:
#         return JSONResponse(
#             status_code=500, 
#             content={"error": str(e)}
#         )

# @app.get("/list-events/")
# async def list_events():
#     try:
#         return face_service.list_events()
#     except Exception as e:
#         return JSONResponse(
#             status_code=500, 
#             content={"error": str(e)}
#         )

# # Startup event to load models
# @app.on_event("startup")
# async def startup_event():
#     print("Face Recognition Service is starting up...")
#     print(f"Using device: {face_recognition_model.device}")