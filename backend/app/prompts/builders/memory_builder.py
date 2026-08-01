"""
Memory Prompt Builder
"""

from app.schemas.message import ChatMessage


class MemoryBuilder:
    @staticmethod
    def build(
        memory: list[ChatMessage] | None = None,
    ) -> list[ChatMessage]:

        return memory or []