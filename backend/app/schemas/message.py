"""
Message Schema
"""

from typing import Literal

from pydantic import BaseModel


Role = Literal[
    "system",
    "user",
    "assistant",
]


class ChatMessage(BaseModel):
    role: Role
    content: str