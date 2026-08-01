"""
Parser Factory
"""

from pathlib import Path

from app.parsers.base import BaseParser
from app.parsers.docx_parser import DocxParser
from app.parsers.pdf_parser import PdfParser
from app.parsers.txt_parser import TxtParser
from app.parsers.xlsx_parser import XlsxParser


class ParserFactory:

    _parsers: list[BaseParser] = [
        TxtParser(),
        PdfParser(),
        DocxParser(),
        XlsxParser(),
    ]

    @classmethod
    def get_parser(
        cls,
        path: Path,
    ) -> BaseParser:

        for parser in cls._parsers:

            if parser.supports(path):
                return parser

        raise ValueError(
            f"지원하지 않는 파일 형식입니다. ({path.suffix})"
        )