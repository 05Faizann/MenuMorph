from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import shutil
from uuid import uuid4
from fastapi.staticfiles import StaticFiles

from app.ai.gemini import analyze_menu
from app.ai.designer import design_website
from app.ai.generator import generate_website
from app.writer import save_website

from app.prompts.prompts import MENU_JSON_PROMPT
from app.models.schemas import RestaurantKnowledge

app = FastAPI()

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

GENERATED_FOLDER = Path("generated_websites")
GENERATED_FOLDER.mkdir(exist_ok=True)

app.mount(
    "/generated",
    StaticFiles(directory=GENERATED_FOLDER),
    name="generated",
)


@app.get("/")
def home():
    return {
        "message": "MenuMorph API is running!"
    }


@app.post("/upload")
async def upload_menu(file: UploadFile = File(...)):
    file_path = UPLOAD_FOLDER / f"{uuid4()}_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # AI #1
    restaurant_knowledge = analyze_menu(
        str(file_path),
        MENU_JSON_PROMPT
    )

    # AI #2
    website_blueprint = design_website(
        restaurant_knowledge
    )

    # AI #3
    generated_website = generate_website(
        restaurant_knowledge,
        website_blueprint
    )

    # Save website files
    folder_name = save_website(
        generated_website,
        restaurant_knowledge.restaurant.name,
    )

    return {
        "message": "Website generated successfully!",
        "website_url": f"/generated/{folder_name}/index.html",
        "restaurant": restaurant_knowledge,
        "blueprint": website_blueprint,
    }