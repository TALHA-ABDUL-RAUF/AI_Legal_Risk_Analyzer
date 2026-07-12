from services.embeddings import EmbeddingModel
from services.vector_store import VectorStore


class SemanticSearch:

    def __init__(
        self,
        embedder: EmbeddingModel,
        vector_store: VectorStore,
    ):
        self.embedder = embedder
        self.vector_store = vector_store

    def search(
        self,
        question: str,
        document_id: str,
        top_k: int = 3,
    ):

        query_embedding = self.embedder.encode([question])[0]

        results = self.vector_store.search(
            query_embedding=query_embedding,
            document_id=document_id,
            top_k=top_k,
        )

        return results