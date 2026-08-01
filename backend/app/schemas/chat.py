"""
Chat Schema

Chat API에서 사용하는 Request / Response 모델
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


# =============================================================================
# Base
# =============================================================================


class ORMBaseModel(BaseModel):
    """
    ORM Base Model
    """

    model_config = ConfigDict(
        from_attributes=True,
    )


# =============================================================================
# Chat
# =============================================================================


class ChatRequest(BaseModel):
    """
    Chat Request
    """

    conversation_id: int | None = Field(
        default=None,
        description="대화 ID (없으면 새 대화 생성)",
    )

    message: str = Field(
        ...,
        min_length=1,
        description="사용자 질문",
    )


class ChatResponse(ORMBaseModel):
    """
    Chat Response
    """

    conversation_id: int

    question: str

    answer: str


# =============================================================================
# Conversation
# =============================================================================


class ConversationSummary(ORMBaseModel):
    """
    대화 목록
    """

    id: int

    title: str

    updated_at: datetime


class ConversationUpdateRequest(BaseModel):
    """
    대화 제목 변경
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="대화 제목",
    )


# =============================================================================
# Message
# =============================================================================


class MessageResponse(ORMBaseModel):
    """
    메시지
    """

    id: int

    role: str

    content: str

    created_at: datetime


# =============================================================================
# Conversation Detail
# =============================================================================


class ConversationDetailResponse(ORMBaseModel):
    """
    대화 상세
    """

    id: int

    title: str

    messages: list[MessageResponse]