"""
Chat API

사용자의 질문을 받아
LLM Service로 전달하는 API
"""

from fastapi import APIRouter, Depends

from app.core.dependencies import get_llm_service
from app.core.response import response
from app.schemas.chat import ChatRequest
from app.schemas.common import ApiResponse
from app.services.llm_service import LLMService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ApiResponse,
)
async def chat(
    request: ChatRequest,
    service: LLMService = Depends(get_llm_service),
):
    """
    사용자 질문을 받아 AI에게 전달한다.
    """

    # AI에게 질문을 전달한다.
    answer = await service.chat(request.message)

    # AI의 답변을 사용자에게 반환한다.
    return response.success(
        message="AI 응답 성공",
        data={
            "question": request.message,
            "answer": answer,
        },
    )