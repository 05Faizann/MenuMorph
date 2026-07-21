import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

from app.models.schemas import RestaurantKnowledge

load_dotenv()

MODEL_NAME = "gemini-3.5-flash"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_menu(image_path: str, prompt: str) -> RestaurantKnowledge:
    image = Image.open(image_path)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=RestaurantKnowledge,
        ),
    )

    return response.parsed