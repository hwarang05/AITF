"""
Embedding Service

Embedding 생성 서비스
"""

from app.providers.embedding_base import (
    BaseEmbeddingProvider,
)


class EmbeddingService:
    """
    Embedding Service
    """

    def __init__(
        self,
        provider: BaseEmbeddingProvider,
    ):
        self.provider = provider

    async def embed(
        self,
        text: str,
    ) -> list[float]:

        return await self.provider.embed(text)

    async def embed_many(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        return await self.provider.embed_many(
            texts
        )