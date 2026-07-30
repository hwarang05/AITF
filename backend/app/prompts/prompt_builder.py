"""
Prompt Builder

LLM에게 전달할 messages를 생성한다.

향후
- System Prompt
- Conversation Memory
- RAG 검색 결과
- Tool Calling 결과
- 사용자 프로필

등을 모두 여기에서 조합한다.
"""

from app.prompts.system import DEFAULT_SYSTEM_PROMPT


class PromptBuilder:
    """
    LLM Prompt 생성기
    """

    @staticmethod
    def build(user_message: str) -> list[dict[str, str]]:
        """
        LLM에게 전달할 messages를 생성한다.

        Args:
            user_message:
                사용자 입력

        Returns:
            Ollama/OpenAI Chat API 형식의 messages
        """

        messages: list[dict[str, str]] = []

        # -------------------------
        # System Prompt
        # -------------------------
        messages.append(
            {
                "role": "system",
                "content": DEFAULT_SYSTEM_PROMPT,
            }
        )

        # -------------------------
        # Conversation Memory
        # (향후 추가 예정)
        # -------------------------

        # -------------------------
        # RAG Context
        # (향후 추가 예정)
        # -------------------------

        # -------------------------
        # User Message
        # -------------------------
        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        return messages