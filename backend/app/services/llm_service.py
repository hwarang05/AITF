"""
LLM Service

AI 모델과의 대화를 담당하는 서비스.
API는 Provider를 직접 호출하지 않고
항상 Service를 통해 접근한다.
"""

from app.prompts.prompt_builder import PromptBuilder
from app.providers.base import BaseLLMProvider


class LLMService:
    """
    LLM 서비스
    """

    def __init__(self, provider: BaseLLMProvider):
        """
        사용할 Provider를 주입받는다.
        """

        self.provider = provider

    async def chat(self, message: str) -> str:
        """
        AI에게 질문한다.
        """

        # LLM에게 전달할 messages 생성
        messages = PromptBuilder.build(message)

        # Provider 호출
        return await self.provider.chat(messages)