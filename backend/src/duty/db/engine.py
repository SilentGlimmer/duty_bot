from sqlalchemy import Engine, Pool, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from duty.settings import get_settings


def get_engine(poolclass: type[Pool] | None = None) -> Engine:
    settings = get_settings()
    return create_engine(str(settings.pg_dsn), poolclass=poolclass, echo=settings.db_session_echo)


def get_async_engine() -> AsyncEngine:
    settings = get_settings()
    return create_async_engine(str(settings.pg_dsn), echo=settings.db_session_echo)
