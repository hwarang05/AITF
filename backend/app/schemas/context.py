"""
LLM Context Schema
"""

from pydantic import BaseModel, Field

from app.schemas.message import ChatMessage


class LLMContext(BaseModel):
    """
    LLM에 전달되는 Context
    """

    memory: list[ChatMessage] = Field(default_factory=list)

    rag_context: str | None = None

    summary: str | None = None

    profile: str | None = None