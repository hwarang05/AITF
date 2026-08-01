"""
LLM Provider Interface

모든 LLM(OpenAI, Ollama, Claude)은
이 인터페이스를 구현해야 한다.
"""

from abc import ABC
from abc import abstractmethod
from collections.abc import AsyncGenerator

from app.schemas.message import ChatMessage


class BaseLLMProvider(ABC):
    """
    LLM Provider 추상 클래스
    """

    @abstractmethod
    async def chat(
        self,
        messages: list[ChatMessage],
    ) -> str:
        """
        일반 Chat 요청
        """
        raise NotImplementedError

    @abstractmethod
    async def stream(
        self,
        messages: list[ChatMessage],
    ) -> AsyncGenerator[str, None]:
        """
        Streaming Chat 요청
        """
        raise NotImplementedError