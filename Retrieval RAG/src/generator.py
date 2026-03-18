from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=150
)

def generate_answer(query, context):

    prompt = f"""
Use the following evidence to answer the question.

Evidence:
{context}

Question:
{query}

Answer:
"""

    result = generator(prompt)

    return result[0]["generated_text"]