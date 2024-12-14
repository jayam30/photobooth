import os
import pickle
import numpy as np
import faiss
from config import SIMILARITY_THRESHOLD

class FaissEmbeddingManager:
    def __init__(self, dimension=512):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.id_to_metadata = {}
    
    def add_embedding(self, embedding, image_path, event_name):
        faiss_id = len(self.id_to_metadata)
        self.index.add(np.array([embedding]))
        self.id_to_metadata[faiss_id] = {
            'image_path': image_path,
            'event_name': event_name
        }
    
    def search(self, query_embedding, event_name=None, threshold=SIMILARITY_THRESHOLD):
        k = len(self.id_to_metadata) if len(self.id_to_metadata) > 0 else 1
        distances, indices = self.index.search(np.array([query_embedding]), k)
        
        matched_images = []
        for dist, idx in zip(distances[0], indices[0]):
            similarity = 1 / (1 + dist)
            
            if similarity >= (1 - threshold):
                metadata = self.id_to_metadata.get(int(idx))
                if metadata and (event_name is None or metadata['event_name'] == event_name):
                    matched_images.append({
                        'image_path': metadata['image_path'],
                        'event_name': metadata['event_name'],
                        'similarity': float(similarity)
                    })
        
        return matched_images
    
    def save(self, filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        faiss.write_index(self.index, filepath + ".index")
        with open(filepath + "_metadata.pkl", 'wb') as f:
            pickle.dump(self.id_to_metadata, f)
    
    @classmethod
    def load(cls, filepath):
        instance = cls()
        if os.path.exists(filepath + ".index"):
            instance.index = faiss.read_index(filepath + ".index")
            with open(filepath + "_metadata.pkl", 'rb') as f:
                instance.id_to_metadata = pickle.load(f)
        return instance