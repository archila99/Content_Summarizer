import requests
import os
import json

API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyDE9Mg0SAE3wrsGkSUiHsr7GwRuYJrPv5w")
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        models = response.json().get('models', [])
        print(f"Found {len(models)} models.")
        for m in models:
            if 'generateContent' in m.get('supportedGenerationMethods', []):
                print(f"Name: {m['name']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Exception: {e}")
