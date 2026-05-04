from DocumentProcessor import DocumentProcessor
from VectorEngine import EmbeddingEngine
from database import VectorManager
import os

class SecondBrain:
    def __init__(self):
        self.processor = DocumentProcessor()
        self.vectors = EmbeddingEngine()
        self.database = VectorManager()
    
    def add_document(self, file_path: str):
        if not os.path.exists(file_path):
            print(f" ERROR: I can't find the file at: {file_path}")
            print(f" Looking at absolute path: {os.path.abspath(file_path)}")
            return  # Stop here so it doesn't crash later
    
    
        chunks = self.processor.processFile(file_path)
        if not chunks or len(chunks) == 0:
            print(f"WARNING: No text could be extracted from {file_path}. Skipping.")
            return # Safely exit without crashing
        
        vectors = self.vectors.embed_chunks(chunks)
        
        metadata = [{"source": file_path} for _ in range(len(chunks))]
        
        self.database.add_to_database(chunks=chunks, metadata=metadata, vectors=vectors)
        
    def read_question(self, question: str, n_results: int = 1):
        vectors = self.vectors.embed_chunks([question]) [0]
        results = self.database.search_database(
            query_embeddings=vectors, 
            n_results=n_results
        )
        
        return results
        
if __name__ == "__main__":
    brain = SecondBrain()
        
    info = brain.read_question("Which of the worksheets talk about plural possessives?")
    if info and info['documents']:
        all_docs = info['documents'][0]
        all_metas = info['metadatas'][0]

        print(f"\n{'='*60}")
        print(f"SEARCH RESULTS")
        print(f"{'='*60}")

        for text, metadata in zip(all_docs, all_metas):

            full_path = metadata.get("source", "Unknown Source")
            filename = os.path.basename(full_path)

            preview = text.strip().replace("\n", " ")[:150]

            print(f"📄 FILE: {filename}")
            print(f"📝 PREVIEW: {preview}...")
            print(f"{'-'*60}")
    else:
        print("No matching information found.")
    
