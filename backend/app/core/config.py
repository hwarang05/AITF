"""
AITF 환경설정 관리

이 파일은 프로젝트에서 사용하는 모든 환경설정(.env)을 관리한다.

앞으로 추가될 설정 예시
- PostgreSQL 접속 정보
- Qdrant 주소
- Ollama 주소
- JWT Secret
- Synology NAS 정보

프로젝트 전체에서 아래처럼 사용한다.

from app.core.config import settings

print(settings.APP_NAME)
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    프로젝트 환경설정 클래스

    BaseSettings를 상속받으면
    .env 파일의 값을 자동으로 읽어온다.
    """

    # ---------------------------------------------------------
    # Application
    # ---------------------------------------------------------

    # 프로젝트 이름 (Swagger 제목 등에서 사용)
    APP_NAME: str = "AITF"

    # 개발 모드 여부
    DEBUG: bool = True

    # ---------------------------------------------------------
    # .env 설정
    # ---------------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


# 프로젝트 전체에서 공통으로 사용하는 설정 객체
settings = Settings()