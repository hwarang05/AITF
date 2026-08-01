"""
Chunk Service

문서 Chunk를 관리한다.
"""

from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.chunk import Chunk
from app.models.file import File


class ChunkService:
    """
    Chunk Service
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    # --------------------------------------------------
    # Chunk 생성
    # --------------------------------------------------
    def create(
        self,
        file: File,
        chunk_index: int,
        content: str,
        token_count: int = 0,
    ) -> Chunk:

        chunk = Chunk(
            file_id=file.id,
            chunk_index=chunk_index,
            content=content,
            token_count=token_count,
        )

        self.db.add(chunk)
        self.db.commit()
        self.db.refresh(chunk)

        return chunk

    # --------------------------------------------------
    # Chunk 일괄 생성
    # --------------------------------------------------
    def create_many(
        self,
        file: File,
        chunks: list[str],
    ) -> list[Chunk]:

        entities: list[Chunk] = []

        for index, content in enumerate(chunks):

            entities.append(
                Chunk(
                    file_id=file.id,
                    chunk_index=index,
                    content=content,
                    token_count=len(content.split()),
                )
            )

        self.db.add_all(entities)
        self.db.commit()

        for entity in entities:
            self.db.refresh(entity)

        return entities

    # --------------------------------------------------
    # File의 Chunk 조회
    # --------------------------------------------------
    def get_chunks(
        self,
        file: File,
    ) -> list[Chunk]:

        stmt = (
            select(Chunk)
            .where(
                Chunk.file_id == file.id,
            )
            .order_by(
                Chunk.chunk_index.asc(),
            )
        )

        return list(self.db.scalars(stmt).all())

    # --------------------------------------------------
    # Chunk 전체 삭제
    # --------------------------------------------------
    def delete_by_file(
        self,
        file: File,
    ) -> None:

        stmt = delete(Chunk).where(
            Chunk.file_id == file.id,
        )

        self.db.execute(stmt)
        self.db.commit()