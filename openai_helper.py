import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with the API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def get_openai_response(text, pdf_text):
    try:
        # Create the chat completion request
        print("User Input:", text)
        print("PDF Content:", pdf_text)  # Optional: for debugging

        # Combine the user's input and PDF content for context
        messages = [
            {"role": "system", "content": "You are a helpful assistant for answering questions about the PDF."},
            {"role": "user", "content": pdf_text},  # Providing the PDF content
            {"role": "user", "content": text}  # Providing the user question or request
        ]

        response = client.chat.completions.create(
            model="gpt-4",  # Use "gpt-4" or "gpt-4o mini" based on your access
            messages=messages,
            max_tokens=100,  # Adjust as necessary
            temperature=0.7  # Adjust to control response creativity
        )
        
        # Extract the content of the response
        return response.choices[0].message.content  # Corrected access method
    except Exception as e:
        return f"Error: {str(e)}"
