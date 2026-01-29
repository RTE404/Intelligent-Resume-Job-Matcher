def build_prompt(resume_chunks, jd_chunks):

    def dedup(results):
        seen = set()
        unique = []
        for r in results:
            if r.payload["text"] not in seen:
                unique.append(r)
                seen.add(r.payload["text"])
        return unique

    resume_chunks = dedup(resume_chunks)
    jd_chunks = dedup(jd_chunks)

    resume_text = "\n".join(
        [f"[R{i}] {c.payload['text']}" for i, c in enumerate(resume_chunks)]
    )

    jd_text = "\n".join(
        [f"[J{i}] {c.payload['text']}" for i, c in enumerate(jd_chunks)]
    )

    prompt = f"""
You are an AI evaluator.

You must ONLY use the information inside the following evidence blocks.

If information is missing, say: "Insufficient evidence".

Resume Evidence:
{resume_text}

Job Description Evidence:
{jd_text}

TASK:

Return a structured report with bullet points only:

Match Summary:
- bullet [R# or J#]
- bullet [R# or J#]

Strengths:
- bullet [R#]

Missing Skills:
- bullet [J#]

Improvement Suggestions:
- bullet


"""

    return prompt
