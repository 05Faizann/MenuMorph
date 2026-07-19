import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.blueprint import WebsiteBlueprint

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-3.5-flash"


def design_website(restaurant_knowledge):
    prompt = f"""
You are an expert UI/UX designer.

Using the restaurant information below, design a modern restaurant website.

Choose:
- color palette
- typography
- layout
- hero section
- website sections

Return ONLY valid JSON matching the WebsiteBlueprint schema.

Restaurant Knowledge:

{restaurant_knowledge.model_dump_json(indent=2)}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=WebsiteBlueprint,
        ),
    )

    return response.parsed