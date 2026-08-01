"""
공통 Exception Handler

프로젝트에서 발생하는 예외를
일관된 API 응답 형식으로 변환한다.
"""

import logging

from fastapi import FastAPI
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.exceptions import AppException
from app.schemas.common import ApiResponse

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    """
    프로젝트에서 사용하는 Exception Handler 등록
    """

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException,
    ):
        logger.warning(
            "%s | %s",
            request.url.path,
            exc.message,
        )

        return JSONResponse(
            status_code=exc.status_code,
            content=ApiResponse(
                success=False,
                message=exc.message,
                data=None,
            ).model_dump(),
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        logger.warning(
            "Validation Error | %s | %s",
            request.url.path,
            exc.errors(),
        )

        return JSONResponse(
            status_code=422,
            content=ApiResponse(
                success=False,
                message="요청 데이터가 올바르지 않습니다.",
                data=jsonable_encoder(exc.errors()),
            ).model_dump(),
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger.exception(
            "Unhandled Exception | %s",
            request.url.path,
        )

        return JSONResponse(
            status_code=500,
            content=ApiResponse(
                success=False,
                message="Internal Server Error",
                data=None,
            ).model_dump(),
        )