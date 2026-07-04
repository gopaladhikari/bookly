from datetime import datetime, timezone
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import func


def now() -> datetime:
    return datetime.now(timezone.utc)


class BaseModel(SQLModel):
    created_at: Optional[datetime] = Field(
        default_factory=now,
        sa_column_kwargs={
            "server_default": func.now(),
        },
    )

    updated_at: Optional[datetime] = Field(
        default_factory=now,
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now(),
        },
    )
