"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

# Portfolio-specific schemas

class Project(BaseModel):
    """
    Portfolio projects collection
    Collection name: "project"
    """
    title: str = Field(..., description="Project title")
    description: str = Field(..., description="Short project summary")
    tags: List[str] = Field(default_factory=list, description="Tech stack tags")
    github_url: Optional[HttpUrl] = Field(None, description="GitHub repository URL")
    live_url: Optional[HttpUrl] = Field(None, description="Live demo URL")
    image_url: Optional[str] = Field(None, description="Thumbnail image URL")

class Message(BaseModel):
    """
    Contact messages collection
    Collection name: "message"
    """
    name: str = Field(..., description="Sender name")
    email: str = Field(..., description="Sender email")
    subject: Optional[str] = Field(None, description="Subject line")
    message: str = Field(..., description="Message body")

# Example schemas (kept for reference but not used by the portfolio directly)
class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")
