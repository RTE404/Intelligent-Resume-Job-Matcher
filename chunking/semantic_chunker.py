import re


def chunk_text(text: str) -> list[str]:
    """
    Baseline semantic-ish chunking.
    Splits text at common resume section headers (case-insensitive).
    """

    separators = [
        "education",
        "experience",
        "projects",
        "skills",
        "skills summary",
        "achievements",
        "certifications",
        "summary"
    ]

    # Build regex pattern: (?i) = case-insensitive
    pattern = r"(?i)(" + "|".join(separators) + r")"

    parts = re.split(pattern, text)

    chunks = []
    current_chunk = ""

    for part in parts:
        if part.lower() in separators:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = part
        else:
            current_chunk += " " + part

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks
