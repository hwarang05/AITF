"""
JWT Security

AITF JWT 인증을 담당한다.

- Access Token 생성
- Access Token 검증
- OAuth2 Bearer Scheme
"""

from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Any

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from jose import jwt

from app.core.config import settings

# -----------------------------------------------------------------------------
# Timezone
# -----------------------------------------------------------------------------

KST = timezone(timedelta(hours=9))

# -----------------------------------------------------------------------------
# OAuth2
# -----------------------------------------------------------------------------

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/token",
)

# -----------------------------------------------------------------------------
# JWT Service
# -----------------------------------------------------------------------------


class JWTService:
    """
    JWT 생성 및 검증
    """

    @staticmethod
    def create_access_token(data: dict[str, Any]) -> str:
        """
        Access Token 생성
        """

        payload = data.copy()

        expire = datetime.now(KST) + timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
        )

        now = datetime.now(KST)

        payload["iat"] = now
        payload["exp"] = expire

        return jwt.encode(
            payload,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM,
        )

    @staticmethod
    def get_access_token_expires_in() -> int:
        """
        Access Token 만료 시간(초)
        """

        return settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60

    @staticmethod
    def verify_token(token: str) -> dict[str, Any] | None:
        """
        JWT 검증

        성공 시 Payload 반환
        실패 시 None 반환
        """

        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=[settings.JWT_ALGORITHM],
            )

            return payload

        except JWTError:
            return None