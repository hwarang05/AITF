"""
Application Logger
"""

import sys
from pathlib import Path

from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(
    exist_ok=True,
)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    enqueue=True,
)

logger.add(
    LOG_DIR / "app.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="DEBUG",
    enqueue=True,
    encoding="utf-8",
)

__all__ = [
    "logger",
]