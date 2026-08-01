"""
Dependency Injection

FastAPI Dependency를 관리한다.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.providers.provider_factory import (
    get_provider,
)
from app.providers.embedding_provider_factory import (
    get_embedding_provider,
)
from app.providers.vector_provider_factory import (
    get_vector_provider,
)

from app.services.chat_service import ChatService
from app.services.chunk_service import ChunkService
from app.services.context_service import ContextService
from app.services.conversation_service import ConversationService
from app.services.embedding_service import EmbeddingService
from app.services.file_service import FileService
from app.services.indexing_service import IndexingService
from app.services.llm_service import LLMService
from app.services.message_service import MessageService
from app.services.profile_service import ProfileService
from app.services.rag_service import RagService
from app.services.summary_service import SummaryService
from app.services.vector_service import VectorService


# --------------------------------------------------
# LLM Service
# --------------------------------------------------
def get_llm_service() -> LLMService:
    """
    LLMService 생성
    """

    provider = get_provider()

    return LLMService(provider)


# --------------------------------------------------
# Embedding Service
# --------------------------------------------------
def get_embedding_service() -> EmbeddingService:
    """
    EmbeddingService 생성
    """

    provider = get_embedding_provider()

    return EmbeddingService(provider)


# --------------------------------------------------
# Vector Service
# --------------------------------------------------
def get_vector_service() -> VectorService:
    """
    VectorService 생성
    """

    provider = get_vector_provider()

    return VectorService(provider)


# --------------------------------------------------
# Conversation Service
# --------------------------------------------------
def get_conversation_service(
    db: Session = Depends(get_db),
) -> ConversationService:

    return ConversationService(db)


# --------------------------------------------------
# Message Service
# --------------------------------------------------
def get_message_service(
    db: Session = Depends(get_db),
) -> MessageService:

    return MessageService(db)


# --------------------------------------------------
# File Service
# --------------------------------------------------
def get_file_service(
    db: Session = Depends(get_db),
) -> FileService:

    return FileService(db)


# --------------------------------------------------
# Chunk Service
# --------------------------------------------------
def get_chunk_service(
    db: Session = Depends(get_db),
) -> ChunkService:

    return ChunkService(db)


# --------------------------------------------------
# Indexing Service
# --------------------------------------------------
def get_indexing_service(
    chunk_service: ChunkService = Depends(
        get_chunk_service,
    ),
) -> IndexingService:

    return IndexingService(
        chunk_service=chunk_service,
    )


# --------------------------------------------------
# Rag Service
# --------------------------------------------------
def get_rag_service(
    embedding_service: EmbeddingService = Depends(
        get_embedding_service,
    ),
    vector_service: VectorService = Depends(
        get_vector_service,
    ),
) -> RagService:

    return RagService(
        embedding_service=embedding_service,
        vector_service=vector_service,
    )


# --------------------------------------------------
# Summary Service
# --------------------------------------------------
def get_summary_service() -> SummaryService:

    return SummaryService()


# --------------------------------------------------
# Profile Service
# --------------------------------------------------
def get_profile_service() -> ProfileService:

    return ProfileService()


# --------------------------------------------------
# Context Service
# --------------------------------------------------
def get_context_service(
    message_service: MessageService = Depends(
        get_message_service,
    ),
    rag_service: RagService = Depends(
        get_rag_service,
    ),
    summary_service: SummaryService = Depends(
        get_summary_service,
    ),
    profile_service: ProfileService = Depends(
        get_profile_service,
    ),
) -> ContextService:

    return ContextService(
        message_service=message_service,
        rag_service=rag_service,
        summary_service=summary_service,
        profile_service=profile_service,
    )


# --------------------------------------------------
# Chat Service
# --------------------------------------------------
def get_chat_service(
    conversation_service: ConversationService = Depends(
        get_conversation_service,
    ),
    message_service: MessageService = Depends(
        get_message_service,
    ),
    llm_service: LLMService = Depends(
        get_llm_service,
    ),
    context_service: ContextService = Depends(
        get_context_service,
    ),
) -> ChatService:

    return ChatService(
        conversation_service=conversation_service,
        message_service=message_service,
        llm_service=llm_service,
        context_service=context_service,
    )