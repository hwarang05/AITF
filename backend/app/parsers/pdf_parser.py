"""
PDF Parser
"""

from pathlib import Path

from pypdf import PdfReader

from app.parsers.base import BaseParser


class PdfParser(BaseParser):
    """
    PDF Parser
    """

    extensions = {
        ".pdf",
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

        reader = PdfReader(path)

        texts: list[str] = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                texts.append(text)

        return "\n".join(texts)