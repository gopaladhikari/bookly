from pydantic import BaseModel, Field, EmailStr, SecretStr
from typing import Optional, Annotated

ValidUsername = Annotated[str, Field(min_length=3, max_length=20)]

ValidPassword = Annotated[SecretStr, Field(min_length=8)]


# Schemas
class RegisterSchema(BaseModel):
    username: ValidUsername
    email: EmailStr
    password: ValidPassword


class LoginSchema(BaseModel):
    username: ValidUsername
    password: ValidPassword


class ResetPassword(BaseModel):
    new_password: ValidPassword
    confirm_new_password: ValidPassword
