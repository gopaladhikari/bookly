from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class ReviewDto(BaseModel):
    id: UUID
    book_id: UUID
    user_id: UUID
    rating: int
    review: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
