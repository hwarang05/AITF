"""
Chat Service

사용자와 AI의 대화를 관리한다.
"""

from collections.abc import AsyncGenerator

from app.core.constants import DEFAULT_CONVERSATION_TITLE
from app.core.exceptions import NotFoundException
from app.core.logger import logger
from app.models.conversation import Conversation
from app.models.user import User
from app.schemas.chat import ChatResponse
from app.schemas.context import LLMContext
from app.services.context_service import ContextService
from app.services.conversation_service import ConversationService
from app.services.llm_service import LLMService
from app.services.message_service import MessageService


class ChatService:
    """
    Chat Service
    """

    def __init__(
        self,
        conversation_service: ConversationService,
        message_service: MessageService,
        llm_service: LLMService,
        context_service: ContextService,
    ):
        self.conversation_service = conversation_service
        self.message_service = message_service
        self.llm_service = llm_service
        self.context_service = context_service

    # --------------------------------------------------
    # Conversation 조회 또는 생성
    # --------------------------------------------------

    def _get_or_create_conversation(
        self,
        user: User,
        conversation_id: int | None,
    ) -> Conversation:

        if conversation_id is None:
            return self.conversation_service.create(user=user)

        return self._get_user_conversation_or_raise(
            conversation_id=conversation_id,
            user=user,
        )

    # --------------------------------------------------
    # Conversation 조회
    # --------------------------------------------------

    def _get_user_conversation_or_raise(
        self,
        *,
        conversation_id: int,
        user: User,
    ) -> Conversation:

        conversation = self.conversation_service.get_user_conversation(
            conversation_id=conversation_id,
            user=user,
        )

        if conversation is None:
            raise NotFoundException("대화를 찾을 수 없습니다.")

        return conversation

    # --------------------------------------------------
    # Message 저장
    # --------------------------------------------------

    def _save_messages(
        self,
        *,
        conversation: Conversation,
        question: str,
        answer: str,
    ) -> None:

        self.message_service.create(
            conversation=conversation,
            role="user",
            content=question,
        )

        self.message_service.create(
            conversation=conversation,
            role="assistant",
            content=answer,
        )

    # --------------------------------------------------
    # 제목 생성
    # --------------------------------------------------

    async def _generate_title(
        self,
        *,
        conversation: Conversation,
        question: str,
        answer: str,
    ) -> None:

        if conversation.title != DEFAULT_CONVERSATION_TITLE:
            return

        try:

            title = await self.llm_service.generate_title(
                question=question,
                answer=answer,
            )

            self.conversation_service.update_title(
                conversation=conversation,
                title=title,
            )

        except Exception:

            logger.exception(
                "Failed to generate conversation title."
            )

    # --------------------------------------------------
    # 채팅 준비
    # --------------------------------------------------

    async def _prepare_chat(
        self,
        *,
        user: User,
        message: str,
        conversation_id: int | None,
    ) -> tuple[Conversation, LLMContext]:

        conversation = self._get_or_create_conversation(
            user=user,
            conversation_id=conversation_id,
        )

        context = await self.context_service.build(
            user=user,
            conversation=conversation,
            message=message,
        )

        return conversation, context

    # --------------------------------------------------
    # 일반 채팅
    # --------------------------------------------------

    async def chat(
        self,
        user: User,
        message: str,
        conversation_id: int | None = None,
    ) -> ChatResponse:

        conversation, context = await self._prepare_chat(
            user=user,
            message=message,
            conversation_id=conversation_id,
        )

        answer = await self.llm_service.chat(
            message=message,
            context=context,
        )

        self._save_messages(
            conversation=conversation,
            question=message,
            answer=answer,
        )

        await self._generate_title(
            conversation=conversation,
            question=message,
            answer=answer,
        )

        return ChatResponse(
            conversation_id=conversation.id,
            question=message,
            answer=answer,
        )

    # --------------------------------------------------
    # Streaming 채팅
    # --------------------------------------------------

    async def stream_chat(
        self,
        user: User,
        message: str,
        conversation_id: int | None = None,
    ) -> AsyncGenerator[str, None]:

        conversation, context = await self._prepare_chat(
            user=user,
            message=message,
            conversation_id=conversation_id,
        )

        answer = ""

        try:

            async for token in self.llm_service.stream(
                message=message,
                context=context,
            ):
                answer += token
                yield token

        finally:

            if answer:

                self._save_messages(
                    conversation=conversation,
                    question=message,
                    answer=answer,
                )

                await self._generate_title(
                    conversation=conversation,
                    question=message,
                    answer=answer,
                )

    # --------------------------------------------------
    # 대화 목록 조회
    # --------------------------------------------------

    def get_conversations(
        self,
        user: User,
    ) -> list[Conversation]:

        return self.conversation_service.get_list(user)

    # --------------------------------------------------
    # 대화 상세 조회
    # --------------------------------------------------

    def get_conversation(
        self,
        conversation_id: int,
        user: User,
    ) -> Conversation:

        conversation = (
            self.conversation_service.get_user_conversation_with_messages(
                conversation_id=conversation_id,
                user=user,
            )
        )

        if conversation is None:
            raise NotFoundException("대화를 찾을 수 없습니다.")

        return conversation

    # --------------------------------------------------
    # 대화 제목 변경
    # --------------------------------------------------

    def update_conversation_title(
        self,
        conversation_id: int,
        title: str,
        user: User,
    ) -> Conversation:

        conversation = self._get_user_conversation_or_raise(
            conversation_id=conversation_id,
            user=user,
        )

        return self.conversation_service.update_title(
            conversation=conversation,
            title=title,
        )

    # --------------------------------------------------
    # 대화 삭제
    # --------------------------------------------------

    def delete_conversation(
        self,
        conversation_id: int,
        user: User,
    ) -> None:

        conversation = self._get_user_conversation_or_raise(
            conversation_id=conversation_id,
            user=user,
        )

        self.conversation_service.delete(conversation)