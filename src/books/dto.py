from pydantic import BaseModel
from uuid import UUID
from datetime import date


class BookDto(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    publisher: str
    published_date: date
    page_count: int
