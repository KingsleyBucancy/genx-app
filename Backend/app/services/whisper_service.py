import whisper
import subprocess
import os

model = whisper.load_model("base")  # preload once

def convert_webm_to_wav(input_path):
    wav_path = input_path.replace(".webm", ".wav")
    subprocess.run([
        "ffmpeg", "-i", input_path,
        "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le",
        wav_path
    ], check=True)
    return wav_path

def transcribe_audio(filepath):
    try:
        # Convert WebM to WAV
        wav_path = convert_webm_to_wav(filepath)

        # Transcribe using Whisper
        result = model.transcribe(wav_path)
        return result['text']

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)
        if os.path.exists(wav_path):
            os.remove(wav_path)
