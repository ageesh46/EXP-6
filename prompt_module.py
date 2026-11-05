import utils

SYSTEM = ("You are a cautious medical information assistant. You do not "
          "diagnose. Use only the information given and do not invent facts. "
          "Explain your reasoning at a general level and say clearly when "
          "the information is not enough.")

ANALYSIS_FORMAT = (
    "Reply using exactly these headings:\n"
    "POSSIBLE CONDITIONS:\n(3 to 5 conditions, one per line)\n"
    "EXPLANATION:\n(2 to 4 sentences on why they were considered)\n")


def build_analysis_prompt(state, verbose=True):
    prompt = (
        "Patient information:\nAge: {age}\nSex: {sex}\nHistory: {history}\n"
        "Medications: {medications}\nAllergies: {allergies}\n\n"
        "Reported symptoms: {symptoms}\nDuration: {duration}\n"
        "Severity: {severity}\n\n"
        "Task: Analyse the symptoms, list possible conditions that may be "
        "associated with them, and explain the reasoning in general terms. "
        "Do not give a definitive diagnosis.\n\n{fmt}"
    ).format(age=state.get("age"), sex=state.get("sex"),
             history=state.get("history"), medications=state.get("medications"),
             allergies=state.get("allergies"),
             symptoms=", ".join(state.get("symptoms", [])),
             duration=state.get("duration"), severity=state.get("severity"),
             fmt=ANALYSIS_FORMAT)
    if verbose:
        print("\nPROMPT GENERATION")
        print(utils.DASH)
        print("SYSTEM : {}".format(SYSTEM))
        print()
        print(prompt)
        print(utils.DASH)
    return prompt


def build_question_prompt(state):
    return ("Symptoms: {}\nDuration: {}\nSeverity: {}\nMissing information: {}\n\n"
            "Write 5 short follow-up questions a clinician might ask to "
            "understand this better. Output a numbered list only."
            ).format(", ".join(state.get("symptoms", [])), state.get("duration"),
                     state.get("severity"), "; ".join(state.get("missing", [])))
