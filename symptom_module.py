import utils

SYSTEM = ("You extract symptoms from a patient's message. Output only the "
          "symptoms, one per line, as short medical terms. Do not add "
          "symptoms that were not mentioned.")

KEYWORDS = {"fever": "Fever", "cough": "Cough", "sore throat": "Sore throat",
            "throat": "Sore throat", "headache": "Headache", "tired": "Fatigue",
            "fatigue": "Fatigue", "nausea": "Nausea", "vomit": "Vomiting",
            "diarrhea": "Diarrhea", "runny nose": "Runny nose",
            "body pain": "Body pain", "chest pain": "Chest pain",
            "breath": "Breathing difficulty", "rash": "Rash", "dizz": "Dizziness"}


def keyword_extract(text):
    low = text.lower()
    found = []
    for key, name in KEYWORDS.items():
        if key in low and name not in found:
            found.append(name)
    return found


def extract_symptoms(text, verbose=True):
    """Option 2 - extract symptoms with the local model (keyword fallback)."""
    raw = utils.ask(SYSTEM, "Patient message: {}\nSymptoms:".format(text),
                    temperature=0.0)
    symptoms = [s.capitalize() for s in utils.bullets(raw)][:10]
    if not symptoms:
        symptoms = keyword_extract(text)
    utils.update_state(symptoms=symptoms)
    if verbose:
        print("\nEXTRACTED SYMPTOMS")
        print(utils.DASH)
        for s in symptoms:
            print("  - {}".format(s))
        print(utils.DASH)
    return symptoms
