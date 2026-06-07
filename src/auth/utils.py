from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from src.core.config import Config
import jwt
from typing import Optional
import logging
from uuid import UUID, uuid4

passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return passwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return passwd_context.verify(plain_password, hashed_password)


def create_jwt_token(data: dict, is_refresh_token: bool = False) -> str:

    now = datetime.now(timezone.utc)

    expiry_minutes = 30 if not is_refresh_token else 43200

    expiry_time = now + timedelta(minutes=expiry_minutes)

    payload = {
        "exp": int(expiry_time.timestamp()),
        "iat": int(now.timestamp()),
        "sub": data.get("user_id") or data,
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
        logging.exception("Expired signature error")
        return None

    except jwt.InvalidTokenError:
        logging.exception("Invalid token error")
        return None
