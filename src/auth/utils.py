from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from src.core.config import Config
import jwt
from typing import Optional
import logging
from uuid import UUID, uuid4
from uuid import UUID

passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return passwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:

    return passwd_context.verify(plain_password, str(hashed_password))


def create_jwt_token(user_id: UUID, is_refresh_token: bool = False) -> str:

    now = datetime.now(timezone.utc)

    expiry_minutes = 43200 if is_refresh_token else 30

    expiry_time = now + timedelta(minutes=expiry_minutes)

    payload = {
        "exp": int(expiry_time.timestamp()),
        "iat": int(now.timestamp()),
        "sub": str(user_id),
        "jti": str(uuid4()),
        "refresh": is_refresh_token,
    }

    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRET,
        algorithm="HS256",
        headers={"typ": "JWT"},
    )

    return token


def decode_jwt_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(
            jwt=token,
            key=Config.JWT_SECRET,
            algorithms=["HS256"],
        )

        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Jwt token is expired")

    except jwt.InvalidTokenError:
        raise ValueError("Jwt token is invalid.")
