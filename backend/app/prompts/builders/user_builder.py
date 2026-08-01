"""
User Prompt Builder
"""

from app.schemas.message import ChatMessage


class UserBuilder:
    @staticmethod
    def build(
        user_message: str,
    ) -> list[ChatMessage]:

        return [
            ChatMessage(
                role="user",
                content=user_message,
            )
        ]