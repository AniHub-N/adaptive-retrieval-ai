import numpy as np
from .ingest import embedding_model, index, chunks

def retrieve(query, k=3):

    k = min(k, len(chunks))

    query_embedding = embedding_model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding), k
    )

    results = [chunks[i] for i in indices[0]]

    return results