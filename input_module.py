import pandas as pd

import utils

SEVERITIES = ["mild", "moderate", "severe"]


def ask_text(label, default=""):
    value = input("{}: ".format(label)).strip()
    return value or default


def get_patient_info():
    """Option 1 - collect basic patient information."""
    print("\nPATIENT INFORMATION")
    print(utils.DASH)
    age = ask_text("Age")
    if not age.isdigit() or not (0 < int(age) < 120):
        raise ValueError("Age must be a number between 1 and 119")
    info = {
        "age": int(age),
        "sex": ask_text("Sex (if relevant)", "Not specified"),
        "history": ask_text("Relevant medical history", "None reported"),
        "medications": ask_text("Current medications (if relevant)", "None reported"),
        "allergies": ask_text("Allergies (if relevant)", "None reported"),
    }
    return info


def get_symptom_input():
    """Option 2 - collect symptoms as natural language."""
    print("\nSYMPTOM INPUT")
    print(utils.DASH)
    text = ask_text("Describe your symptoms")
    if len(text) < 3:
        raise ValueError("Please describe at least one symptom")
    duration = ask_text("Duration (e.g. 2 days)", "Not specified")
    severity = ask_text("Severity {}".format(SEVERITIES), "Not specified").lower()
    if severity != "not specified" and severity not in SEVERITIES:
        raise ValueError("Severity must be one of {}".format(SEVERITIES))
    return {"symptom_text": text, "duration": duration, "severity": severity}


def load_sample_case(row=0):
    """Load a sample case from data/sample_cases.csv (used for testing)."""
    df = pd.read_csv("data/sample_cases.csv")
    return df.iloc[row].to_dict()
