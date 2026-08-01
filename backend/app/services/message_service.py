"""
Message Service

대화 메시지를 관리한다.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.message import Message
from app.schemas.message import ChatMessage


class MessageService:
    """
    Message Service
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    # --------------------------------------------------
    # 메시지 저장
    # --------------------------------------------------
    def create(
        self,
        conversation: Conversation,
        role: str,
        content: str,
    ) -> Message:

        message = Message(
            conversation_id=conversation.id,
            role=role,
            content=content,
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)

        return message

    # --------------------------------------------------
    # 대화 메시지 조회
    # --------------------------------------------------
    def get_messages(
        self,
        conversation: Conversation,
    ) -> list[Message]:

        stmt = (
            select(Message)
            .where(
                Message.conversation_id == conversation.id,
            )
            .order_by(Message.id.asc())
        )

        return list(self.db.scalars(stmt).all())

    # --------------------------------------------------
    # 최근 N개 메시지 조회
    # --------------------------------------------------
    def get_recent_messages(
        self,
        conversation: Conversation,
        limit: int = 20,
    ) -> list[Message]:

        stmt = (
            select(Message)
            .where(
                Message.conversation_id == conversation.id,
            )
            .order_by(Message.id.desc())
            .limit(limit)
        )

        messages = list(self.db.scalars(stmt).all())

        messages.reverse()

        return messages

    # --------------------------------------------------
    # LLM Memory 조회
    # --------------------------------------------------
    def get_recent_memory(
        self,
        conversation: Conversation,
        limit: int = 20,
    ) -> list[ChatMessage]:

        messages = self.get_recent_messages(
            conversation=conversation,
            limit=limit,
        )

        return [
            ChatMessage(
                role=message.role,
                content=message.content,
            )
            for message in messages
        ]

    # --------------------------------------------------
    # 메시지 삭제
    # --------------------------------------------------
    def delete(
        self,
        message: Message,
    ) -> None:

        self.db.delete(message)
        self.db.commit()