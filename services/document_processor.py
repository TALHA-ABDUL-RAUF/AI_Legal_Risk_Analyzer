from pathlib import Path

from services.validator import validate_file
from services.extractor import TextExtractor
from services.chunker import TextChunker
from services.embeddings import EmbeddingModel
from services.vector_store import VectorStore
from services.model_manager import get_embedder


class DocumentProcessor:

    def __init__(self):

        self.chunker = TextChunker()

        self.embedder = get_embedder()

        self.vector_store = VectorStore()

    def process_document(
        self,
        file_path: str,
        document_id: str,
    ) -> dict:
        """
        Complete document ingestion pipeline.

        Returns:
            {
                "success": bool,
                "message": str,
                "chunks": int
            }
        """

        # -----------------------------
        # Step 1
        # Validate
        # -----------------------------

        valid, message = validate_file(file_path)

        if not valid:
            return {
                "success": False,
                "message": message,
            }

        # -----------------------------
        # Step 2
        # Extract Text
        # -----------------------------

        text = TextExtractor.extract_text(file_path)

        if not text.strip():
            return {
                "success": False,
                "message": "Document contains no readable text.",
            }

        # -----------------------------
        # Step 3
        # Chunk Text
        # -----------------------------

        chunks = self.chunker.split(text)

        if len(chunks) == 0:
            return {
                "success": False,
                "message": "No chunks were generated.",
            }

        # -----------------------------
        # Step 4
        # Generate Embeddings
        # -----------------------------

        embeddings = self.embedder.encode(chunks)

        # -----------------------------
        # Step 5
        # Store in ChromaDB
        # -----------------------------

        self.vector_store.add_document(
            document_id=document_id,
            chunks=chunks,
            embeddings=embeddings,
        )

        # -----------------------------
        # Done
        # -----------------------------

        return {
            "success": True,
            "message": "Document processed successfully.",
            "chunks": len(chunks),
        }