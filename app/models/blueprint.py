from typing import List
from pydantic import BaseModel


class ColorPalette(BaseModel):
    primary: str
    secondary: str
    accent: str
    background: str
    text: str


class Typography(BaseModel):
    heading_font: str
    body_font: str


class Layout(BaseModel):
    hero: str
    menu: str
    gallery: str
    footer: str


class Hero(BaseModel):
    headline: str
    subheadline: str
    cta: str


class WebsiteBlueprint(BaseModel):
    palette: ColorPalette
    typography: Typography
    layout: Layout
    hero: Hero
    sections: List[str]