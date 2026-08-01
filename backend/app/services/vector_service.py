"""
Vector Service
"""

from app.providers.vector_base import (
    BaseVectorProvider,
)


class VectorService:
    """
    Vector Service
    """

    def __init__(
        self,
        provider: BaseVectorProvider,
    ):
        self.provider = provider

    async def upsert(
        self,
        *,
        ids: list[str],
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
    ) -> None:

        await self.provider.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    async def search(
        self,
        *,
        embedding: list[float],
        limit: int = 5,
    ) -> list[dict]:

        return await self.provider.search(
            embedding=embedding,
            limit=limit,
        )

    async def delete(
        self,
        *,
        ids: list[str],
    ) -> None:

        await self.provider.delete(
            ids=ids,
        )