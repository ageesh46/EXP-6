import datetime
import os

import safety_module
import utils


def build_report(state):
    safety_module.assess(state)
    state = utils.load_state()
    L = lambda items: ["  - {}".format(i) for i in items] or ["  - None"]
    lines = ["MEDICAL SYMPTOM ANALYSIS", "=" * 50,
             "Date: {}".format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M")),
             "=" * 50, "", "1. REPORTED SYMPTOMS"] + L(state.get("symptoms", []))
    lines += ["", "2. PATIENT INFORMATION",
              "  Age: {}".format(state.get("age")), "  Sex: {}".format(state.get("sex")),
              "  History: {}".format(state.get("history")),
              "  Medications: {}".format(state.get("medications")),
              "  Allergies: {}".format(state.get("allergies")),
              "  Duration: {}".format(state.get("duration")),
              "  Severity: {}".format(state.get("severity")),
              "", "3. POSSIBLE CONDITIONS"] + L(state.get("conditions", []))
    lines += ["", "4. EXPLANATION", "  " + state.get("explanation", ""),
              "", "5. MISSING INFORMATION"] + L(state.get("missing", []))
    lines += ["", "6. FOLLOW-UP QUESTIONS"] + [
        "  {}. {}".format(i, q) for i, q in enumerate(state.get("questions", []), 1)]
    lines += ["", "7. MEDICAL ATTENTION GUIDANCE", "  " + state.get("attention", ""),
              "", "8. DISCLAIMER", utils.DISCLAIMER, ""]
    return "\n".join(lines)


def save_report(state, verbose=True):
    """Option 8 - save the structured report to outputs/medical_analysis.txt."""
    if not state.get("conditions"):
        raise ValueError("Run 'Analyze Symptoms' before saving the report")
    try:
        os.makedirs(utils.OUTPUT_DIR, exist_ok=True)
        with open(utils.REPORT_FILE, "w") as f:
            f.write(build_report(state))
    except OSError as exc:
        raise utils.ModelError("Could not save the report: {}".format(exc))
    if verbose:
        print("\nReport saved to {}".format(utils.REPORT_FILE))
