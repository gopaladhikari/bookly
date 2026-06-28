from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from src.books.dto import BookDto
from typing import List


class UserDto(BaseModel):
    message: str
    id: UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: str
    email: str
    is_verified: bool
    created_at: datetime


class UserBookDto(UserDto):
    books = List[BookDto]


class UserLoginDto(BaseModel):
    message: str
    user: UserDto
    access_token: str
    refresh_token: str
