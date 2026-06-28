from sqlmodel import SQLModel, Field, Relationship, func
from datetime import datetime, timezone
from uuid import uuid4, UUID
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.auth.models import User
    from src.books.models import Book


def now() -> datetime:
    return datetime.now(timezone.utc)


class Review(SQLModel, table=True):
    __tablename__ = "reviews"  # type: ignore

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)

    book_id: UUID = Field(foreign_key="books.id")

    user_id: UUID = Field(foreign_key="users.id")

    rating: Optional[int] = Field(ge=1, le=5)

    review: Optional[str] = Field(max_length=250)

    created_at: datetime = Field(
        default_factory=now, sa_column_kwargs={"server_default": func.now()}
    )

    updated_at: datetime = Field(
        default_factory=now,
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()},
    )

    book: Optional["Book"] = Relationship(back_populates="reviews")

    user: Optional["User"] = Relationship(back_populates="reviews")

    def __repr__(self):
        return f"<Review {self.review} for {self.book_id}> by {self.user_id}"
