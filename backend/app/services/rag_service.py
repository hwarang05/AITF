"""
RAG Service

질문과 관련된 문서를 검색한다.
"""

from app.models.user import User
from app.services.embedding_service import (
    EmbeddingService,
)
from app.services.vector_service import (
    VectorService,
)


class RagService:
    """
    RAG 검색 서비스
    """

    DEFAULT_TOP_K = 5

    DEFAULT_DISTANCE_THRESHOLD = 1.2

    def __init__(
        self,
        embedding_service: EmbeddingService,
        vector_service: VectorService,
    ):
        self.embedding_service = embedding_service
        self.vector_service = vector_service

    async def search(
        self,
        *,
        user: User,
        question: str,
        limit: int | None = None,
    ) -> list[dict]:
        """
        질문과 관련된 Chunk를 검색한다.
        """

        del user

        if limit is None:
            limit = self.DEFAULT_TOP_K

        embedding = await self.embedding_service.embed(
            question,
        )

        results = await self.vector_service.search(
            embedding=embedding,
            limit=limit,
        )

        return [
            item
            for item in results
            if item["distance"] <= self.DEFAULT_DISTANCE_THRESHOLD
        ]