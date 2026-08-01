"""
Indexing Service

파일을 분석하여 Chunk를 생성한다.
"""

from pathlib import Path

from app.models.file import File
from app.parsers.factory import ParserFactory
from app.services.chunk_service import ChunkService


class IndexingService:
    """
    File Indexing Service
    """

    def __init__(
        self,
        chunk_service: ChunkService,
    ):
        self.chunk_service = chunk_service

    # --------------------------------------------------
    # Index
    # --------------------------------------------------
    def index(
        self,
        file: File,
    ) -> None:

        path = Path(file.path)

        parser = ParserFactory.get_parser(path)

        text = parser.parse(path)

        chunks = self._split_text(text)

        self.chunk_service.delete_by_file(file)

        self.chunk_service.create_many(
            file=file,
            chunks=chunks,
        )

    # --------------------------------------------------
    # Split Text
    # --------------------------------------------------
    def _split_text(
        self,
        text: str,
        max_length: int = 1000,
    ) -> list[str]:

        text = text.strip()

        if not text:
            return []

        paragraphs = [
            p.strip()
            for p in text.split("\n\n")
            if p.strip()
        ]

        results: list[str] = []

        for paragraph in paragraphs:

            if len(paragraph) <= max_length:
                results.append(paragraph)
                continue

            start = 0

            while start < len(paragraph):

                results.append(
                    paragraph[start:start + max_length]
                )

                start += max_length

        return results