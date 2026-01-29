from retrieval.retriever import Retriever

if __name__ == "__main__":
    retriever = Retriever()

    resume_chunks = [
        "Built FastAPI backend",
        "Trained CNN for image classification",
        "Used Python and PyTorch"
    ]

    jd_chunks = [
        "Looking for backend engineer with API experience",
        "Need deep learning experience"
    ]

    retriever.index_resume(resume_chunks)
    retriever.index_job_description(jd_chunks)

    res_matches = retriever.retrieve_resume_chunks(jd_chunks)

    print("Resume matches:")
    for r in res_matches:
        print(r.payload["text"])
