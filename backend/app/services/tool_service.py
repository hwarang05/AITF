"""
Tool Service

LLM이 사용할 Tool을 관리한다.
"""

from collections.abc import Callable


class ToolService:
    """
    Tool Service
    """

    def __init__(self):
        self._tools: dict[str, Callable] = {}

    # --------------------------------------------------
    # Tool 등록
    # --------------------------------------------------

    def register(
        self,
        name: str,
        tool: Callable,
    ) -> None:
        """
        Tool 등록
        """

        self._tools[name] = tool

    # --------------------------------------------------
    # Tool 조회
    # --------------------------------------------------

    def get(
        self,
        name: str,
    ) -> Callable | None:
        """
        Tool 반환
        """

        return self._tools.get(name)

    # --------------------------------------------------
    # Tool 목록
    # --------------------------------------------------

    def get_tools(
        self,
    ) -> dict[str, Callable]:
        """
        등록된 Tool 반환
        """

        return self._tools.copy()

    # --------------------------------------------------
    # Tool 존재 여부
    # --------------------------------------------------

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._tools

    # --------------------------------------------------
    # Tool 삭제
    # --------------------------------------------------

    def unregister(
        self,
        name: str,
    ) -> None:

        self._tools.pop(name, None)

    # --------------------------------------------------
    # 전체 삭제
    # --------------------------------------------------

    def clear(
        self,
    ) -> None:

        self._tools.clear()