"""
User Service

AITF 사용자 정보를 관리한다.
"""

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


# --------------------------------------------------
# Korea Standard Time (UTC+9)
# --------------------------------------------------
KST = timezone(timedelta(hours=9))


class UserService:
    """
    User Service

    NAS 인증 성공 후
    AITF 사용자 정보를 관리한다.
    """

    def __init__(self, db: Session):
        self.db = db

    # --------------------------------------------------
    # 사용자 조회
    # --------------------------------------------------
    def get_by_username(
        self,
        nas_username: str,
    ) -> User | None:

        stmt = select(User).where(
            User.nas_username == nas_username
        )

        return self.db.scalar(stmt)

    # --------------------------------------------------
    # 사용자 생성
    # --------------------------------------------------
    def create(
        self,
        nas_username: str,
        display_name: str,
        email: str | None = None,
    ) -> User:

        user = User(
            nas_username=nas_username,
            display_name=display_name,
            email=email,
            is_active=True,
            last_login_at=datetime.now(KST),
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    # --------------------------------------------------
    # 마지막 로그인 갱신
    # --------------------------------------------------
    def update_last_login(
        self,
        user: User,
    ) -> User:

        user.last_login_at = datetime.now(KST)

        self.db.commit()
        self.db.refresh(user)

        return user

    # --------------------------------------------------
    # 조회 또는 생성
    # --------------------------------------------------
    def get_or_create(
        self,
        nas_username: str,
        display_name: str,
        email: str | None = None,
    ) -> User:

        user = self.get_by_username(nas_username)

        if user is None:
            return self.create(
                nas_username=nas_username,
                display_name=display_name,
                email=email,
            )

        return self.update_last_login(user)