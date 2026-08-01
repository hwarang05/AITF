"""
AITF Backend

FastAPI 애플리케이션의 시작점(Entry Point)

현재 기능
- 서버 실행
- Swagger 제공
- 서버 상태 확인 API

향후 추가 예정
- API Router 등록
- Middleware 등록
- Exception Handler 등록
- Logging 설정
"""

from fastapi import FastAPI

from app.api.router import api_v1
from app.core.config import settings
from app.core.database import engine
from app.core.exception_handler import register_exception_handlers
from app.core.response import response
from app.models.base import Base

# ---------------------------------------------------------------------
# Model Import
#
# Base.metadata.create_all()이 테이블을 생성할 수 있도록
# 모든 ORM Model을 import한다.
# ---------------------------------------------------------------------

from app.models.user import User
from app.models.conversation import Conversation
from app.models.message import Message

from app.schemas.common import ApiResponse

# -----------------------------------------------------------------------------
# FastAPI 애플리케이션 생성
# -----------------------------------------------------------------------------

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

# -----------------------------------------------------------------------------
# Database
# -----------------------------------------------------------------------------

Base.metadata.create_all(bind=engine)

# -----------------------------------------------------------------------------
# Exception Handler 등록
# -----------------------------------------------------------------------------

register_exception_handlers(app)

# -----------------------------------------------------------------------------
# API Router 등록
# -----------------------------------------------------------------------------

app.include_router(api_v1)

# -----------------------------------------------------------------------------
# Root API
# -----------------------------------------------------------------------------

@app.get(
    "/",
    tags=["System"],
    response_model=ApiResponse,
)
async def root():
    """
    서버 상태 확인 API
    """

    return response.success(
        message="AITF Backend Running",
        data={
            "version": settings.APP_VERSION,
        },
    )