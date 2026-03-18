def format_with_citations(docs):

    context = ""
    sources = []

    for i, (doc, score) in enumerate(docs):

        source_id = i + 1

        context += f"[{source_id}] {doc['text']}\n\n"

        sources.append(
            f"[{source_id}] {doc['paper']} ({doc['section']})"
        )

    return context, sources