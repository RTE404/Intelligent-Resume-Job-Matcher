from fastapi import FastAPI, UploadFile, File, Form
from dotenv import load_dotenv
import tempfile

from ingestion.pdf_parser import extract_text_from_pdf
from ingestion.cleaner import clean_text
from chunking.semantic_chunker import chunk_text
from retrieval.retriever import Retriever
from rag.prompt_builder import build_prompt
from rag.llm_client import LLMClient

load_dotenv(dotenv_path=".env")

app = FastAPI(title="Resume Job Matcher")

retriever = Retriever()
llm = LLMClient()


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/match")
async def match_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        content = await resume.read()
        tmp.write(content)
        tmp_path = tmp.name

    # Ingestion
    raw = extract_text_from_pdf(tmp_path)
    cleaned = clean_text(raw)
    resume_chunks = chunk_text(cleaned)

    jd_chunks = chunk_text(job_description)

    # Index
    retriever.index_resume(resume_chunks)
    retriever.index_job_description(jd_chunks)

    # Retrieve
    res_matches = retriever.retrieve_resume_chunks(jd_chunks)
    jd_matches = retriever.retrieve_jd_chunks(resume_chunks)

    # Build prompt
    prompt = build_prompt(res_matches, jd_matches)

    # Generate answer
    answer = llm.generate(prompt)

    return {"result": answer}
