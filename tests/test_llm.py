from services.embeddings import EmbeddingModel
from services.vector_store import VectorStore
from services.semantic_search import SemanticSearch
from services.legal_analyzer import LegalAnalyzer

embedder = EmbeddingModel()

store = VectorStore()

semantic = SemanticSearch(
    embedder,
    store,
)

analyzer = LegalAnalyzer(
    semantic,
)

answer = analyzer.analyze(
    "What are the termination conditions?",
    "doc_5",
)

print(answer)