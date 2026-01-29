from embeddings.embedder import Embedder


if __name__ == "__main__":
    embedder = Embedder()

    texts = [
        "I built a FastAPI backend",
        "I like playing football"
    ]

    vectors = embedder.embed_texts(texts)

    print(len(vectors))
    print(len(vectors[0]))
