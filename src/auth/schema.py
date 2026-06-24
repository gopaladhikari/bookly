from pydantic import BaseModel, Field, EmailStr, SecretStr
from typing import Annotated
from enum import Enum
from uuid import UUID

ValidUsername = Annotated[str, Field(min_length=3, max_length=20)]

ValidPassword = Annotated[SecretStr, Field(min_length=8)]


# Schemas
class RegisterSchema(BaseModel):
    username: ValidUsername
    email: EmailStr
    password: ValidPassword


class LoginSchema(BaseModel):
    email: EmailStr
    password: ValidPassword


class ResetPassword(BaseModel):
    new_password: ValidPassword
    confirm_new_password: ValidPassword


class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"


class TokenPayload(BaseModel):
    exp: int
    iat: int
    sub: UUID
    jti: str
    role: Role
    refresh: bool
