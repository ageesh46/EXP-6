import utils


def save_profile(info):
    utils.update_state(**info)


def show_profile(state):
    print("\nPATIENT PROFILE")
    print(utils.DASH)
    rows = [("Age", state.get("age", "")), ("Sex", state.get("sex", "")),
            ("Medical History", state.get("history", "")),
            ("Medications", state.get("medications", "")),
            ("Allergies", state.get("allergies", "")),
            ("Duration", state.get("duration", "")),
            ("Severity", state.get("severity", ""))]
    for label, value in rows:
        print("{:<16}: {}".format(label, value))
    print(utils.DASH)
