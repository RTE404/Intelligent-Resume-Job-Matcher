from ingestion.pdf_parser import extract_text_from_pdf
from ingestion.cleaner import clean_text
from chunking.semantic_chunker import chunk_text


if __name__ == "__main__":
    raw = extract_text_from_pdf("sample_resume.pdf")
    cleaned = clean_text(raw)
    chunks = chunk_text(cleaned)

    print(f"Total chunks: {len(chunks)}")
    print(chunks[0][:300])
