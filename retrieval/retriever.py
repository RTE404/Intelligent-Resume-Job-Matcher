from embeddings.embedder import Embedder
from vectorstore.qdrant_store import QdrantStore


class Retriever:
    """
    Handles bidirectional retrieval between resumes and job descriptions.
    """

    def __init__(self):
        self.embedder = Embedder()
        self.resume_store = QdrantStore("resumes")
        self.jd_store = QdrantStore("job_descriptions")

    def index_resume(self, chunks: list[str]):
        vectors = self.embedder.embed_texts(chunks)
        self.resume_store.add_texts(chunks, vectors)

    def index_job_description(self, chunks: list[str]):
        vectors = self.embedder.embed_texts(chunks)
        self.jd_store.add_texts(chunks, vectors)

    def retrieve_resume_chunks(self, jd_chunks: list[str], top_k: int = 3):
        retrieved = []

        for chunk in jd_chunks:
            q_vec = self.embedder.embed_texts([chunk])[0]
            results = self.resume_store.search(q_vec, top_k)
            retrieved.extend(results)

        return retrieved

    def retrieve_jd_chunks(self, resume_chunks: list[str], top_k: int = 3):
        retrieved = []

        for chunk in resume_chunks:
            q_vec = self.embedder.embed_texts([chunk])[0]
            results = self.jd_store.search(q_vec, top_k)
            retrieved.extend(results)

        return retrieved
