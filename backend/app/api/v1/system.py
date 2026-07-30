"""
System API

서버의 상태를 확인하거나,
운영에 필요한 기본 기능을 제공하는 API.

현재는 Ping 기능만 제공한다.
"""

from fastapi import APIRouter

from app.core.response import response
from app.schemas.common import ApiResponse

# -----------------------------------------------------------------------------
# Router 생성
# -----------------------------------------------------------------------------

router = APIRouter(
    prefix="/system",
    tags=["System"],
)


@router.get(
    "/ping",
    response_model=ApiResponse,
)
async def ping():
    """
    서버 정상 동작 확인
    """

    return response.success(
        message="Pong!",
        data={
            "server": "AITF",
            "version": "0.1.0",
        },
    )