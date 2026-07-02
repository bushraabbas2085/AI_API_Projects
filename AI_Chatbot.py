from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Read the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("============================================")
print("==========WELCOME HERE, LET'S TALK==========")
print("============================================")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Jarvis: Goodbye! Shutting down...")
        break

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "You are a helpful and funny AI assistant named Jarvis"
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("Jarvis:", response.output[0].content[0].text)