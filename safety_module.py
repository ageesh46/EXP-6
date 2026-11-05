import utils

RED_FLAGS = ["chest pain", "difficulty breathing", "shortness of breath",
             "can't breathe", "cannot breathe", "unconscious", "fainted",
             "severe bleeding", "seizure", "confusion", "stroke",
             "suicid", "self-harm", "blue lips", "stiff neck"]


def assess(state):
    """Option 6 - cautious escalation message (not a clinical triage)."""
    text = (state.get("symptom_text", "") + " " + " ".join(state.get("symptoms", []))).lower()
    flags = [f for f in RED_FLAGS if f in text]
    severe = state.get("severity") == "severe"
    child_or_elder = state.get("age", 30) < 3 or state.get("age", 30) > 65
    if flags or severe:
        level = "URGENT"
        msg = ("Some reported symptoms may need prompt attention. Please "
               "contact a healthcare professional or local emergency services "
               "as soon as possible.")
    elif child_or_elder:
        level = "CAUTION"
        msg = ("Because of the patient's age, consider consulting a "
               "healthcare professional even if symptoms seem mild.")
    else:
        level = "ROUTINE"
        msg = ("If symptoms are severe, rapidly worsening, or concerning, "
               "seek appropriate professional medical care.")
    utils.update_state(attention_level=level, attention=msg, red_flags=flags)
    return level, msg, flags


def show_attention(state):
    level, msg, flags = assess(state)
    print("\nMEDICAL ATTENTION")
    print(utils.DASH)
    print(msg)
    if flags:
        print("\nConcerning terms noticed: {}".format(", ".join(flags)))
    print("\nThis is general guidance, not a clinical triage decision.")
    print(utils.DASH)


def show_disclaimer():
    print("\nDISCLAIMER")
    print(utils.DASH)
    print(utils.DISCLAIMER)
    print(utils.DASH)
