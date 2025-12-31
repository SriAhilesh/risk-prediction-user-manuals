from src.preprocessing.load_dataset import load_dataset
from src.preprocessing.text_cleaning import clean_text
from src.risk_detection.risk_rules import (
    detect_ambiguity,
    detect_cognitive_overload,
    detect_sequence_dependency
)

DATASET_PATH = "data/raw/instruction_misuse_dataset.csv"


def predict_risk(text):
    """
    Predicts risk type using rule-based logic.
    Priority order is important.
    """
    if detect_ambiguity(text):
        return "AMBIGUITY"
    if detect_sequence_dependency(text):
        return "SEQUENCE_DEPENDENCY"
    if detect_cognitive_overload(text):
        return "COGNITIVE_OVERLOAD"
    return "LOW_RISK_CLEAR"


def run_pipeline():
    dataset = load_dataset(DATASET_PATH)

    print("\n--- Instruction Misuse Risk Analysis ---\n")

    for idx, item in enumerate(dataset, start=1):
        instruction = item["instruction_text"]
        actual_risk = item["risk_type"]

        cleaned_text = clean_text(instruction)
        predicted_risk = predict_risk(cleaned_text)

        print(f"Instruction {idx}: {instruction}")
        print(f"Actual Risk    : {actual_risk}")
        print(f"Predicted Risk : {predicted_risk}")
        print("-" * 50)


if __name__ == "__main__":
    run_pipeline()
