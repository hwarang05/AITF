"""
Conversation Entity

사용자와 AI의 대화 세션을 관리한다.
"""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import BaseEntity

if TYPE_CHECKING:
    from app.models.message import Message
    from app.models.user import User


class Conversation(BaseEntity):
    """
    대화 세션
    """

    __tablename__ = "conversations"

    # -------------------------
    # User
    # -------------------------
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="사용자 ID",
    )

    user: Mapped["User"] = relationship(
        back_populates="conversations",
    )

    # -------------------------
    # Title
    # -------------------------
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        default="새 대화",
        comment="대화 제목",
    )

    # -------------------------
    # Messages
    # -------------------------
    messages: Mapped[list["Message"]] = relationship(
        back_populates="conversation",
        cascade="all, delete-orphan",
        order_by="Message.id",
    )