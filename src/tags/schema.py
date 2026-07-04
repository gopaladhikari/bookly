from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class TagSchema(BaseModel):
    uid: UUID
    title: str = Field(max_length=20)
    created_at: datetime


class TagCreateModel(BaseModel):
    title: str = Field(max_length=20)
