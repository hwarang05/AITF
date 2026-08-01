"""
Chat API

사용자의 질문을 받아
AI와 대화를 수행한다.
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import StreamingResponse

from app.core.dependencies import get_chat_service
from app.core.response import response
from app.dependencies.auth import get_current_active_user
from app.models.user import User
from app.schemas.chat import (
    ChatRequest,
    ConversationDetailResponse,
    ConversationUpdateRequest,
)
from app.schemas.common import ApiResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


# =============================================================================
# Chat
# =============================================================================


@router.post(
    "",
    response_model=ApiResponse,
)
async def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):

    result = await service.chat(
        user=current_user,
        message=request.message,
        conversation_id=request.conversation_id,
    )

    return response.success(
        message="AI 응답 성공",
        data=result,
    )


@router.post("/stream")
async def stream_chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):

    async def event_stream():

        async for token in service.stream_chat(
            user=current_user,
            message=request.message,
            conversation_id=request.conversation_id,
        ):
            yield token

    return StreamingResponse(
        event_stream(),
        media_type="text/plain; charset=utf-8",
    )


# =============================================================================
# Conversation
# =============================================================================


@router.get(
    "/conversations",
    response_model=ApiResponse,
)
def get_conversations(
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):

    conversations = service.get_conversations(
        user=current_user,
    )

    return response.success(
        message="대화 목록 조회 성공",
        data=conversations,
    )


@router.get(
    "/conversations/{conversation_id}",
    response_model=ApiResponse,
)
def get_conversation(
    conversation_id: int,
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):

    conversation = service.get_conversation(
        conversation_id=conversation_id,
        user=current_user,
    )

    return response.success(
        message="대화 조회 성공",
        data=ConversationDetailResponse.model_validate(
            conversation,
        ),
    )


@router.patch(
    "/conversations/{conversation_id}",
    response_model=ApiResponse,
)
def update_conversation_title(
    conversation_id: int,
    request: ConversationUpdateRequest,
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):

    conversation = service.update_conversation_title(
        conversation_id=conversation_id,
        title=request.title,
        user=current_user,
    )

    return response.success(
        message="대화 제목 변경 성공",
        data=conversation,
    )


@router.delete(
    "/conversations/{conversation_id}",
    response_model=ApiResponse,
)
def delete_conversation(
    conversation_id: int,
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):

    service.delete_conversation(
        conversation_id=conversation_id,
        user=current_user,
    )

    return response.success(
        message="대화 삭제 성공",
    )