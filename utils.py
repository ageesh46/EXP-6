import json
import os

import ollama

MODEL = "llama3.2:latest"
OUTPUT_DIR = "outputs"
REPORT_FILE = os.path.join(OUTPUT_DIR, "medical_analysis.txt")
STATE_FILE = os.path.join(OUTPUT_DIR, "state.json")
DASH = "-" * 50

DISCLAIMER = (
    "This AI-generated response is intended for\n"
    "educational and informational purposes only.\n\n"
    "It is not a medical diagnosis and does not\n"
    "replace advice from a qualified healthcare\n"
    "professional.\n\n"
    "For serious, worsening or urgent symptoms,\n"
    "seek appropriate medical care."
)


class ModelError(Exception):
    pass


def ask(system, prompt, temperature=0.2):
    """Send one prompt to the local Ollama model and return the text."""
    try:
        resp = ollama.chat(
            model=MODEL,
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": prompt}],
            options={"temperature": temperature},
        )
        return resp["message"]["content"].strip()
    except Exception as exc:
        raise ModelError("Ollama request failed: {}".format(exc))


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def update_state(**kwargs):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    state = load_state()
    state.update(kwargs)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
    return state


def bullets(text):
    """Turn model text into a clean list of items (drops bullets/numbers)."""
    items = []
    for line in text.splitlines():
        line = line.strip().lstrip("-*\u2022").strip()
        if line[:2].rstrip(".) ").isdigit():
            line = line.split(" ", 1)[-1].strip()
        if line and not line.endswith(":"):
            items.append(line)
    return items
