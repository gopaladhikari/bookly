from sqlmodel.ext.asyncio.session import AsyncSession
from .model import User
from uuid import UUID
from .schema import RegisterSchema, LoginSchema, ResetPassword
from pydantic import EmailStr
from sqlmodel import select, or_
from .utils import hash_password, verify_password, create_jwt_token


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

        hashed_password = hash_password(plain_password)

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
        statement = select(User).where(User.email == user.email)

        result = await session.exec(statement)

        existing_user = result.first()

        if existing_user is None:
            raise ValueError("Invalid email or password.")

        is_password_correct = verify_password(existing_user.password, user.password)

        if not is_password_correct:
            raise ValueError("Invalid email or password.")

        access_token = create_jwt_token(existing_user.id)

        refresh_token = create_jwt_token(existing_user.id, True)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": existing_user,
        }

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
