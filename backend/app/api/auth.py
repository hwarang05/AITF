from fastapi import APIRouter

from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

service = AuthService()


@router.post("/login")
async def login(request: LoginRequest):

    success = await service.login(
        username=request.username,
        password=request.password,
    )

    return {
        "success": success,
    }