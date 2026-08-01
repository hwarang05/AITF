"""
Prompt Builder

LLM에게 전달할 messages를 생성한다.
"""

from app.prompts.builders import (
    ContextBuilder,
    MemoryBuilder,
    SystemBuilder,
    UserBuilder,
)
from app.schemas.context import LLMContext
from app.schemas.message import ChatMessage


class PromptBuilder:
    @staticmethod
    def build(
        *,
        user_message: str,
        context: LLMContext | None = None,
        system_prompt: str | None = None,
    ) -> list[ChatMessage]:

        context = context or LLMContext()

        messages: list[ChatMessage] = []

        messages.extend(
            SystemBuilder.build(system_prompt)
        )

        messages.extend(
            MemoryBuilder.build(context.memory)
        )

        messages.extend(
            ContextBuilder.build(context)
        )

        messages.extend(
            UserBuilder.build(user_message)
        )

        return messages