from services.validator import validate_file
from services.extractor import TextExtractor
from services.chunker import TextChunker
from services.embeddings import EmbeddingModel
from services.vector_store import VectorStore
from services.semantic_search import SemanticSearch

FILE = "tests/sample.pdf"
DOCUMENT_ID = "doc_001"

print("=" * 60)
print("STEP 1 - VALIDATION")
print("=" * 60)

valid, message = validate_file(FILE)

print(valid, message)

if not valid:
    exit()

print("\n")

print("=" * 60)
print("STEP 2 - EXTRACTION")
print("=" * 60)

text = TextExtractor.extract_text(FILE)

print(text[:300])

print("\n")

print("=" * 60)
print("STEP 3 - CHUNKING")
print("=" * 60)

chunker = TextChunker()

chunks = chunker.split(text)

print("Chunks:", len(chunks))

print("\n")

print("=" * 60)
print("STEP 4 - EMBEDDINGS")
print("=" * 60)

embedder = EmbeddingModel()

embeddings = embedder.encode(chunks)

print("Embedding Shape:", embeddings.shape)

print("\n")

print("=" * 60)
print("STEP 5 - STORE IN CHROMADB")
print("=" * 60)

store = VectorStore()

store.add_document(
    DOCUMENT_ID,
    chunks,
    embeddings,
)

print("Stored Successfully")

print("\n")

print("=" * 60)
print("STEP 6 - SEMANTIC SEARCH")
print("=" * 60)


store = VectorStore()

search = SemanticSearch(
    embedder=embedder,
    vector_store=store,
)
results = search.search(
    "What are the termination conditions?",
    DOCUMENT_ID,
)

print(results)