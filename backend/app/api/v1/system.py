"""
System API

서버의 상태를 확인하거나,
운영에 필요한 기본 기능을 제공하는 API.

현재는 Ping 기능만 제공한다.
"""

from fastapi import APIRouter

# -----------------------------------------------------------------------------
# Router 생성
# -----------------------------------------------------------------------------

router = APIRouter(
    prefix="/system",
    tags=["System"],
)


@router.get("/ping")
async def ping():
    """
    서버 정상 동작 확인

    Returns:
        dict
    """

    return {
        "success": True,
        "message": "Pong!",
    }