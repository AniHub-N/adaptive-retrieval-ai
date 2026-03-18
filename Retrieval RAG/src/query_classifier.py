from .retriever import retrieve
from .reranker import rerank

def classify_query(query):

    q = query.lower()

    if "difference" in q or "compare" in q or "vs" in q:
        return "comparison"

    if "which" in q or "who" in q:
        return "multi-hop"

    if len(q.split()) > 12:
        return "broad"

    return "simple"


def adaptive_retrieve(query):

    query_type = classify_query(query)

    if query_type == "simple":
        k = 10
    elif query_type == "comparison":
        k = 30
    elif query_type == "multi-hop":
        k = 40
    else:
        k = 20

    docs = retrieve(query, k)
    ranked = rerank(query, docs)

    return ranked[:5]