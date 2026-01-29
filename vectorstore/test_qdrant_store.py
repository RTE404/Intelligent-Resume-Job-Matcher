from embeddings.embedder import Embedder
from vectorstore.qdrant_store import QdrantStore


if __name__ == "__main__":
    embedder = Embedder()
    store = QdrantStore(collection_name="test_collection")

    texts = [
        "I built a FastAPI backend",
        "I play football",
        "I trained a CNN model"
    ]

    vectors = embedder.embed_texts(texts)

    store.add_texts(texts, vectors)

    query = embedder.embed_texts(["backend development"])[0]

    results = store.search(query, top_k=2)

    for r in results:
        print(r.payload["text"])
