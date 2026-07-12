import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="legal_documents"
        )

    def add_document(
        self,
        document_id,
        chunks,
        embeddings,
    ):

        ids = [
            f"{document_id}_{i}"
            for i in range(len(chunks))
        ]

        metadatas = [
            {"document_id": document_id}
            for _ in chunks
        ]

        self.collection.add(

            ids=ids,

            documents=chunks,

            embeddings=embeddings.tolist(),

            metadatas=metadatas,

        )

    def search(
        self,
        query_embedding,
        document_id,
        top_k=3,
    ):

        return self.collection.query(

            query_embeddings=[
                query_embedding.tolist()
            ],

            n_results=top_k,

            where={
                "document_id": document_id
            }

        )