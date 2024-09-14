from flask import Blueprint, request, jsonify
from core.resume_generator import generate_resume
import os

api_blueprint = Blueprint('api', __name__)
UPLOAD_FOLDER = 'uploads'

@api_blueprint.route('/generate_resume', methods=['POST'])
def generate_resume_route():
    open_ai_key = request.form.get('open_ai_key')
    pdf_file = request.files.get('pdf_file')
    
    if not open_ai_key or not pdf_file:
        return jsonify({"error": "Missing OpenAI key or PDF file"}), 400
    
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Save the PDF file to a temporary location
    pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
    pdf_file.save(pdf_path)
    
    # Generate the resume using the core logic
    result = generate_resume(open_ai_key, pdf_path)

    # Clean up the saved file after processing
    os.remove(pdf_path)
    
    return jsonify(result)
