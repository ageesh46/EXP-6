import utils

SYMPTOM_QUESTIONS = {
    "fever": "Exact temperature",
    "cough": "Whether the cough is dry or productive",
    "chest": "Whether the pain spreads to the arm or jaw",
    "headache": "Location and intensity of the headache",
    "vomit": "Whether fluids can be kept down",
    "diarrhea": "Number of episodes and signs of dehydration",
    "rash": "Whether the rash is spreading or itchy",
}


def find_missing(state, verbose=True):
    """Option 2 - identify information that would help the analysis."""
    missing = []
    if state.get("duration", "Not specified") == "Not specified":
        missing.append("Duration of the symptoms")
    if state.get("severity", "Not specified") == "Not specified":
        missing.append("Severity of the symptoms")
    text = " ".join(state.get("symptoms", [])).lower() + " " + state.get("symptom_text", "").lower()
    for key, item in SYMPTOM_QUESTIONS.items():
        if key in text:
            missing.append(item)
    if "breath" not in text:
        missing.append("Breathing difficulty")
    missing.append("Whether symptoms are improving or worsening")
    missing.append("Any additional symptoms")
    utils.update_state(missing=missing)
    if verbose:
        print("\nCONTEXT ANALYSIS - MISSING INFORMATION")
        print(utils.DASH)
        for m in missing:
            print("  - {}".format(m))
        print(utils.DASH)
    return missing
