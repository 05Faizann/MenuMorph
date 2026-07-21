import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.models.generated_website import GeneratedWebsite
from app.prompts.prompts import WEBSITE_GENERATOR_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"


def generate_website(restaurant_knowledge, website_blueprint):

    prompt = f"""
{WEBSITE_GENERATOR_PROMPT}

Restaurant Knowledge:

{restaurant_knowledge.model_dump_json(indent=2)}

Website Blueprint:

{website_blueprint.model_dump_json(indent=2)}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=GeneratedWebsite,
        ),
    )

    return response.parsed