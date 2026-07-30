"""
OpenAI Provider

OpenAI API와 통신하는 Provider
"""

from app.providers.base import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):

    async def chat(
        self,
        prompt: str,
    ) -> str:

        raise NotImplementedError(
            "OpenAI Provider는 아직 구현되지 않았습니다."
        )