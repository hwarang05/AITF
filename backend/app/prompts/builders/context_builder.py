"""
Context Prompt Builder
"""

from app.schemas.context import LLMContext
from app.schemas.message import ChatMessage


class ContextBuilder:
    @staticmethod
    def build(
        context: LLMContext,
    ) -> list[ChatMessage]:

        messages: list[ChatMessage] = []

        if context.summary:
            messages.append(
                ChatMessage(
                    role="system",
                    content=f"대화 요약\n\n{context.summary}",
                )
            )

        if context.profile:
            messages.append(
                ChatMessage(
                    role="system",
                    content=f"사용자 정보\n\n{context.profile}",
                )
            )

        if context.rag_context:
            messages.append(
                ChatMessage(
                    role="system",
                    content=(
                        "다음 정보를 참고하여 답변하세요.\n\n"
                        f"{context.rag_context}"
                    ),
                )
            )

        return messages