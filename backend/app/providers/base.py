"""
LLM Provider Interface

모든 LLM(OpenAI, Ollama, Claude, Gemini)은
이 인터페이스를 구현해야 한다.
"""

from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    LLM Provider 추상 클래스

    모든 Provider는 아래 메서드를 반드시 구현해야 한다.
    """

    @abstractmethod
    async def chat(
        self,
        messages: list[dict],
    ) -> str:
        """
        LLM에게 전달할 messages를 받아
        AI의 응답을 반환한다.

        Args:
            messages:
                OpenAI/Ollama 형식의 메시지 목록

        Returns:
            AI 응답 문자열
        """
        raise NotImplementedError