"""
Database

SQLAlchemy Engine 및 Session을 관리한다.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


# -------------------------
# Database Engine
# -------------------------
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
)


# -------------------------
# Session Factory
# -------------------------
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# -------------------------
# FastAPI Dependency
# -------------------------
def get_db() -> Generator[Session, None, None]:
    """
    Database Session Dependency
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()