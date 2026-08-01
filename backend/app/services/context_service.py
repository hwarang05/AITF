"""
Context Service

LLM에 전달할 Context를 생성한다.
"""

from app.models.conversation import Conversation
from app.models.user import User
from app.schemas.context import LLMContext
from app.services.message_service import MessageService
from app.services.profile_service import ProfileService
from app.services.rag_service import RagService
from app.services.summary_service import SummaryService


class ContextService:
    """
    Context Service
    """

    def __init__(
        self,
        message_service: MessageService,
        rag_service: RagService,
        summary_service: SummaryService,
        profile_service: ProfileService,
    ):
        self.message_service = message_service
        self.rag_service = rag_service
        self.summary_service = summary_service
        self.profile_service = profile_service

    async def build(
        self,
        *,
        user: User,
        conversation: Conversation,
        message: str,
    ) -> LLMContext:
        """
        LLM Context 생성
        """

        memory = self.message_service.get_recent_memory(
            conversation=conversation,
        )

        summary = await self.summary_service.get_summary(
            conversation=conversation,
        )

        profile = await self.profile_service.get_profile(
            user=user,
        )

        rag_results = await self.rag_service.search(
            user=user,
            question=message,
        )

        rag_context = "\n\n".join(
            item["content"]
            for item in rag_results
        )

        return LLMContext(
            memory=memory,
            rag_context=rag_context or None,
            summary=summary,
            profile=profile,
        )