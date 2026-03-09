# main.py
import json
from batch_processor import process_batch

results = process_batch("inputs.txt")

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("✅ Conflict detection completed. Output saved to output.json")
