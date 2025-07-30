from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

client = OpenAI(api_key=OPENAI_API_KEY)

def call_gpt(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
    )
    return response.choices[0].message.content.strip()
