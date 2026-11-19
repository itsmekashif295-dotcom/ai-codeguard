import os

# GitHub Actions ke liye dummy API key
# Taake test fail na ho
os.environ["GEMINI_API_KEY"] = os.environ.get("GEMINI_API_KEY", "dummy_key_for_testing")