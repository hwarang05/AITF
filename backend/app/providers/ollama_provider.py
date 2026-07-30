"""
Ollama Provider

LLM과 직접 통신하는 계층이다.
Service는 Provider만 호출하며,
실제 API 주소나 통신 방식은 Provider 내부에 숨긴다.
"""

import httpx

from app.core.config import settings
from app.providers.base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    """
    Ollama와 통신하는 Provider
    """

    async def chat(
        self,
        messages: list[dict[str, str]],
    ) -> str:
        """
        Ollama Chat API 호출

        Args:
            messages:
                LLM에게 전달할 messages 목록

        Returns:
            AI가 생성한 응답 문자열
        """

        # Ollama Chat API 요청 데이터
        payload = {
            "model": settings.LLM_MODEL,
            "messages": messages,
            "stream": False,
        }

        try:
            async with httpx.AsyncClient(
                timeout=settings.LLM_TIMEOUT,
            ) as client:

                response = await client.post(
                    f"{settings.LLM_BASE_URL}/api/chat",
                    json=payload,
                )

                # HTTP 오류 발생 시 예외 발생
                response.raise_for_status()

                # JSON 응답
                data = response.json()

                # AI 응답 반환
                return data["message"]["content"]

        except httpx.ConnectError as e:
            raise RuntimeError(
                "Ollama 서버에 연결할 수 없습니다."
            ) from e

        except httpx.TimeoutException as e:
            raise RuntimeError(
                "Ollama 응답 시간이 초과되었습니다."
            ) from e

        except httpx.HTTPStatusError as e:
            raise RuntimeError(
                f"Ollama API 오류: {e.response.status_code}"
            ) from e