"""
LLM Service

AI 모델과의 대화를 담당하는 서비스.
API는 Provider를 직접 호출하지 않고
항상 Service를 통해 접근한다.
"""

from collections.abc import AsyncGenerator

from app.prompts.prompt_builder import PromptBuilder
from app.prompts.title import TITLE_SYSTEM_PROMPT
from app.providers.base import BaseLLMProvider
from app.schemas.context import LLMContext


class LLMService:
    """
    LLM 서비스
    """

    def __init__(
        self,
        provider: BaseLLMProvider,
    ):
        self.provider = provider

    @staticmethod
    def _build_messages(
        *,
        message: str,
        context: LLMContext | None = None,
        system_prompt: str | None = None,
    ):

        return PromptBuilder.build(
            user_message=message,
            context=context,
            system_prompt=system_prompt,
        )

    async def chat(
        self,
        *,
        message: str,
        context: LLMContext,
    ) -> str:

        messages = self._build_messages(
            message=message,
            context=context,
        )

        return await self.provider.chat(messages)

    async def stream(
        self,
        *,
        message: str,
        context: LLMContext,
    ) -> AsyncGenerator[str, None]:

        messages = self._build_messages(
            message=message,
            context=context,
        )

        async for token in self.provider.stream(messages):
            yield token

    async def generate_title(
        self,
        question: str,
        answer: str,
    ) -> str:

        messages = self._build_messages(
            message=(
                f"질문\n{question}\n\n"
                f"답변\n{answer}"
            ),
            system_prompt=TITLE_SYSTEM_PROMPT,
        )

        return (
            await self.provider.chat(messages)
        ).strip()