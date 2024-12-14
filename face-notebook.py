{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Install required packages\n",
    "!pip install -q -r ../requirements.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "sys.path.append('..')\n",
    "\n",
    "from src.models.face_recognition import FaceRecognitionModel\n",
    "from src.models.embedding_manager import FaissEmbeddingManager\n",
    "from src.services.face_service import FaceService\n",
    "from config import FAISS_INDEX_FILE\n",
    "from google.colab import files\n",
    "\n",
    "# Initialize models and services\n",
    "face_recognition_model = FaceRecognitionModel()\n",
    "embedding_manager = FaissEmbeddingManager.load(FAISS_INDEX_FILE)\n",
    "face_service = FaceService(face_recognition_model, embedding_manager)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def upload_and_process_faces():\n",
    "    print(\"Please upload one or more images containing faces...\")\n",
    "    event_name = input(\"Enter event name: \")\n",
    "    \n",
    "    uploaded = files.upload()\n",
    "    results = []\n",
    "    \n",
    "    for filename, content in uploaded.items():\n",
    "        with open(filename, 'wb') as f:\n", 
    "            f.write(content)\n",
    "        result = face_service.process_image(filename, event_name)\n",
    "        results.append(result)\n",
    "        os.remove(filename)\n",
    "    \n",
    "    return results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def search_faces():\n",
    "    print(\"Please upload an image to search for matching faces...\")\n",
    "    event_name = input(\"Enter event name (or press Enter to search all events): \").strip()\n",
    "    event_name = event_name if event_name else None\n",
    "    \n",
    "    uploaded = files.upload()\n",
    "    results = []\n",
    "    \n",
    "    for filename, content in uploaded.items():\n",
    "        with open(filename, 'wb') as f:\n",
    "            f.write(content)\n",
    "        result = face_service.search_image(filename, event_name)\n",
    "        results.append(result)\n",
    "        os.remove(filename)\n",
    "    \n",
    "    return results"
   ]
  }
 ]
}