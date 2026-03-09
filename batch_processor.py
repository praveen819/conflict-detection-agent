# batch_processor.py
from detector import detect_conflicts


def process_batch(input_file: str):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    cases = content.strip().split("\n\n")
    results = []

    for i, text in enumerate(cases, start=1):
        result = detect_conflicts(text)
        results.append({
            "case_id": i,
            "input": text,
            "result": result
        })

    return results
