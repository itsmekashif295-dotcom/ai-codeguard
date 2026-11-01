import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=8000) # 8 seconds timeout
)

def analyze_code_with_ai(code: str) -> dict:
    # Prompt ko aur behtar banaya gaya hai (chota aur direct)
    prompt = f"""
You are an expert security scanner.
Analyze this code for ONE main vulnerability.
Return ONLY a JSON object with no extra text, markdown, or code blocks.
Format:
{{
  "is_vulnerable": true/false,
  "cwe_id": "CWE-XXX" or null,
  "severity": "HIGH/MEDIUM/LOW/NONE",
  "explanation": "One line explanation",
  "fix": "One line fix"
}}

Code:
{code}
"""
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt
        )
        
        raw_text = response.text.strip()
        
        # Agar AI ne markdown laga diya ho toh usko saaf karein
        if raw_text.startswith("```json"): raw_text = raw_text[7:]
        if raw_text.startswith("```"): raw_text = raw_text[3:]
        if raw_text.endswith("```"): raw_text = raw_text[:-3]
        
        result = json.loads(raw_text.strip())
        return result
    
    except json.JSONDecodeError:
        return {
            "is_vulnerable": False, 
            "error": "AI returned an invalid response. Please try again."
        }
    except Exception as e:
        # Agar Timeout ho jaye
        if "DEADLINE_EXCEEDED" in str(e) or "504" in str(e):
            return {
                "is_vulnerable": False, 
                "error": "AI server is too slow right now. Skipping AI analysis."
            }
        # Agar API key galat ho
        elif "API_KEY_INVALID" in str(e):
            return {
                "is_vulnerable": False, 
                "error": "Invalid API key. Please check your .env file."
            }
        else:
            return {
                "is_vulnerable": False, 
                "error": f"AI connection error: {str(e)[:50]}"
            }