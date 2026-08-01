"""
Chunk Entity

RAG 검색을 위한 문서 Chunk를 관리한다.
"""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import BaseEntity

if TYPE_CHECKING:
    from app.models.file import File


class Chunk(BaseEntity):
    """
    문서 Chunk
    """

    __tablename__ = "chunks"

    # --------------------------------------------------
    # File
    # --------------------------------------------------

    file_id: Mapped[int] = mapped_column(
        ForeignKey(
            "files.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="파일 ID",
    )

    file: Mapped["File"] = relationship(
        back_populates="chunks",
    )

    # --------------------------------------------------
    # Chunk Index
    # --------------------------------------------------

    chunk_index: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Chunk 순서",
    )

    # --------------------------------------------------
    # Content
    # --------------------------------------------------

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        comment="Chunk 내용",
    )

    # --------------------------------------------------
    # Token Count
    # --------------------------------------------------

    token_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        comment="토큰 수",
    )