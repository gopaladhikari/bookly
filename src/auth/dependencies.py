from fastapi.security import HTTPBearer
from fastapi import Request, status
from .utils import decode_jwt_token
from fastapi.exceptions import HTTPException
from .schema import TokenPayload


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> TokenPayload | None:  # type: ignore[override]
        credentials = await super().__call__(request)

        if credentials is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        try:
            token = decode_jwt_token(credentials.credentials)

            if token.refresh:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Please provide a valid access token",
                )

            return token

        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
