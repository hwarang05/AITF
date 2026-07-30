"""
Authentication Service

사용자 인증 관련 비즈니스 로직을 담당한다.
"""

from sqlalchemy.orm import Session

from app.providers.nas_auth_provider import NASAuthProvider
from app.services.user_service import UserService


class AuthService:
    """
    인증 서비스
    """

    def __init__(self, db: Session):
        self.provider = NASAuthProvider()
        self.user_service = UserService(db)

    async def login(
        self,
        username: str,
        password: str,
    ):
        """
        로그인 처리
        """

        success = await self.provider.authenticate(
            username=username,
            password=password,
        )

        if not success:
            return None

        user = self.user_service.get_or_create(
            nas_username=username,
            display_name=username,
            email=None,
        )

        return user