import re

SECTION_HEADERS = [
    "abstract",
    "introduction",
    "background",
    "method",
    "methods",
    "approach",
    "experiment",
    "results",
    "discussion",
    "conclusion"
]


def split_into_sections(text):

    lines = text.split("\n")

    sections = []
    current_section = "unknown"
    buffer = []

    for line in lines:

        clean = line.strip().lower()

        if clean in SECTION_HEADERS:

            if buffer:
                sections.append(
                    (current_section, " ".join(buffer))
                )
                buffer = []

            current_section = clean
        else:
            buffer.append(line)

    if buffer:
        sections.append((current_section, " ".join(buffer)))

    return sections


def chunk_sections(text, chunk_size=250):

    sections = split_into_sections(text)

    chunks = []

    for section, content in sections:

        words = content.split()

        for i in range(0, len(words), chunk_size):

            chunk = " ".join(words[i:i + chunk_size])

            chunks.append({
                "text": chunk,
                "section": section
            })

    return chunks