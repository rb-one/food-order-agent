from collections.abc import MutableMapping
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import HTTPException

from app.config import JWT_SECRET

JWT_SECRET = "your_secret_key"  # Replace with environment variable


def create_jwt(data: MutableMapping[str, str]) -> str:
    """Cretes a JWT token with the given data."""
    expiration = datetime.now(timezone.utc) + timedelta(hours=1)
    data.update({"expires_at": expiration.isoformat()})
    return jwt.encode({**data}, JWT_SECRET, algorithm="HS256")


def decode_jwt(token: str):
    """Decodes the given JWT token."""
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
