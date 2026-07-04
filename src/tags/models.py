from sqlmodel import Field, Relationship, SQLModel
from src.core.base_model import BaseModel
from uuid import UUID, uuid4
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.books.models import Book


class BookTag(SQLModel, table=True):
    __tablename__ = "book_tag"  # type: ignore

    book_id: UUID = Field(default=None, foreign_key="books.id", primary_key=True)
    tag_id: UUID = Field(default=None, foreign_key="tags.id", primary_key=True)


class Tag(BaseModel, table=True):
    __tablename__ = "tags"  # type: ignore

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    title: str = Field(nullable=False, max_length=20)

    books: List["Book"] = Relationship(
        link_model=BookTag,
        back_populates="tags",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    def __repr__(self) -> str:
        return f"<Tag {self.title}>"
