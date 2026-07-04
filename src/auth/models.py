from sqlmodel import Field, Relationship
from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime, timezone
from .schema import Role
from typing import Optional, List, TYPE_CHECKING
from src.core.base_model import BaseModel
from sqlalchemy import text

if TYPE_CHECKING:
    from src.books.models import Book
    from src.reviews.models import Review


class User(BaseModel, table=True):
    __tablename__ = "users"  # type: ignore

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)

    username: str = Field(index=True, nullable=False)

    email: str = Field(index=True, nullable=False, unique=True)

    first_name: Optional[str] = Field(default=None)

    last_name: Optional[str] = Field(default=None)

    role: Role = Field(
        default=Role.USER,
        sa_column_kwargs={"server_default": text(f"'{Role.USER.value}'")},
    )

    password: str = Field(exclude=True)

    is_verified: bool = False

    books: List["Book"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )

    reviews: List["Review"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )

    def __repr__(self) -> str:
        return f"<User {self.username}>"
