"""
Conversation Service

대화(Conversation)를 관리한다.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.core.constants import DEFAULT_CONVERSATION_TITLE
from app.models.conversation import Conversation
from app.models.user import User


class ConversationService:
    """
    Conversation Service
    """

    def __init__(self, db: Session):
        self.db = db

    # --------------------------------------------------
    # 대화 조회
    # --------------------------------------------------
    def get_by_id(
        self,
        conversation_id: int,
    ) -> Conversation | None:

        stmt = select(Conversation).where(
            Conversation.id == conversation_id
        )

        return self.db.scalar(stmt)

    # --------------------------------------------------
    # 사용자의 대화 조회
    # --------------------------------------------------
    def get_user_conversation(
        self,
        conversation_id: int,
        user: User,
    ) -> Conversation | None:

        stmt = (
            select(Conversation)
            .where(
                Conversation.id == conversation_id,
                Conversation.user_id == user.id,
            )
        )

        return self.db.scalar(stmt)

    # --------------------------------------------------
    # 사용자의 대화 + 메시지 조회
    # --------------------------------------------------
    def get_user_conversation_with_messages(
        self,
        conversation_id: int,
        user: User,
    ) -> Conversation | None:
        """
        Conversation과 Message를 함께 조회한다.

        Conversation 상세 조회 API,
        RAG,
        Streaming 등에서 사용한다.
        """

        stmt = (
            select(Conversation)
            .options(
                selectinload(Conversation.messages),
            )
            .where(
                Conversation.id == conversation_id,
                Conversation.user_id == user.id,
            )
        )

        return self.db.scalar(stmt)

    # --------------------------------------------------
    # 대화 생성
    # --------------------------------------------------
    def create(
        self,
        user: User,
        title: str = DEFAULT_CONVERSATION_TITLE,
    ) -> Conversation:

        conversation = Conversation(
            user_id=user.id,
            title=title,
        )

        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)

        return conversation

    # --------------------------------------------------
    # 사용자 대화 목록
    # --------------------------------------------------
    def get_list(
        self,
        user: User,
    ) -> list[Conversation]:

        stmt = (
            select(Conversation)
            .where(
                Conversation.user_id == user.id,
            )
            .order_by(Conversation.updated_at.desc())
        )

        return list(self.db.scalars(stmt).all())

    # --------------------------------------------------
    # 제목 변경
    # --------------------------------------------------
    def update_title(
        self,
        conversation: Conversation,
        title: str,
    ) -> Conversation:

        conversation.title = title

        self.db.commit()
        self.db.refresh(conversation)

        return conversation

    # --------------------------------------------------
    # 삭제
    # --------------------------------------------------
    def delete(
        self,
        conversation: Conversation,
    ) -> None:

        self.db.delete(conversation)
        self.db.commit()