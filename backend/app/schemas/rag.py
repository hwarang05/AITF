"""
RAG Schema

RAG 검색 결과 모델
"""

from pydantic import BaseModel
from pydantic import Field


class RagResult(BaseModel):
    """
    RAG 검색 결과
    """

    chunk_id: str = Field(
        description="Chunk ID",
    )

    content: str = Field(
        description="Chunk 내용",
    )

    distance: float = Field(
        description="Vector Distance",
    )

    metadata: dict = Field(
        default_factory=dict,
        description="메타데이터",
    )