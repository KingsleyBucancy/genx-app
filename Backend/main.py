from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os
import logging
from prompt_builder import build_prompt
import re

# Load env variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up logging
logging.basicConfig(level=logging.INFO)

# FastAPI app
app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for input validation
class PromptRequest(BaseModel):
    idea: str

def extract_code(raw: str) -> str:
    # Try to extract from a markdown block if present
    code_blocks = re.findall(r"```(?:jsx|js)?\n([\s\S]+?)```", raw)
    if code_blocks:
        return code_blocks[0].strip()

    # If no code block, return the text without intro lines
    lines = raw.strip().split('\n')
    cleaned_lines = [line for line in lines if not line.lower().startswith("here is") and "```" not in line]


@app.post("/generate_code")
async def generate_code(request: PromptRequest):
    try:
        idea = request.idea.strip()
        logging.info(f"Received idea: {idea}")

        if not idea:
            return {"code": "// No idea provided."}

        prompt = build_prompt(idea)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful expert frontend developer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        raw_code = response.choices[0].message.content
        code = extract_code(raw_code)
        return {"code": code}


    except Exception as e:
        logging.error("Error during code generation:", exc_info=True)
        return {"code": f"// Error: {str(e)}"}
