"""
Authentication Service

사용자 인증 관련 비즈니스 로직을 담당한다.
"""

from app.providers.nas_auth_provider import NASAuthProvider


class AuthService:
    """
    인증 서비스
    """

    def __init__(self):
        self.provider = NASAuthProvider()

    async def login(
        self,
        username: str,
        password: str,
    ) -> bool:
        """
        NAS 로그인

        Returns
        -------
        bool
            로그인 성공 여부
        """

        return await self.provider.authenticate(
            username=username,
            password=password,
        )