from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from app.services.whisper_service import transcribe_audio

transcribe_bp = Blueprint('transcribe', __name__)

@transcribe_bp.route('/transcribe', methods=['POST'])
def transcribe_audio_route():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save audio file
    filename = secure_filename(file.filename)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        transcript = transcribe_audio(filepath)
        print(f"📝 Transcribed text: {transcript}")
        return jsonify({"transcript": transcript})
    except Exception as e:
        print(f"❌ Whisper error: {e}")
        return jsonify({"error": "Transcription failed"}), 500
