# openai_handler.py
import os

from dotenv import load_dotenv
from openai import OpenAI
from utils import check_api_key

# Load environment variables
load_dotenv()

check_api_key()

api_key = os.getenv('OPEN_AI_KEY')

if api_key is None:
    raise ValueError("API key not found. Make sure to set OPEN_AI_KEY in your environment.")

client = OpenAI(api_key=api_key)


# openai_handler.py
def compliance_check(content, compliance_policy):
    try:
        prompt = f"Given a compliance policy:\n{compliance_policy}\n\nWebpage content:\n{content}\nCheck for compliance issues and report findings."

        response = client.completions.create(
            engine="gpt-4",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100
        )

        if response:
            return response.choices[0].text.strip()

        return None
    except Exception as e:
        return str(e)
