import os, json
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_code_with_ai(code: str) -> dict:
    prompt = f"""
Analyze this Python code for vulnerabilities. Return ONLY JSON:
{{"is_vulnerable": true/false, "cwe_id": "CWE-XXX", "severity": "HIGH", "explanation": "text", "fix": "text"}}
Code:
{code}
"""
    try:
        response = client.models.generate_content(model='gemini-3.8-flash', contents=prompt)
        raw_text = response.text.strip()
        if raw_text.startswith("```json"): raw_text = raw_text[7:]
        if raw_text.startswith("```"): raw_text = raw_text[3:]
        if raw_text.endswith("```"): raw_text = raw_text[:-3]
        result = json.loads(raw_text.strip())
        return result
    except Exception as e:
        return {"is_vulnerable": False, "error": str(e)}