from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from the .env file in this case for your OpenAI API key
load_dotenv()

# Access the OpenAI API key from the environment variable
open_ai_key = os.getenv('OPEN_AI_KEY')
os.environ["OPENAI_API_KEY"] = open_ai_key

client = OpenAI()

# Create a completion with the OpenAI API client using the GPT-4 model and the prompt requested by the user
prompt=input("Enter the prompt (exit to quit): ")
while prompt.lower != "exit":
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        print(completion.choices[0].message)
        prompt=input("Enter the prompt (exit to quit): ")
    except Exception as e:
        print(e)
