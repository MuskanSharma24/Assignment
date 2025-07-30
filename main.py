import os
from dotenv import load_dotenv
from utils.generator import generate_code
from utils.clarifier import clarify_requirements
from utils.io_helpers import save_output, load_prompt
from flask import Flask
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

load_dotenv()

def main():
    print("\n🔧 Welcome to the AI CRM Code Generator!\n")
    domain = input("Enter industry (real_estate, healthcare, ecommerce, education, freelancers): ").strip().lower()

    print("\n💬 Let's clarify your requirements:")
    user_details = clarify_requirements(domain)

    prompt_template = load_prompt(domain)
    final_prompt = prompt_template + f"\n\nUser Clarifications:\n{user_details}"

    print("\n🧠 Generating CRM code using GPT-4...")
    code_output = generate_code(final_prompt)

    save_output(domain, code_output)
    print(f"\n✅ CRM code for '{domain}' saved to outputs/{domain}/")

if __name__ == "__main__":
    main()
