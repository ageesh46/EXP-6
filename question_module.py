import prompt_module
import utils

DEFAULT = ["What is your measured temperature?",
           "When exactly did the symptoms begin?",
           "Are you experiencing difficulty breathing?",
           "Are the symptoms improving or worsening?",
           "Do you have any other symptoms?"]


def generate_questions(state, verbose=True):
    """Option 4 - generate follow-up questions."""
    if not state.get("symptoms"):
        raise ValueError("Enter patient information and symptoms first")
    raw = utils.ask(prompt_module.SYSTEM, prompt_module.build_question_prompt(state))
    questions = [q for q in utils.bullets(raw) if q.endswith("?")][:6] or DEFAULT
    utils.update_state(questions=questions)
    if verbose:
        print("\nFOLLOW-UP QUESTIONS")
        print(utils.DASH)
        for i, q in enumerate(questions, 1):
            print("{}. {}".format(i, q))
        print(utils.DASH)
    return questions
