"""
OpenAI Provider

OpenAI API와 통신하는 Provider
"""

from collections.abc import AsyncGenerator

from app.providers.base import BaseLLMProvider
from app.schemas.message import ChatMessage


class OpenAIProvider(BaseLLMProvider):
    """
    OpenAI Provider
    """

    async def chat(
        self,
        messages: list[ChatMessage],
    ) -> str:

        raise NotImplementedError(
            "OpenAI Provider는 아직 구현되지 않았습니다."
        )
  
    async def stream(
        self,
        messages: list[ChatMessage],
    ) -> AsyncGenerator[str, None]:

        raise NotImplementedError(
            "OpenAI Provider는 아직 구현되지 않았습니다."
        )