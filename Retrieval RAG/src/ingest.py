import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/sample_chunks.json", "r") as f:
    chunks = json.load(f)

texts = [c["text"] for c in chunks]
embeddings = embedding_model.encode(texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))