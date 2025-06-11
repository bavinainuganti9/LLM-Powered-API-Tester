import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tests(endpoints):
    combined = "\n".join([
        f"{ep['method']} {ep['path']} - {ep['summary']}" for ep in endpoints
    ])

    prompt = f"""
You are an expert API engineer. Generate Python test cases using `requests` for the following endpoints:

{combined}

Include headers, sample payloads, and assert status codes.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{ "role": "user", "content": prompt }],
        temperature=0.5,
    )
    return response.choices[0].message.content
