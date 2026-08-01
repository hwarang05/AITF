"""
ChromaDB Provider
"""

from urllib.parse import urlparse

import chromadb

from app.core.config import settings
from app.providers.vector_base import (
    BaseVectorProvider,
)


class ChromaDBProvider(BaseVectorProvider):
    """
    ChromaDB Provider
    """

    COLLECTION_NAME = "documents"

    def __init__(self):

        parsed = urlparse(
            settings.VECTOR_DB_URL,
        )

        host = parsed.hostname or "localhost"
        port = parsed.port or 8000

        self.client = chromadb.HttpClient(
            host=host,
            port=port,
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=self.COLLECTION_NAME,
            )
        )

    async def upsert(
        self,
        *,
        ids: list[str],
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
    ) -> None:

        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    async def search(
        self,
        *,
        embedding: list[float],
        limit: int = 5,
    ) -> list[dict]:

        result = self.collection.query(
            query_embeddings=[embedding],
            n_results=limit,
        )

        ids = result.get("ids", [[]])[0]
        documents = result.get("documents", [[]])[0]
        metadatas = result.get("metadatas", [[]])[0]
        distances = result.get("distances", [[]])[0]

        results: list[dict] = []

        for chunk_id, document, metadata, distance in zip(
            ids,
            documents,
            metadatas,
            distances,
        ):
            results.append(
                {
                    "id": int(chunk_id),
                    "content": document,
                    "metadata": metadata or {},
                    "distance": distance,
                }
            )

        return results

    async def delete(
        self,
        *,
        ids: list[str],
    ) -> None:

        self.collection.delete(
            ids=ids,
        )