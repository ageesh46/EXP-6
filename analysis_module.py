import prompt_module
import utils


def split_sections(text):
    """Split the model reply into POSSIBLE CONDITIONS and EXPLANATION."""
    low = text.upper()
    i = low.find("POSSIBLE CONDITIONS")
    j = low.find("EXPLANATION")
    if i == -1:
        return [], text.strip()
    cond_end = j if j > i else len(text)
    conditions = utils.bullets(text[i:cond_end].split(":", 1)[-1])
    explanation = text[j:].split(":", 1)[-1].strip() if j != -1 else ""
    return conditions, explanation


def analyze(state, verbose=True):
    """Option 3 - preliminary symptom analysis with the local model."""
    if not state.get("symptoms"):
        raise ValueError("Enter patient information and symptoms first")
    prompt = prompt_module.build_analysis_prompt(state, verbose)
    raw = utils.ask(prompt_module.SYSTEM, prompt)
    conditions, explanation = split_sections(raw)
    utils.update_state(raw_analysis=raw, conditions=conditions, explanation=explanation)
    if verbose:
        print("\nMODEL RESPONSE")
        print(utils.DASH)
        print(raw)
        print(utils.DASH)
    return conditions, explanation


def show_conditions(state):
    print("\nPOSSIBLE CONDITIONS")
    print(utils.DASH)
    for i, c in enumerate(state.get("conditions", []), 1):
        print("{}. {}".format(i, c))
    print("\nNote: These symptoms can occur in multiple conditions.")
    print("The information provided is not sufficient to establish a diagnosis.")
    print(utils.DASH)
