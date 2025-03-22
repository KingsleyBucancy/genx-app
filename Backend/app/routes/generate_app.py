# app/routes/generate_app.py
from flask import Blueprint, request, jsonify
from app.routes.generate_code import generate_app_code  # ensure this is correctly exported
from app.services.gpt_service import classify_intent, generate_nocode_guide

generate_bp = Blueprint('generate_app', __name__)

@generate_bp.route('/generate-app', methods=['POST'])
def generate_app():
    data = request.get_json()
    idea = data.get("idea", "").strip()

    if not idea:
        return jsonify({"error": "No idea provided"}), 400

    try:
        # Step 1: Classify intent (code or no-code)
        intent_result = classify_intent(idea)
        intent = intent_result.get("type", "code")  # fallback default

        # Step 2: Route to appropriate GPT generator
        if intent == "code":
            generated = generate_app_code(idea)
            response = {
                "intent": "code",
                "format": "react",
                "files": generated.get("files", {}),
                "summary": generated.get("summary", "")
            }
        else:
            generated = generate_nocode_guide(idea)
            response = {
                "intent": "no-code",
                "tools": generated.get("tools", []),
                "instructions": generated.get("instructions", []),
                "summary": generated.get("summary", "")
            }

        return jsonify(response)

    except Exception as e:
        print("❌ Error generating app:", e)
        return jsonify({"error": "Failed to generate app."}), 500
