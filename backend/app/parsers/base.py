"""
Base Parser

모든 문서 Parser의 부모 클래스
"""

from abc import ABC
from abc import abstractmethod
from pathlib import Path


class BaseParser(ABC):
    """
    Parser Base Class
    """

    @abstractmethod
    def supports(
        self,
        path: Path,
    ) -> bool:
        """
        해당 파일을 처리 가능한지 확인
        """
        raise NotImplementedError

    @abstractmethod
    def parse(
        self,
        path: Path,
    ) -> str:
        """
        파일을 문자열로 변환
        """
        raise NotImplementedError