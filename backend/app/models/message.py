"""
Message Entity

대화 내의 개별 메시지를 관리한다.
"""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import BaseEntity

if TYPE_CHECKING:
    from app.models.conversation import Conversation


class Message(BaseEntity):
    """
    대화 메시지
    """

    __tablename__ = "messages"

    # -------------------------
    # Conversation
    # -------------------------
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey(
            "conversations.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="대화 ID",
    )

    conversation: Mapped["Conversation"] = relationship(
        back_populates="messages",
    )

    # -------------------------
    # Role
    # -------------------------
    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        comment="user / assistant / system",
    )

    # -------------------------
    # Content
    # -------------------------
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        comment="메시지 내용",
    )