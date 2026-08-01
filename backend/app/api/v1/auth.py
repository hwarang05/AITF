"""
Authentication API

사용자 로그인 API를 제공한다.
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.response import response
from app.core.security import JWTService
from app.dependencies.auth import get_current_active_user
from app.models.user import User
from app.schemas.auth import LoginRequest
from app.schemas.auth import LoginResponse
from app.services.auth_service import AuthService

# -----------------------------------------------------------------------------
# Router
# -----------------------------------------------------------------------------

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

# -----------------------------------------------------------------------------
# Login
# -----------------------------------------------------------------------------

@router.post(
    "/login",
    response_model=LoginResponse,
)
async def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    """
    사용자 로그인
    """

    auth_service = AuthService(db)

    user = await auth_service.login(
        username=request.username,
        password=request.password,
    )

    if user is None:
        return LoginResponse(
            success=False,
            message="Login Failed",
        )

    access_token = JWTService.create_access_token(
        {
            "sub": user.nas_username,
            "user_id": user.id,
        }
    )

    return LoginResponse(
        success=True,
        message="Login Success",
        access_token=access_token,
        token_type="bearer",
        expires_in=JWTService.get_access_token_expires_in(),
    )


# -----------------------------------------------------------------------------
# Current User
# -----------------------------------------------------------------------------

@router.get("/me")
async def me(
    current_user: User = Depends(get_current_active_user),
):
    """
    현재 로그인한 사용자 조회
    """

    return response.success(
        message="Current User",
        data={
            "id": current_user.id,
            "nas_username": current_user.nas_username,
            "display_name": current_user.display_name,
            "email": current_user.email,
            "is_active": current_user.is_active,
            "last_login_at": current_user.last_login_at,
        },
    )


# -----------------------------------------------------------------------------
# Logout
# -----------------------------------------------------------------------------

@router.post("/logout")
async def logout():
    """
    로그아웃

    JWT는 Stateless이므로
    클라이언트에서 토큰을 삭제하면 로그아웃된다.
    """

    return response.success(
        message="Logout Success",
    )