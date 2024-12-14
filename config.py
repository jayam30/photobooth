import os
import torch

# Directory Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_IMAGE_FOLDER = os.path.join(BASE_DIR, "uploaded_images")
FAISS_INDEX_FILE = os.path.join(BASE_DIR, "faiss_index")

# Ensure directories exist
os.makedirs(BASE_IMAGE_FOLDER, exist_ok=True)

# Device Configuration
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Model Configuration
FACE_DETECTION_CONFIG = {
    'image_size': 160,
    'margin': 0,
    'min_face_size': 20,
    'keep_all': True
}

# Search Configuration
SIMILARITY_THRESHOLD = 0.6