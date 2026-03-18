from .query_classifier import adaptive_retrieve
from .retriever import retrieve
from .reranker import rerank

def extract_entities(text):

    words = text.split()
    entities = []

    for w in words:
        if w.istitle():
            entities.append(w)

    return entities[:3]


def multi_hop_retrieve(query):

    docs = adaptive_retrieve(query)

    collected_docs = [d[0] for d in docs]

    new_queries = []

    for doc, score in docs:
        entities = extract_entities(doc["text"])
        new_queries.extend(entities)

    for q in new_queries[:2]:

        more_docs = retrieve(q, k=10)
        collected_docs.extend(more_docs)

    unique_chunks = {}

    for doc in collected_docs:
        key = doc["text"]

        if key not in unique_chunks:
            unique_chunks[key] = doc

    final_ranked = rerank(query, list(unique_chunks.values()))

    return final_ranked[:5]