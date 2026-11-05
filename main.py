import analysis_module
import context_module
import input_module
import profile_module
import question_module
import safety_module
import save_module
import symptom_module
import utils

MENU = """
1. Enter Patient Information
2. Enter Symptoms
3. Analyze Symptoms
4. Generate Follow-up Questions
5. Display Possible Conditions
6. Display Medical Attention Guidance
7. Display Disclaimer
8. Save Report
9. Exit"""


def run(choice):
    state = utils.load_state()
    if choice == "1":
        profile_module.save_profile(input_module.get_patient_info())
    elif choice == "2":
        data = input_module.get_symptom_input()
        utils.update_state(**data)
        symptom_module.extract_symptoms(data["symptom_text"])
        state = utils.load_state()
        profile_module.show_profile(state)
        context_module.find_missing(state)
    elif choice == "3":
        analysis_module.analyze(state)
    elif choice == "4":
        question_module.generate_questions(state)
    elif choice == "5":
        analysis_module.show_conditions(state)
    elif choice == "6":
        safety_module.show_attention(state)
    elif choice == "7":
        safety_module.show_disclaimer()
    elif choice == "8":
        save_module.save_report(state)
    else:
        print("Choose a number from 1 to 9")


def main():
    print("===== AI-POWERED MEDICAL SYMPTOM ASSISTANT =====")
    print("Educational information only - NOT a medical diagnosis.")
    while True:
        print(MENU)
        choice = input("Select an option: ").strip()
        if choice == "9":
            print("Goodbye!")
            break
        try:
            run(choice)
        except (ValueError, utils.ModelError) as exc:
            print("Error: {}".format(exc))


if __name__ == "__main__":
    main()
