from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_study_material(text):

    prompt = f"""
You are an educational assistant.

Analyze the following study material.

Return:

1. Short Summary

2. Key Concepts

3. Revision Notes

4. 5 Important Viva Questions

5. 5 MCQs with answers

Text:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content