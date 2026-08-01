"""
Embedding Provider Factory

설정에 따라 사용할 Embedding Provider를 반환한다.
"""

from app.core.config import settings
from app.providers.embedding_base import (
    BaseEmbeddingProvider,
)
from app.providers.ollama_embedding_provider import (
    OllamaEmbeddingProvider,
)


PROVIDERS: dict[
    str,
    type[BaseEmbeddingProvider],
] = {
    "ollama": OllamaEmbeddingProvider,
}


def get_embedding_provider() -> BaseEmbeddingProvider:
    """
    설정에 따라 사용할 Embedding Provider를 생성한다.
    """

    provider_name = settings.LLM_PROVIDER.lower()

    provider_class = PROVIDERS.get(
        provider_name,
    )

    if provider_class is None:

        supported = ", ".join(
            PROVIDERS,
        )

        raise ValueError(
            f"지원하지 않는 Embedding Provider입니다: "
            f"{provider_name} "
            f"(지원: {supported})"
        )

    return provider_class()