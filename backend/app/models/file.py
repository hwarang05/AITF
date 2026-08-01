"""
File Entity

NAS 파일 메타데이터를 관리한다.
"""

from typing import TYPE_CHECKING

from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import BaseEntity

if TYPE_CHECKING:
    from app.models.chunk import Chunk


class File(BaseEntity):
    """
    NAS File
    """

    __tablename__ = "files"

    # --------------------------------------------------
    # NAS Path
    # --------------------------------------------------

    path: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
        unique=True,
        index=True,
        comment="NAS 전체 경로",
    )

    # --------------------------------------------------
    # File Name
    # --------------------------------------------------

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="파일명",
    )

    # --------------------------------------------------
    # Extension
    # --------------------------------------------------

    extension: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        comment="확장자",
    )

    # --------------------------------------------------
    # File Size
    # --------------------------------------------------

    size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
        comment="파일 크기(Byte)",
    )

    # --------------------------------------------------
    # Indexed
    # --------------------------------------------------

    indexed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        comment="벡터 생성 여부",
    )

    # --------------------------------------------------
    # Enabled
    # --------------------------------------------------

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        comment="검색 사용 여부",
    )

    # --------------------------------------------------
    # Chunks
    # --------------------------------------------------

    chunks: Mapped[list["Chunk"]] = relationship(
        back_populates="file",
        cascade="all, delete-orphan",
        order_by="Chunk.chunk_index",
    )