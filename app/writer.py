from pathlib import Path
import re

from app.models.generated_website import GeneratedWebsite


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def save_website(
    website: GeneratedWebsite,
    restaurant_name: str,
):
    folder_name = slugify(restaurant_name)

    output_folder = Path("generated_websites") / folder_name
    output_folder.mkdir(parents=True, exist_ok=True)

    # Fix common AI filename mistakes
    website.index_html = (
        website.index_html
        .replace('href="style_css"', 'href="style.css"')
        .replace("href='style_css'", "href='style.css'")
        .replace('src="script_js"', 'src="script.js"')
        .replace("src='script_js'", "src='script.js'")
    )

    (output_folder / "index.html").write_text(
        website.index_html,
        encoding="utf-8",
    )

    (output_folder / "style.css").write_text(
        website.style_css,
        encoding="utf-8",
    )

    (output_folder / "script.js").write_text(
        website.script_js,
        encoding="utf-8",
    )

    print(f"Website saved to: {output_folder.resolve()}")