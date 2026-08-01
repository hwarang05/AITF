"""
Conversation API

대화 목록 및 상세 조회를 관리한다.
"""

from fastapi import APIRouter
from fastapi import Depends

from app.core.dependencies import get_chat_service
from app.core.response import response
from app.dependencies.auth import get_current_active_user
from app.models.user import User
from app.schemas.chat import ConversationUpdateRequest
from app.schemas.common import ApiResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/conversations",
    tags=["Conversation"],
)


@router.get(
    "",
    response_model=ApiResponse,
)
def get_conversations(
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):
    """
    사용자 대화 목록 조회
    """

    result = service.get_conversations(
        user=current_user,
    )

    return response.success(
        message="대화 목록 조회 성공",
        data=result,
    )


@router.get(
    "/{conversation_id}",
    response_model=ApiResponse,
)
def get_conversation(
    conversation_id: int,
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):
    """
    대화 상세 조회
    """

    result = service.get_conversation(
        conversation_id=conversation_id,
        user=current_user,
    )

    return response.success(
        message="대화 조회 성공",
        data=result,
    )


@router.patch(
    "/{conversation_id}",
    response_model=ApiResponse,
)
def update_conversation(
    conversation_id: int,
    request: ConversationUpdateRequest,
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):
    """
    대화 제목 변경
    """

    result = service.update_conversation_title(
        conversation_id=conversation_id,
        title=request.title,
        user=current_user,
    )

    return response.success(
        message="대화 제목 변경 성공",
        data=result,
    )


@router.delete(
    "/{conversation_id}",
    response_model=ApiResponse,
)
def delete_conversation(
    conversation_id: int,
    current_user: User = Depends(get_current_active_user),
    service: ChatService = Depends(get_chat_service),
):
    """
    대화 삭제
    """

    service.delete_conversation(
        conversation_id=conversation_id,
        user=current_user,
    )

    return response.success(
        message="대화 삭제 성공",
    )