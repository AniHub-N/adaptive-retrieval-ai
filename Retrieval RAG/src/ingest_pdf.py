import fitz  # PyMuPDF
import json
from .chunker import chunk_sections


def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    full_text = ""

    for page in doc:
        full_text += page.get_text()

    return full_text


def pdf_to_chunks(pdf_path, paper_title):

    text = extract_text_from_pdf(pdf_path)

    from src.chunker import chunk_sections

    text_chunks = chunk_sections(text)

    chunks = []

    for c in text_chunks:

        chunks.append({
            "text": c["text"],
            "paper": paper_title,
            "section": c["section"]
        })

    return chunks


def save_chunks(chunks, output_path):

    with open(output_path, "w") as f:
        json.dump(chunks, f, indent=2)
