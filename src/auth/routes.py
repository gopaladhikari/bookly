from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import AuthService
from src.core.database import get_session
from .schema import RegisterSchema, LoginSchema, TokenPayload
from .dto import UserDto, UserLoginDto
from .dependencies import AccessTokenBearer

auth_service = AuthService()

auth_router = APIRouter()

access_token_bearer = AccessTokenBearer()


@auth_router.post("/login", status_code=status.HTTP_200_OK, response_model=UserLoginDto)
async def login(
    user: LoginSchema, response: Response, session: AsyncSession = Depends(get_session)
):
    try:
        user_details = await auth_service.login_user(user, session)

        response.set_cookie(
            key="access_token",
            value=user_details["access_token"],
            httponly=True,
            max_age=30 * 60,
            samesite="lax",
            secure=True,
        )

        response.set_cookie(
            key="refresh_token",
            value=user_details["refresh_token"],
            httponly=True,
            max_age=30 * 24 * 60 * 60,
            samesite="lax",
            secure=True,
        )

        return {
            "message": "User logged in successfully.",
            **user_details,
        }

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@auth_router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserDto
)
async def register(user: RegisterSchema, session: AsyncSession = Depends(get_session)):
    try:
        new_user = await auth_service.register_user(user, session)

        return {"message": "User registered successfully.", **new_user.model_dump()}

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@auth_router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    response_model=UserDto,
)
async def get_current_user(
    session: AsyncSession = Depends(get_session),
    token_details: TokenPayload = Depends(access_token_bearer),
):
    try:
        user = await auth_service.get_current_user(token_details.sub, session)

        return {"message": "User retrieved successfully.", **user.model_dump()}

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


# Refresh Access Token
@auth_router.post(
    "/refresh-access-token",
    status_code=status.HTTP_200_OK,
    response_model=UserLoginDto,
)
async def refresh_access_token(
    response: Response,
    token_details: TokenPayload = Depends(access_token_bearer),
    session: AsyncSession = Depends(get_session),
):
    try:
        user_details = await auth_service.refreshAccessToken(token_details.sub, session)

        response.set_cookie(
            key="access_token",
            value=user_details["access_token"],
            httponly=True,
            max_age=30 * 60,
            samesite="lax",
            secure=True,
        )

        response.set_cookie(
            key="refresh_token",
            value=user_details["refresh_token"],
            httponly=True,
            max_age=30 * 24 * 60 * 60,
            samesite="lax",
            secure=True,
        )

        return {
            "message": "Access token refreshed successfully.",
            **user_details,
        }

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
