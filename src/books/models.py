from sqlmodel import Field, Relationship
from src.core.base_model import BaseModel
from datetime import datetime, timezone, date
from uuid import uuid4, UUID
from typing import TYPE_CHECKING, Optional, List
from src.tags.models import BookTag

if TYPE_CHECKING:
    from src.auth.models import User
    from src.reviews.models import Review
    from src.tags.models import Tag


class Book(BaseModel, table=True):
    __tablename__ = "books"  # type: ignore

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)

    user_id: UUID = Field(foreign_key="users.id")

    title: str

    author: str

    description: str

    publisher: str

    published_date: date

    page_count: int

    language: str = Field(default="English", max_length=10)

    user: Optional["User"] = Relationship(back_populates="books")

    reviews: List["Review"] = Relationship(back_populates="book")

    tags: List["Tag"] = Relationship(
        back_populates="books",
        link_model=BookTag,
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    def __repr__(self):
        return f"<Book {self.title}>"
