from src.ingest_pdf import pdf_to_chunks, save_chunks

pdf_path = "data/papers/rag_paper.pdf"

chunks = pdf_to_chunks(pdf_path, "RAG Paper")

save_chunks(chunks, "data/sample_chunks.json")

print("PDF converted into chunks successfully.")