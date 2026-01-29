from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct


class QdrantStore:
    """
    Wrapper around Qdrant vector database.
    """

    def __init__(self, collection_name: str):
        self.client = QdrantClient(":memory:")
        self.collection_name = collection_name

        self._create_collection_if_not_exists()

    def _create_collection_if_not_exists(self):
        collections = self.client.get_collections().collections
        names = [c.name for c in collections]

        if self.collection_name not in names:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE
                )
            )

    def add_texts(self, texts: list[str], embeddings: list[list[float]]):
        points = []

        for idx, (text, vector) in enumerate(zip(texts, embeddings)):
            points.append(
                PointStruct(
                    id=idx,
                    vector=vector,
                    payload={"text": text}
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(self, query_vector: list[float], top_k: int = 5):
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k
        )
        return results
