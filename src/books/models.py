from sqlmodel import Field, SQLModel, Column, func
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime, timezone
from uuid import uuid4, UUID


def now():
    return datetime.now(timezone.utc)


class Book(SQLModel, table=True):
    __tablename__ = "books"  # type: ignore

    id: UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid4
        )
    )
    title: str
    author: str
    description: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str

    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP(timezone=True), default=now, nullable=False)
    )

    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            default=now,
            onupdate=func.now,
            nullable=False,
        )
    )

    def __repr__(self):
        return f"<Book {self.title}>"
