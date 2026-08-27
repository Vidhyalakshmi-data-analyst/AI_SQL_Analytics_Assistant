import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_gemini_client():
    """
    Create and return a Gemini client.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found.")

    return genai.Client(api_key=api_key)


def get_model_name():
    """
    Return the configured Gemini model.
    """

    return os.getenv(
        "GEMINI_MODEL", "gemini-3.5-flash")
