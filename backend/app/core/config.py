"""
애플리케이션 환경설정

모든 설정은 .env 파일에서 읽어온다.
개발/운영 환경이 달라도 코드 수정 없이 .env만 변경하면 된다.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


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
    # 사용할 LLM Provider
    LLM_PROVIDER: str

    # LLM 서버 주소
    LLM_BASE_URL: str

    # 사용할 모델명
    LLM_MODEL: str

    # LLM 요청 제한 시간(초)
    LLM_TIMEOUT: int = 120

    # -------------------------
    # Database
    # -------------------------
    # 데이터베이스 연결 문자열
    DATABASE_URL: str

    # SQL 실행 로그 출력 여부
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
    # Authentication
    # (추후 NAS / LDAP 로그인)
    # -------------------------
    NAS_BASE_URL: str
    NAS_VERIFY_SSL: bool = False

    # -------------------------
    # Logging
    # (추후 Log Level 등)
    # -------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()

print(settings.model_dump())