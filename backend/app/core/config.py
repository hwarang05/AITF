"""
프로젝트 공통 설정

환경변수(.env)를 읽어와
프로젝트 전체에서 사용하는 설정을 관리한다.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    프로젝트 설정
    """

    # ---------------------------------------------------------
    # App
    # ---------------------------------------------------------

    APP_NAME: str = "AITF Backend"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "AI Technology Framework Backend"

    DEBUG: bool = True

    # ---------------------------------------------------------
    # API
    # ---------------------------------------------------------

    API_PREFIX: str = "/api/v1"

    # ---------------------------------------------------------
    # Environment
    # ---------------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()