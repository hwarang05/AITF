"""
Profile Service

사용자 Profile을 관리한다.
"""

from app.models.user import User


class ProfileService:
    """
    Profile Service
    """

    async def get_profile(
        self,
        user: User,
    ) -> dict | None:
        """
        LLM에서 사용할 사용자 Profile을 반환한다.

        현재는 Profile 기능이 없으므로 None을 반환한다.

        추후
        - 부서
        - 직급
        - 프로젝트
        - 권한
        - 개인 설정
        등을 반환하도록 확장한다.
        """

        return None