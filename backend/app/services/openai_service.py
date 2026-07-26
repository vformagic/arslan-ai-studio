import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_ai(topic: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Sen profesyonel bir teknoloji içerik editörüsün."
            },
            {
                "role": "user",
                "content": topic
            }
        ]
    )

    return response.choices[0].message.content