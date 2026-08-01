"""
Ollama Provider

LLM과 직접 통신하는 계층이다.
Service는 Provider만 호출하며,
실제 API 주소나 통신 방식은 Provider 내부에 숨긴다.
"""

import json
from collections.abc import AsyncGenerator

import httpx

from app.core.config import settings
from app.providers.base import BaseLLMProvider
from app.schemas.message import ChatMessage


class OllamaProvider(BaseLLMProvider):
    """
    Ollama와 통신하는 Provider
    """

    @staticmethod
    def _serialize_messages(
        messages: list[ChatMessage],
    ) -> list[dict[str, str]]:

        return [
            message.model_dump()
            for message in messages
        ]

    @staticmethod
    def _build_payload(
        messages: list[ChatMessage],
        stream: bool,
    ) -> dict:

        return {
            "model": settings.LLM_MODEL,
            "messages": OllamaProvider._serialize_messages(
                messages
            ),
            "stream": stream,
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

    async def chat(
        self,
        messages: list[ChatMessage],
    ) -> str:

        payload = self._build_payload(
            messages,
            stream=False,
        )

        try:

            async with httpx.AsyncClient(
                timeout=settings.LLM_TIMEOUT,
            ) as client:

                response = await client.post(
                    f"{settings.LLM_BASE_URL}/api/chat",
                    json=payload,
                )

                response.raise_for_status()

                return response.json()["message"]["content"]

        except Exception as e:
            self._handle_exception(e)

    async def stream(
        self,
        messages: list[ChatMessage],
    ) -> AsyncGenerator[str, None]:

        payload = self._build_payload(
            messages,
            stream=True,
        )

        try:

            async with httpx.AsyncClient(
                timeout=None,
            ) as client:

                async with client.stream(
                    "POST",
                    f"{settings.LLM_BASE_URL}/api/chat",
                    json=payload,
                ) as response:

                    response.raise_for_status()

                    async for line in response.aiter_lines():

                        if not line:
                            continue

                        data = json.loads(line)

                        if "message" in data:

                            content = data[
                                "message"
                            ].get(
                                "content",
                                "",
                            )

                            if content:
                                yield content

                        if data.get("done"):
                            break

        except Exception as e:
            self._handle_exception(e)