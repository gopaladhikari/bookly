from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


class BookWithId(
    BookCreate,
    BaseModel,
):
    id: UUID
