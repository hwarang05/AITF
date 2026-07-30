"""
Authentication API

사용자 로그인 API를 제공한다.
"""

from fastapi import APIRouter

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
# Service
# -----------------------------------------------------------------------------

auth_service = AuthService()

# -----------------------------------------------------------------------------
# Login
# -----------------------------------------------------------------------------

@router.post(
    "/login",
    response_model=LoginResponse,
)
async def login(
    request: LoginRequest,
):
    """
    사용자 로그인
    """

    success = await auth_service.login(
        username=request.username,
        password=request.password,
    )

    return LoginResponse(
        success=success,
        message="Login Success" if success else "Login Failed",
    )