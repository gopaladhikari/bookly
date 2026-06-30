from pydantic import BaseModel, Field
from typing import Optional


class ReviewSchema(BaseModel):
    rating: int = Field(ge=1, le=5)
    review: Optional[str] = Field(max_length=250)
