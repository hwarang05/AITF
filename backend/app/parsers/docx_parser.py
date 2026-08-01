"""
DOCX Parser
"""

from pathlib import Path

from docx import Document

from app.parsers.base import BaseParser


class DocxParser(BaseParser):
    """
    DOCX Parser
    """

    extensions = {
        ".docx",
    }

    def supports(
        self,
        path: Path,
    ) -> bool:

        return path.suffix.lower() in self.extensions

    def parse(
        self,
        path: Path,
    ) -> str:

        document = Document(path)

        texts: list[str] = []

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text:
                texts.append(text)

        return "\n".join(texts)