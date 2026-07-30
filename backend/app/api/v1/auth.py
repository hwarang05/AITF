"""
Authentication API

사용자 로그인 API를 제공한다.
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
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

    return LoginResponse(
        success=user is not None,
        message="Login Success" if user else "Login Failed",
    )