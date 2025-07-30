# routes.py
from flask import Blueprint, request, jsonify
from utils.generator import generate_code
from utils.clarifier import clarify_requirements
from utils.io_helpers import load_prompt, save_output

routes = Blueprint('routes', __name__)

@routes.route('/generate', methods=['POST'])
def generate_crm_code():
    data = request.get_json()

    if not data or 'domain' not in data or 'clarifications' not in data:
        return jsonify({'error': 'Missing required fields: domain, clarifications'}), 400

    domain = data['domain'].strip().lower()
    clarifications = data['clarifications'].strip()

    try:
        prompt_template = load_prompt(domain)
        final_prompt = prompt_template + f"\n\nUser Clarifications:\n{clarifications}"

        code_output = generate_code(final_prompt)
        save_output(domain, code_output)

        return jsonify({'message': f'CRM code for {domain} generated successfully.', 'code': code_output})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
