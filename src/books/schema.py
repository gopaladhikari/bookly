from pydantic import BaseModel
from typing import Optional
from datetime import date


class CreateBookSchema(BaseModel):
    title: str
    author: str
    description: str
    publisher: str
    published_date: date
    page_count: int
    language: str


class UpdateBookSchema(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[date] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
