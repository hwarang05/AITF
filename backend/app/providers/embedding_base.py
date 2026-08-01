"""
Embedding Provider Interface

모든 Embedding Provider는
이 인터페이스를 구현해야 한다.
"""

from abc import ABC
from abc import abstractmethod


class BaseEmbeddingProvider(ABC):
    """
    Embedding Provider 추상 클래스
    """

    @abstractmethod
    async def embed(
        self,
        text: str,
    ) -> list[float]:
        """
        Embedding 생성
        """
        raise NotImplementedError

    async def embed_many(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        vectors = []

        for text in texts:
            vectors.append(
                await self.embed(text)
            )

        return vectors