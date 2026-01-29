from retrieval.retriever import Retriever
from rag.prompt_builder import build_prompt


if __name__ == "__main__":
    retriever = Retriever()

    resume_chunks = [
        "Built FastAPI backend",
        "Trained CNN for image classification",
        "Used Python and PyTorch"
    ]

    jd_chunks = [
        "Looking for backend engineer",
        "Need deep learning experience"
    ]

    retriever.index_resume(resume_chunks)
    retriever.index_job_description(jd_chunks)

    res_matches = retriever.retrieve_resume_chunks(jd_chunks)
    jd_matches = retriever.retrieve_jd_chunks(resume_chunks)

    prompt = build_prompt(res_matches, jd_matches)

    print(prompt)
