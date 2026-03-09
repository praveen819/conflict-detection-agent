# detector.py
import json
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"


def detect_conflicts(text: str) -> dict:
    prompt = f"""
Analyze the following text and detect logical contradictions.

Return JSON ONLY in this format:
{{
  "conflicts": [
    {{
      "statement_1": "",
      "statement_2": "",
      "severity": "low | medium | high",
      "explanation": ""
    }}
  ]
}}

Text:
{text}
"""

    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "format": "json"
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    # Use ["message"]["content"] for /api/chat
    content = response.json()["message"]["content"]

    # Basic cleaning to handle potential markdown or whitespace
    content = content.strip()
    if content.startswith("```json"):
        content = content.replace(
            "```json", "", 1).replace("```", "", 1).strip()

    return json.loads(content)
