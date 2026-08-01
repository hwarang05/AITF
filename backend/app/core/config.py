"""
애플리케이션 환경설정

모든 설정은 .env 파일에서 읽어온다.
개발/운영 환경이 달라도 코드 수정 없이 .env만 변경하면 된다.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.logger import logger


class Settings(BaseSettings):
    # -------------------------
    # Application
    # -------------------------
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str

    DEBUG: bool
    API_PREFIX: str

    # -------------------------
    # LLM
    # -------------------------

    LLM_PROVIDER: str
    LLM_BASE_URL: str
    LLM_MODEL: str
    LLM_TIMEOUT: int = 120

    # -------------------------
    # Database
    # -------------------------

    DATABASE_URL: str
    DATABASE_ECHO: bool = False

    # -------------------------
    # Vector DB
    # -------------------------

    VECTOR_DB_PROVIDER: str
    VECTOR_DB_URL: str

    # -------------------------
    # Storage
    # -------------------------

    FILE_STORAGE: str

    # -------------------------
    # NAS
    # -------------------------

    NAS_BASE_URL: str
    NAS_VERIFY_SSL: bool = False

    # -------------------------
    # JWT
    # -------------------------

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

if settings.DEBUG:
    logger.debug(settings.model_dump())