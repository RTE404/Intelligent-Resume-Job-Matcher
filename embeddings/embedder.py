from sentence_transformers import SentenceTransformer


class Embedder:
    """
    Wrapper around SentenceTransformer embedding model.
    """

    def __init__(self, model_name: str = "sentence-transformers/all-mpnet-base-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """
        Converts list of texts into list of embedding vectors.
        """
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )
        return embeddings.tolist()
