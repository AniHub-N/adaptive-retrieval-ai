from rank_bm25 import BM25Okapi
import numpy as np
from .ingest import embedding_model, index, chunks

tokenized_corpus = [
    c["text"].split() for c in chunks
]

bm25 = BM25Okapi(tokenized_corpus)

def retrieve(query, k=3):

    k = min(k, len(chunks))

    query_embedding = embedding_model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding), k
    )

    results = [chunks[i] for i in indices[0]]

    return results

def bm25_retrieve(query, k=10):

    tokens = query.split()

    scores = bm25.get_scores(tokens)

    ranked = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    results = [chunks[i] for i in ranked[:k]]

    return results

def hybrid_retrieve(query, k=20):

    vector_docs = retrieve(query, k)
    bm25_docs = bm25_retrieve(query, k)

    merged = {}

    for doc in vector_docs + bm25_docs:

        key = doc["text"]

        if key not in merged:
            merged[key] = doc

    return list(merged.values())