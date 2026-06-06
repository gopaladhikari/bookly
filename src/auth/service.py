from sqlmodel.ext.asyncio.session import AsyncSession
from .model import User
from uuid import UUID
from .schema import RegisterSchema, LoginSchema, ResetPassword
from pydantic import EmailStr
from sqlmodel import select, or_
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    async def register_user(self, user: RegisterSchema, session: AsyncSession):
        # Check if user already exists
        statement = select(User).where(
            or_(User.email == user.email, User.username == user.username)
        )

        result = await session.exec(statement)

        existing_user = result.first()

        if existing_user:
            if existing_user.email == user.email:
                raise ValueError("A user with this email already exists.")

            raise ValueError("This username is already taken.")

        # Create a new user
        plain_password = user.password.get_secret_value()

        hashed_password = pwd_context.hash(plain_password)

        new_user = User(
            username=user.username,
            email=user.email,
            password=hashed_password,
        )

        session.add(new_user)

        await session.commit()

        await session.refresh(new_user)

        return new_user

    async def login_user(self, user: LoginSchema, session: AsyncSession):
        pass

    async def verify_email(
        self,
        email: EmailStr,
    ):
        pass

    async def get_current_user(self, email: EmailStr, session: AsyncSession):
        statement = select(User).where(User.email == email)

        result = await session.exec(statement)

        user = result.first()

        if user is None:
            return None

        return user

    async def forget_password(self, email: EmailStr):
        pass

    async def reset_password(self, jwt_token: str, passwords: ResetPassword):
        pass

    async def refreshAccessToken(self, access_token: str):
        pass
