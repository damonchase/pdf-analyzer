import pymupdf
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

chat_history = []

def main():
    doc = pymupdf.open("US Intern Offer Letter 2025-11-26.pdf")

    text = ""
    for page in doc:
        text = text + page.get_text()

    prompt = "Your job is to read pdf documents and give a super brief summary of them with just the important parts. Trying to make it as minimal as possible"

    chat_history.append(
        types.Content(
            role="user",
            parts=[types.Part(text=prompt), types.Part(text=text)]
        )
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=chat_history
    )

    print(response.text)

if __name__ == "__main__":
    main()
