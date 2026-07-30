"""
공통 API 응답 생성 도우미(Response Factory)

프로젝트의 모든 API는 이 클래스를 통해 응답을 생성한다.

장점
- 응답 형식을 프로젝트 전체에서 통일
- 중복 코드 제거
- 응답 형식 변경 시 한 곳만 수정하면 됨
- API 코드가 간결해짐
"""

from typing import Any

from app.schemas.common import ApiResponse


class ResponseFactory:
    """
    공통 API 응답 생성 클래스

    사용 예시
    ----------
    return response.success(
        message="조회 완료",
        data=result
    )

    return response.fail(
        message="권한이 없습니다."
    )
    """

    def success(
        self,
        message: str = "Success",
        data: Any = None,
    ) -> ApiResponse:
        """
        성공 응답 생성

        Args:
            message: 사용자에게 전달할 메시지
            data: 실제 응답 데이터

        Returns:
            ApiResponse
        """

        return ApiResponse(
            success=True,
            message=message,
            data=data,
        )

    def fail(
        self,
        message: str = "Fail",
        data: Any = None,
    ) -> ApiResponse:
        """
        실패 응답 생성

        Args:
            message: 오류 메시지
            data: 추가 오류 정보

        Returns:
            ApiResponse
        """

        return ApiResponse(
            success=False,
            message=message,
            data=data,
        )


# ----------------------------------------------------------------------
# 프로젝트 전체에서 사용하는 공용 Response 객체
#
# 사용 예시
#
# from app.core.response import response
#
# return response.success(...)
# ----------------------------------------------------------------------

response = ResponseFactory()