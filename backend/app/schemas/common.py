"""
공통 API 응답 모델

모든 API는 동일한 응답 형식을 사용한다.

성공 예시
{
    "success": true,
    "message": "성공",
    "data": { ... }
}

실패 예시
{
    "success": false,
    "message": "실패",
    "data": null
}
"""

from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    """
    공통 API 응답 모델

    Attributes:
        success : 요청 성공 여부
        message : 사용자에게 전달할 메시지
        data    : 실제 응답 데이터
    """

    # 요청 성공 여부
    success: bool

    # 응답 메시지
    message: str

    # 실제 데이터
    data: Any | None = None