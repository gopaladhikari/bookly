from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import AuthService
from src.core.database import get_session
from .schema import RegisterSchema, LoginSchema, UserResponseDto

auth_service = AuthService()

auth_router = APIRouter()


@auth_router.post(
    "/login", status_code=status.HTTP_200_OK, response_model=UserResponseDto
)
async def login(user: LoginSchema, session: AsyncSession = Depends(get_session)):
    pass


@auth_router.post(
    "/register", status_code=status.HTTP_200_OK, response_model=UserResponseDto
)
async def register(user: RegisterSchema, session: AsyncSession = Depends(get_session)):
    try:
        new_user = await auth_service.register_user(user, session)

        return new_user

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
