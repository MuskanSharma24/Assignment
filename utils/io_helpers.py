import os
from config import PROMPT_DIR, OUTPUT_DIR

def load_prompt(domain: str) -> str:
    path = os.path.join(PROMPT_DIR, f"{domain}_prompt.txt")
    with open(path, 'r') as f:
        return f.read()

def save_output(domain: str, content: str):
    os.makedirs(os.path.join(OUTPUT_DIR, domain), exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, domain, "generated_code.py")
    with open(file_path, 'w') as f:
        f.write(content)
