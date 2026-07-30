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

from app.core.config import settings
from app.api.router import api_v1

# ============================================================
# FastAPI 애플리케이션 생성
# ============================================================

app = FastAPI(
    title=settings.APP_NAME,
    description="AI Technology Framework Backend",
    version="0.1.0",
    debug=settings.DEBUG,
)
app.include_router(api_v1)

# ============================================================
# Root API
# ============================================================


@app.get("/", tags=["System"])


async def root():
    """
    서버 상태 확인 API

    개발 초기에는 서버가 정상적으로 실행되는지
    확인하기 위한 용도이다.

    Returns:
        dict: 서버 상태 정보
    """

    return {
        "status": "success",
        "message": "AITF Backend Running",
        "version": "0.1.0",
    }
