"""
Provider Factory

설정에 따라 사용할 LLM Provider를 반환한다.
"""

from app.core.config import settings
from app.providers.base import BaseLLMProvider
from app.providers.ollama_provider import OllamaProvider
from app.providers.openai_provider import OpenAIProvider


# 사용할 Provider 목록
PROVIDERS = {
    "ollama": OllamaProvider,
    "openai": OpenAIProvider,
}


def get_provider() -> BaseLLMProvider:
    """
    설정에 따라 사용할 LLM Provider를 생성하여 반환한다.
    """

    provider_name = settings.LLM_PROVIDER.lower()

    provider_class = PROVIDERS.get(provider_name)

    if provider_class is None:
        supported = ", ".join(PROVIDERS.keys())
        raise ValueError(
            f"지원하지 않는 LLM Provider입니다: {provider_name} "
            f"(지원: {supported})"
        )

    return provider_class()