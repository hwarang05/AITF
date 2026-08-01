"""
TXT Parser
"""

from pathlib import Path

from app.parsers.base import BaseParser


class TxtParser(BaseParser):
    """
    TXT Parser
    """

    extensions = {
        ".txt",
        ".md",
        ".log",
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

        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        )