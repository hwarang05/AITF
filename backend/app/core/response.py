"""
공통 API 응답 생성 도우미(Response Factory)

프로젝트의 모든 API는 이 클래스를 통해 응답을 생성한다.
"""

from typing import TypeVar

from app.schemas.common import ApiResponse

T = TypeVar("T")


class ResponseFactory:
    """
    공통 API 응답 생성 클래스
    """

    @staticmethod
    def success(
        *,
        message: str = "Success",
        data: T | None = None,
    ) -> ApiResponse[T]:

        return ApiResponse[T](
            success=True,
            message=message,
            data=data,
        )

    @staticmethod
    def fail(
        *,
        message: str = "Fail",
        data: T | None = None,
    ) -> ApiResponse[T]:

        return ApiResponse[T](
            success=False,
            message=message,
            data=data,
        )


response = ResponseFactory()