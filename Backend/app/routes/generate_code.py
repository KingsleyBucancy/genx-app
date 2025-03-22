from flask import Blueprint, request, jsonify
from app.services.gpt_service import generate_app_code

codegen_bp = Blueprint('generate_code', __name__)

@codegen_bp.route('/generate-code', methods=['POST'])
def generate_code():
    data = request.get_json()
    idea = data.get("idea", "").strip()

    print("🔁 Received idea:", idea) 

    if not idea:
        return jsonify({"error": "No idea provided"}), 400

    try:
        generated_code = generate_app_code(idea)
        return jsonify({ "code": generated_code })
    except Exception as e:
        print(f"❌ GPT Error: {e}")
        return jsonify({ "error": "Failed to generate code." }), 500
