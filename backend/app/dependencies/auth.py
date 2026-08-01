"""
Authentication Dependency

JWT 인증을 수행하고
현재 로그인한 사용자를 반환한다.
"""

from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import JWTService
from app.core.security import oauth2_scheme
from app.models.user import User
from app.services.user_service import UserService


# -----------------------------------------------------------------------------
# Current User
# -----------------------------------------------------------------------------
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """
    JWT 인증

    Access Token을 검증하고
    현재 로그인한 사용자를 반환한다.
    """

    payload = JWTService.verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid access token",
        )

    user_id = payload.get("user_id")

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid access token",
        )

    user_service = UserService(db)

    user = user_service.get_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user


# -----------------------------------------------------------------------------
# Current Active User
# -----------------------------------------------------------------------------
async def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    활성 사용자 확인
    """

    if not current_user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Inactive user",
        )

    return current_user