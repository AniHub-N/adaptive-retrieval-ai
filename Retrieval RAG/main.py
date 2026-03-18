from src.pipeline import run_pipeline

query = input("Ask a question: ")

answer, sources, confidence = run_pipeline(query)

print("\nAnswer:\n")
print(answer)

print("\nSources:")
for s in sources:
    print(s)

print("\nConfidence:", confidence)
