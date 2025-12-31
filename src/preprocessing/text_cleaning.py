import re

def clean_text(text):
    """
    Cleans input instruction text.
    - Converts to lowercase
    - Removes extra spaces
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def tokenize(text):
    """
    Splits text into tokens (words).
    """
    return text.split()

if __name__ == "__main__":
    sample_text = "Press the reset button while holding the power switch."
    cleaned = clean_text(sample_text)
    tokens = tokenize(cleaned)

    print("Original:", sample_text)
    print("Cleaned :", cleaned)
    print("Tokens  :", tokens)
