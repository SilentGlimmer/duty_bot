import asyncio
from typing import AsyncGenerator

import pytest
from alembic import command as alembic_command
from alembic.config import Config
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from sqlalchemy_utils import create_database, database_exists, drop_database

from duty.api.dependencies import get_async_session_maker
from duty.settings import BASE_DIR

__all__ = [
    "run_db_migrations",
    "db_session",
]


@pytest.fixture()
def run_db_migrations(settings):
    config = Config(BASE_DIR / "alembic.ini")
    db_url = str(settings.pg_dsn)

    if database_exists(db_url):
        drop_database(db_url)

    create_database(db_url)
    alembic_command.upgrade(config, "head")
    yield
    alembic_command.downgrade(config, "base")


@pytest.fixture()
async def db_session(run_db_migrations: None) -> AsyncGenerator[AsyncSession, None]:
    session = async_scoped_session(get_async_session_maker(), scopefunc=asyncio.current_task)()
    yield session
    await session.rollback()
    await session.close()
