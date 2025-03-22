from openai import OpenAI
from flask import current_app

client = OpenAI()

#to clasify the users intent -- code or no code
def classify_intent(idea: str) -> dict:
    prompt = f"""
You are an AI assistant that classifies user app ideas as either intended for code-based development or no-code tools.

Classify this idea: "{idea}"

Respond ONLY in this JSON format:
{{
  "type": "code"  // or "no-code"
}}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You classify user ideas into 'code' or 'no-code'."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        import json
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print("❌ Intent classification failed:", e)
        return {"type": "code"}  # fallback default

def generate_app_code(user_idea: str) -> str:
    #openai.api_key = current_app.config['OPENAI_API_KEY']

    prompt = f"""
    You are an expert React developer.

Your task is to generate complete boilerplate code for an app idea described below using React and TailwindCSS.

App Idea: "{user_idea}"

Please provide:
- A brief summary (as a comment)
- index.html
- App.js
- Any other required components
- Tailwind classes for styling
- Label each code block clearly using '## filename'

ONLY return code. No explanation.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional app developer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
