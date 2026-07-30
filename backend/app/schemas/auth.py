"""
Authentication Schema
"""

from pydantic import BaseModel


class LoginRequest(BaseModel):
    """
    로그인 요청
    """

    username: str
    password: str


class LoginResponse(BaseModel):
    """
    로그인 응답
    """

    success: bool
    message: str