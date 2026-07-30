"""
User Entity

AITF 사용자 정보를 관리한다.

인증(Authentication)은 Synology NAS가 담당하고,
AITF는 최소한의 사용자 정보만 관리한다.
"""

from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseEntity


class User(BaseEntity):
    """
    AITF 사용자

    비밀번호는 저장하지 않는다.
    NAS 인증 성공 후 사용자 정보를 관리한다.
    """

    __tablename__ = "users"

    # -------------------------
    # NAS Username
    # -------------------------
    nas_username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
        comment="NAS 로그인 ID",
    )

    # -------------------------
    # Display Name
    # -------------------------
    display_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        comment="사용자 이름",
    )

    # -------------------------
    # Email
    # -------------------------
    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="이메일",
    )

    # -------------------------
    # Active
    # -------------------------
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        comment="사용 가능 여부",
    )

    # -------------------------
    # Last Login
    # -------------------------
    last_login_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        comment="마지막 로그인 시간",
    )