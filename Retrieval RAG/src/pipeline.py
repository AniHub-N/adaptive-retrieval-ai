from .multihop import multi_hop_retrieve
from .citations import format_with_citations
from .confidence import compute_confidence
from .generator import generate_answer


def run_pipeline(query):

    results = multi_hop_retrieve(query)

    results = results[:3]

    context, sources = format_with_citations(results)

    answer = generate_answer(query, context)

    confidence = compute_confidence(results)

    return answer, sources, confidence