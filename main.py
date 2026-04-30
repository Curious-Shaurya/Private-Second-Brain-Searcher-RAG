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
    
    # 1. Add a document 
    brain.add_document(r"D:\AV Rising Stars Tuition\English\Plurals_and_Possessives_Worksheet_Final.docx")
        
    # 2. Ask a question
    info = brain.read_question("Which of the worksheets talk about plural possessives?")
    if info and info['documents']:
        # Get the lists for our one question
        all_docs = info['documents'][0]
        all_metas = info['metadatas'][0]

        print(f"\n{'='*60}")
        print(f"SEARCH RESULTS")
        print(f"{'='*60}")

        # zip() pairs (doc1, meta1), (doc2, meta2), etc.
        for text, metadata in zip(all_docs, all_metas):
            # 1. Get just the filename
            full_path = metadata.get("source", "Unknown Source")
            filename = os.path.basename(full_path)

            # 2. Create a preview (First 150 characters)
            preview = text.strip().replace("\n", " ")[:150]

            print(f"📄 FILE: {filename}")
            print(f"📝 PREVIEW: {preview}...")
            print(f"{'-'*60}")
    else:
        print("No matching information found.")
    
