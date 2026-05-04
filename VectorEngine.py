from sentence_transformers import SentenceTransformer

class EmbeddingEngine:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name, local_files_only=True)

    def embed_chunks(self, text_chunks: list[str]):
        return self.model.encode(text_chunks)