"""
System Prompt Builder
"""

from app.prompts.system import DEFAULT_SYSTEM_PROMPT
from app.schemas.message import ChatMessage


class SystemBuilder:
    @staticmethod
    def build(
        system_prompt: str | None = None,
    ) -> list[ChatMessage]:

        return [
            ChatMessage(
                role="system",
                content=system_prompt or DEFAULT_SYSTEM_PROMPT,
            )
        ]