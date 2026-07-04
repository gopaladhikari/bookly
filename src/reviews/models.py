from sqlmodel import Field, Relationship
from src.core.base_model import BaseModel
from datetime import datetime, timezone
from uuid import uuid4, UUID
from typing import Optional, TYPE_CHECKING
from sqlalchemy import UniqueConstraint

if TYPE_CHECKING:
    from src.auth.models import User
    from src.books.models import Book


class Review(BaseModel, table=True):
    __tablename__ = "reviews"  # type: ignore

    __table_args__ = (
        UniqueConstraint("book_id", "user_id", name="unique_review_per_user_book"),
    )

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)

    book_id: UUID = Field(foreign_key="books.id")

    user_id: UUID = Field(foreign_key="users.id")

    rating: int = Field(ge=1, le=5)

    review: Optional[str] = Field(max_length=250)

    book: Optional["Book"] = Relationship(back_populates="reviews")

    user: Optional["User"] = Relationship(back_populates="reviews")

    def __repr__(self):
        return f"<Review {self.review} for {self.book_id}> by {self.user_id}"
