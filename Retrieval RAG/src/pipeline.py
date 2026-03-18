from .multihop import multi_hop_retrieve
from .citations import format_with_citations
from .confidence import compute_confidence


def run_pipeline(query):

    results = multi_hop_retrieve(query)

    context, sources = format_with_citations(results)

    confidence = compute_confidence(results)

    return context, sources, confidence