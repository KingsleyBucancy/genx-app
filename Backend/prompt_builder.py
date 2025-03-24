import re
def build_prompt(app_idea: str) -> str:
    return f"""You are an expert frontend developer.

 Write a complete and clean React component using JSX and Tailwind CSS based on the following idea:

"{app_idea}"

✅ Requirements:
- Return a full working React code snippet as a single file.
- Use functional components and React best practices.
- Use Tailwind CSS for styling.
- Do not include explanations — only return the code.
- The app should render a basic usable UI.



Output only the code. No Markdown. No commentary."""


