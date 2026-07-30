"""
API Router 관리

모든 API Router를 이곳에서 등록한다.

향후 추가 예정
- Chat API
- Auth API
- Document API
- Admin API
"""

from fastapi import APIRouter

from app.api.v1.system import router as system_router
from app.core.config import settings

# -----------------------------------------------------------------------------
# Version 1 Router
# -----------------------------------------------------------------------------

api_v1 = APIRouter(
    prefix=settings.API_PREFIX
)

api_v1.include_router(system_router)