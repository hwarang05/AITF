"""
Dependency Injection

FastAPI Dependency를 관리한다.
"""

from app.providers.provider_factory import get_provider
from app.services.llm_service import LLMService


def get_llm_service() -> LLMService:
    """
    LLMService를 생성한다.
    """

    provider = get_provider()

    return LLMService(provider)