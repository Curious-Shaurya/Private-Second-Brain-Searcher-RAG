import chromadb
import os
from chromadb.config import Settings

class VectorManager:
    def __init__(self, path: str = "./chroma_db"):

        self.client = chromadb.PersistentClient(path=path)
        # A 'collection' is where we store specific groups of vectors
        self.collection = self.client.get_or_create_collection(name="my_second_brain")

    def add_to_database(self, chunks: list[str], vectors: list, metadata: list[dict]):
        # We need to give each item a unique ID
        file_prefix = os.path.basename(metadata[0].get("source", "doc"))
        chunk_ids = [f"{file_prefix}_{i}" for i in range(len(chunks))]
        self.collection.add(
            ids=chunk_ids,
            embeddings=vectors,
            metadatas=metadata,
            documents=chunks
        )
        
    def search_database (self, query_embeddings: list[float], n_results: int):
        results = self.collection.query(
            query_embeddings=[query_embeddings],
            n_results=n_results 
        )
        
        return results