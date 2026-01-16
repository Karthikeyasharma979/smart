from openai import OpenAI
import os

def summary(text: str, length="medium", format_type="paragraph"):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("open_router"),
    )
    
    length_instruction = "concise" if length == "short" else "detailed" if length == "long" else "moderate length"
    format_instruction = "a bulleted list. Use a new line for each point. Start each point with a '•' character" if "bullet" in format_type.lower() or "point" in format_type.lower() else "paragraph"

    prompt = f"Summarize the following text.\nLength: {length_instruction}.\nFormat: {format_instruction}.\nReturn ONLY the summary content without introductory text.\n\nText:\n{text}"

    completion = client.chat.completions.create(
        model="meta-llama/llama-3.2-3b-instruct:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content