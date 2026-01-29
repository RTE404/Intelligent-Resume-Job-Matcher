import re


def extract_citations(text):
    return re.findall(r"\[(R\d+|J\d+)\]", text)


def validate_citations(answer, resume_chunks, jd_chunks):
    valid = set()

    for i in range(len(resume_chunks)):
        valid.add(f"R{i}")

    for i in range(len(jd_chunks)):
        valid.add(f"J{i}")

    citations = extract_citations(answer)

    for c in citations:
        if c not in valid:
            return False

    return True
