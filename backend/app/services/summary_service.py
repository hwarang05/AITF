"""
Summary Service

대화 요약을 관리한다.
"""

from app.models.conversation import Conversation


class SummaryService:
    """
    Summary Service
    """

    async def get_summary(
        self,
        conversation: Conversation,
    ) -> str | None:
        """
        현재는 요약이 없으므로 None 반환.

        추후
        - 일정 메시지 수 이상
        - Token 초과
        - Background Task

        에서 생성하도록 확장한다.
        """

        return None