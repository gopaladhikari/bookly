from sqlmodel import SQLModel, Column, Field, func
from uuid import uuid4, UUID
from datetime import datetime, timezone
import sqlalchemy.dialects.postgresql as pg


def now():
    return datetime.now(timezone.utc)


class User(SQLModel, table=True):
    __tablename__ = "users"  # type: ignore

    id: UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4
        )
    )

    username: str
    email: str
    first_name: str
    last_name: str
    password: str = Field(exclude=True)
    is_verified: bool = False
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
        return f"<User {self.username}>"
