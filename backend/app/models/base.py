"""
SQLAlchemy Base

모든 ORM 모델의 부모 클래스와
공통 Entity를 정의한다.
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    """
    모든 ORM 모델의 최상위 Base 클래스
    """

    pass


class BaseEntity(Base):
    """
    모든 ORM 모델이 공통으로 사용하는 Entity

    공통 컬럼:
    - id
    - created_at
    - updated_at
    """

    __abstract__ = True

    # -------------------------
    # Primary Key
    # -------------------------
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    # -------------------------
    # Created At
    # -------------------------
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # -------------------------
    # Updated At
    # -------------------------
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )