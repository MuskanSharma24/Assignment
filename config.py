# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4"
TEMPERATURE = 0.3

# Add these paths (you can customize them)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_DIR = os.path.join(os.path.dirname(__file__), 'prompts')
OUTPUT_DIR = os.path.join(BASE_DIR, "../outputs")
