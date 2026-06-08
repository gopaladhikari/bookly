from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import AuthService
from src.core.database import get_session
from .schema import RegisterSchema, LoginSchema
from .dto import UserRegisterDto, UserLoginDto
from fastapi.responses import JSONResponse

auth_service = AuthService()

auth_router = APIRouter()


@auth_router.post("/login", status_code=status.HTTP_200_OK, response_model=UserLoginDto)
async def login(user: LoginSchema, session: AsyncSession = Depends(get_session)):
    try:
        user_details = await auth_service.login_user(user, session)

        return {
            "message": "User logged in successfully.",
            **user_details,
        }

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@auth_router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserRegisterDto
)
async def register(user: RegisterSchema, session: AsyncSession = Depends(get_session)):
    try:
        new_user = await auth_service.register_user(user, session)

        return {"message": "User registered successfully.", **new_user.model_dump()}

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
