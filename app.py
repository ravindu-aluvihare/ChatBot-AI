from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("")
#api_key = os.getenv("OPENAI_API_KEY")


# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# API request
response = client.chat.completions.create(
    model="",  
    #model="gpt-3.5-turbo"
    messages=[{"role": "user", "content": "hello"}],
    max_tokens=50,
    temperature=0
)

# Print response
for choice in response.choices:
   print(choice.message.content)
