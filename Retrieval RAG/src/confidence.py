def compute_confidence(ranked_docs):

    scores = [score for _, score in ranked_docs]

    avg_score = sum(scores) / len(scores)

    evidence_bonus = min(len(ranked_docs) / 5, 1)

    confidence = avg_score * 0.7 + evidence_bonus * 0.3

    return confidence