from sqlmodel import SQLModel, Field, func
from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime, timezone


def now() -> datetime:
    return datetime.now(timezone.utc)


class User(SQLModel, table=True):
    __tablename__ = "users"  # type: ignore

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)

    username: str = Field(index=True, nullable=False)

    email: str = Field(index=True, nullable=False, unique=True)

    first_name: Optional[str] = Field(default=None)

    last_name: Optional[str] = Field(default=None)

    password: str = Field(exclude=True)

    is_verified: bool = False

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

    def __repr__(self) -> str:
        return f"<User {self.username}>"
