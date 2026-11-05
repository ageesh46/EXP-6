# AI-Powered Medical Symptom Assistant (Experiment 6, 24CS2506)

Educational tool using a local LLM (Ollama, llama3.2). Not a medical diagnosis.

Setup:
    pip install -r requirements.txt
    ollama pull llama3.2
Run:
    python main.py
Suggested demo: option 1 (age 22, female) -> option 2 ("I have been having fever and cough for two days. My throat is also painful.", 2 days, mild) -> 3 -> 4 -> 5 -> 6 -> 7 -> 8.
Report is saved to outputs/medical_analysis.txt. Sample cases: data/sample_cases.csv.
