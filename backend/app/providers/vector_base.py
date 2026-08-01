"""
Vector Store Provider Interface
"""

from abc import ABC
from abc import abstractmethod


class BaseVectorProvider(ABC):
    """
    Vector Store Provider 추상 클래스
    """

    @abstractmethod
    async def upsert(
        self,
        *,
        ids: list[str],
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
    ) -> None:
        """
        Vector 저장
        """
        raise NotImplementedError

    @abstractmethod
    async def search(
        self,
        *,
        embedding: list[float],
        limit: int = 5,
    ) -> list[dict]:
        """
        Vector 검색
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(
        self,
        *,
        ids: list[str],
    ) -> None:
        """
        Vector 삭제
        """
        raise NotImplementedError