from typing import List, Optional
from pydantic import BaseModel


# ---------- Restaurant ----------

class Restaurant(BaseModel):
    name: Optional[str] = None
    cuisine: Optional[str] = None
    description: Optional[str] = None
    tagline: Optional[str] = None


# ---------- Branding ----------

class Branding(BaseModel):
    mood: Optional[str] = None
    style: Optional[str] = None
    tone: Optional[str] = None
    target_audience: Optional[str] = None
    dining_type: Optional[str] = None
    price_range: Optional[str] = None


# ---------- Design ----------

class Design(BaseModel):
    primary_colors: List[str] = []
    secondary_colors: List[str] = []
    typography: Optional[str] = None
    logo_style: Optional[str] = None
    illustration_style: Optional[str] = None


# ---------- Business ----------

class Business(BaseModel):
    signature_dishes: List[str] = []
    specialties: List[str] = []
    dietary_options: List[str] = []


# ---------- Menu ----------

class MenuItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    vegetarian: bool = False
    vegan: bool = False
    spicy: bool = False
    category: Optional[str] = None


class MenuCategory(BaseModel):
    name: str
    items: List[MenuItem]


# ---------- Website Content ----------

class WebsiteContent(BaseModel):
    hero_title: Optional[str] = None
    hero_subtitle: Optional[str] = None
    about: Optional[str] = None


# ---------- SEO ----------

class SEO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    keywords: List[str] = []


# ---------- Master ----------

class RestaurantKnowledge(BaseModel):
    restaurant: Restaurant
    branding: Branding
    design: Design
    business: Business
    content: WebsiteContent
    seo: SEO
    menu: List[MenuCategory]