import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    UPLOAD_FOLDER = 'uploads/'
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
