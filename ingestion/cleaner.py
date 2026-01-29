import ftfy


def clean_text(text: str) -> str:
    """
    Basic text normalization:
    - Fix unicode issues
    - Preserve line breaks
    - Normalize whitespace per line
    """

    text = ftfy.fix_text(text)

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    text = "\n".join(lines)

    return text
