from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class UserDto(BaseModel):
    message: str
    id: UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: str
    email: str
    is_verified: bool
    created_at: datetime


class UserLoginDto(BaseModel):
    message: str
    user: UserDto
    access_token: str
    refresh_token: str
