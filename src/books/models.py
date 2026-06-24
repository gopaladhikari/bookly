from sqlmodel import Field, SQLModel, func, Relationship
from datetime import datetime, timezone, date
from uuid import uuid4, UUID
from typing import Optional
from src.auth.model import User


def now() -> datetime:
    return datetime.now(timezone.utc)


class Book(SQLModel, table=True):
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

    created_at: datetime = Field(
        default_factory=now, sa_column_kwargs={"server_default": "CURRENT_TIMESTAMP"}
    )

    updated_at: datetime = Field(
        default_factory=now,
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now(),
        },
    )

    user: Optional[User] = Relationship(back_populates="books")

    def __repr__(self):
        return f"<Book {self.title}>"
