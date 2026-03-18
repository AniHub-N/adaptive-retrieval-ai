from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_answer(query, context):

    context = context[:1500]

    prompt = f"""
You are a research assistant.

Answer the question using ONLY the evidence provided.

Write a short 2-3 sentence explanation.

Evidence:
{context}

Question: {query}

Answer:
"""

    result = generator(prompt, max_new_tokens=120)

    return result[0]["generated_text"]