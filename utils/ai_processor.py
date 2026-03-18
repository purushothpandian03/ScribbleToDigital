import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Initialize the client with your API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def correct_text(raw_text):
    """
    Send raw OCR text to Gemini for grammar correction and formatting.
    """
    prompt = f"""
    You are an AI assistant that corrects handwritten OCR text.
    Fix spelling, grammar, and reconstruct incomplete words.
    Format the result into clean paragraphs.

    Raw text:
    {raw_text}

    Corrected text:
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # Use the latest model
        contents=prompt
    )
    return response.text.strip()

def extract_todos(raw_text):
    """
    Extract actionable to-do items from the raw text.
    """
    prompt = f"""
    Extract all actionable tasks from the following notes.
    Return them as a bullet list (each starting with - ).

    Notes:
    {raw_text}

    To-Do list:
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()
