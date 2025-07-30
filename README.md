AI Prompt Generator - Assignment Project

 Overview

This project is a lightweight, modular AI-powered CRM code generator designed to support industries such as real estate, e-commerce, education, healthcare, and freelancing. The application uses OpenAI’s GPT model to dynamically generate CRM boilerplate code based on industry-specific prompt templates.

The overall approach focuses on modularity, environment-based configuration, and containerized deployment. The goal was to make it intuitive, developer-friendly, and extendable.

---

 Approach

1. Organized the project with clear separation of concerns under the `app/` directory.
2. Created modular utility scripts for prompt I/O, prompt clarification, GPT-based generation, and routing.
3. Prompts for different domains are saved in `.txt` files under `prompts/`.
4. API keys and model configs are securely handled using environment variables via `dotenv`.
5. GPT-4 or GPT-3.5 is used via OpenAI’s ChatCompletion API to generate meaningful code outputs.
6. Git is used for version control, and Docker ensures environment-independent deployment.

---

 Project Structure

```
ASSIGNMENT/
├── .env                       Environment variables (not committed)
├── .gitignore                Ignore virtual env, env files, etc.
├── Dockerfile                Docker config for deployment
├── README.md                 Project documentation
├── requirements.txt          Python dependencies
├── venv/                     Virtual environment (ignored in git)
├── outputs/                  Stores generated outputs per domain
└── app/
    ├── main.py               CLI entry point to run the app
    ├── config.py             API keys, model name, temperature
    ├── model.py              GPT call logic
    ├── routes.py             Flask-based API routes
    ├── prompts/              .txt templates for each domain
    │   ├── real_estate_prompt.txt
    │   ├── education_prompt.txt
    │   └── ...
    └── utils/
        ├── io_helpers.py     Load/save prompts and outputs
        ├── generator.py      Calls `model.py` to generate content
        └── clarifier.py      Refines user inputs into better prompts
```

---

 How to Run (Locally)

1. Create and activate virtual environment (optional):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key in `.env`:

   ```
   OPENAI_API_KEY=your-key-here
   ```

4. Run the script:

   ```bash
   python app/main.py
   ```

5. Follow the CLI prompts to generate CRM code.
   The generated output is saved in the `outputs/` directory.

---

 Deployment via Docker

1. Build the Docker image:

   ```bash
   docker build -t prompt-generator .
   ```

2. Run the container:

   ```bash
   docker run -p 5000:5000 prompt-generator
   ```
