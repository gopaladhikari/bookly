from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class UserRegisterDto(BaseModel):
    message: str
    id: UUID
    first_name: str
    last_name: str
    username: str
    email: str
    is_verified: bool
    created_at: datetime


class UserLoginDto(BaseModel):
    message: str
    user: UserRegisterDto
    access_token: str
    refresh_token: str
