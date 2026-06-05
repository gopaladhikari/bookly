from sqlmodel.ext.asyncio.session import AsyncSession
from .model import User
from uuid import UUID
from .schema import RegisterSchema, LoginSchema


class AuthService:
    async def register_user(self, user: RegisterSchema, session: AsyncSession):
        pass

    async def login_user(self, user: LoginSchema, session: AsyncSession):
        pass
