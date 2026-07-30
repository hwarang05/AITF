from fastapi import APIRouter

from app.schemas.auth import LoginRequest
from app.schemas.auth import LoginResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=LoginResponse,
)
async def login(
    request: LoginRequest,
):
    return LoginResponse(
        success=True,
        message="Login Success",
    )