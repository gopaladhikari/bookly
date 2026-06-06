from sqlmodel import Field, SQLModel, Column, func
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime, timezone, date
from uuid import uuid4, UUID


def now() -> datetime:
    return datetime.now(timezone.utc)


class Book(SQLModel, table=True):
    __tablename__ = "books"  # type: ignore

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)

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

    def __repr__(self):
        return f"<Book {self.title}>"
