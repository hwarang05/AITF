"""
Chat Schema

채팅 API에서 사용하는 Request/Response 모델
"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    사용자 질문
    """

    message: str