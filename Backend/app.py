# app.py
from flask import Flask, request, jsonify
import whisper
import os
from werkzeug.utils import secure_filename
import subprocess
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)
CORS(app)  # <- allow cross-origin requests

app.config['UPLOAD_FOLDER'] = 'uploads/'

# Load Whisper model once when app starts
model = whisper.load_model("base")  # options: tiny, base, small, medium, large

@app.route('/transcribe', methods=['POST'])
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded audio
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

        # Convert WebM to WAV using FFmpeg
    wav_path = filepath.replace(".webm", ".wav")
    subprocess.run(["ffmpeg", "-i", filepath, "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", wav_path])


    try:
        # Transcribe using Whisper
        result = model.transcribe(filepath)
        transcript = result['text']
        print(f"📝 Transcribed text: {transcript}")

        return jsonify({"transcript": transcript})

    except Exception as e:
        print(f"❌ Whisper error: {e}")
        return jsonify({"error": "Transcription failed"}), 500

    finally:
        # Clean up file after use
        os.remove(filepath)

if __name__ == "__main__":
    app.run(port=5000, debug=True)