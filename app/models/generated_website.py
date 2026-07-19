from pydantic import BaseModel


class GeneratedWebsite(BaseModel):
    index_html: str
    style_css: str
    script_js: str