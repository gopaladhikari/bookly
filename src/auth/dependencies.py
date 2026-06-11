from fastapi.security import HTTPBearer
from fastapi import Request, status
from .utils import decode_jwt_token
from fastapi.exceptions import HTTPException
from .schema import TokenPayload


class AccessTokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> TokenPayload | None:  # type: ignore[override]

        token = request.cookies.get("access_token")

        if not token:
            try:
                credentials = await super().__call__(request)
                if credentials:
                    token = credentials.credentials
            except HTTPException:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated. Please log in.",
                )

        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated. Please log in.",
            )

        try:
            decoded_jwt = decode_jwt_token(token)

            if decoded_jwt.refresh:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Please provide a valid access token",
                )

            return decoded_jwt

        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


class RefreshTokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> TokenPayload | None:  # type: ignore[override]

        token = request.cookies.get("refresh_token")

        if not token:
            try:
                credentials = await super().__call__(request)
                if credentials:
                    token = credentials.credentials
            except HTTPException:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated. Please log in.",
                )

        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated. Please log in.",
            )

        try:
            decoded_jwt = decode_jwt_token(token)

            if not decoded_jwt.refresh:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Please provide a valid refresh token",
                )

            return decoded_jwt

        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
