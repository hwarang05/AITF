"""
Ollama Embedding Provider

Ollama Embedding API와 직접 통신하는 Provider이다.
"""

import httpx

from app.core.config import settings
from app.providers.embedding_base import (
    BaseEmbeddingProvider,
)


class OllamaEmbeddingProvider(
    BaseEmbeddingProvider,
):
    """
    Ollama Embedding Provider
    """

    @staticmethod
    def _build_payload(
        input_data: str | list[str],
    ) -> dict:

        return {
            "model": settings.LLM_MODEL,
            "input": input_data,
        }

    @staticmethod
    def _handle_exception(
        e: Exception,
    ) -> None:

        if isinstance(
            e,
            httpx.ConnectError,
        ):
            raise RuntimeError(
                "Ollama 서버에 연결할 수 없습니다."
            ) from e

        if isinstance(
            e,
            httpx.TimeoutException,
        ):
            raise RuntimeError(
                "Ollama 응답 시간이 초과되었습니다."
            ) from e

        if isinstance(
            e,
            httpx.HTTPStatusError,
        ):
            raise RuntimeError(
                f"Ollama API 오류: {e.response.status_code}"
            ) from e

        raise e

    async def _request(
        self,
        input_data: str | list[str],
    ) -> list[list[float]]:

        payload = self._build_payload(
            input_data,
        )

        try:

            async with httpx.AsyncClient(
                timeout=settings.LLM_TIMEOUT,
            ) as client:

                response = await client.post(
                    f"{settings.LLM_BASE_URL}/api/embed",
                    json=payload,
                )

                response.raise_for_status()

                data = response.json()

                embeddings = data.get(
                    "embeddings",
                    [],
                )

                if not embeddings:
                    raise RuntimeError(
                        "Embedding 생성에 실패했습니다."
                    )

                return embeddings

        except Exception as e:
            self._handle_exception(e)

    async def embed(
        self,
        text: str,
    ) -> list[float]:

        embeddings = await self._request(
            text,
        )

        return embeddings[0]

    async def embed_many(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        return await self._request(
            texts,
        )