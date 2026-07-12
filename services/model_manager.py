from services.embeddings import EmbeddingModel


_embedder = None


def get_embedder():

    global _embedder

    if _embedder is None:

        print("Loading Embedding Model...")

        _embedder = EmbeddingModel()

    return _embedder