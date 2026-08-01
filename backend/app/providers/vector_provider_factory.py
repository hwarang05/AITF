"""
Vector Provider Factory

설정에 따라 사용할 Vector Provider를 반환한다.
"""

from app.providers.vector_base import (
    BaseVectorProvider,
)
from app.providers.chromadb_provider import (
    ChromaDBProvider,
)


PROVIDERS: dict[
    str,
    type[BaseVectorProvider],
] = {
    "chromadb": ChromaDBProvider,
}


def get_vector_provider() -> BaseVectorProvider:
    """
    Vector Provider 생성
    """

    provider_class = PROVIDERS["chromadb"]

    return provider_class()