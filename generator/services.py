import os
import requests
from dotenv import load_dotenv
from requests.exceptions import HTTPError

load_dotenv()
HF_API_TOKEN = os.getenv('HF_API_TOKEN')
HF_MODEL     = os.getenv('HF_MODEL')

API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type":  "application/json"
}

def generate_text(prompt: str, max_new_tokens: int = 200) -> str:
    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            json={
                "inputs": prompt,
                "parameters": {"max_new_tokens": max_new_tokens}
            },
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data[0].get('generated_text', '')
    except HTTPError as err:
        print(f"HuggingFace API HTTPError: {err}")
        return "Извините, в данный момент генерация недоступна."
    except Exception as err:
        print(f"Unexpected error: {err}")
        return "При генерации произошла ошибка."

