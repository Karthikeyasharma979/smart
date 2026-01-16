
from openai import OpenAI
import os
def chat(text, tone, model="meta-llama/llama-3.2-3b-instruct:free"):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("open_router"),  # Replace with your actual key
    )
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"""Rewrite the following text to have a {tone} tone. Keep the meaning but adjust the style. Return ONLY the rewritten text without any introductory or concluding remarks.\n\nOriginal Text:\n{text}"""
            }
        ]
    )
    return completion.choices[0].message.content
