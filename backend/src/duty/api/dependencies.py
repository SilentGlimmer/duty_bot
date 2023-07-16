from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from duty.db.engine import get_async_engine


def get_async_session_maker() -> async_sessionmaker:
    return async_sessionmaker(get_async_engine(), expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session_maker = get_async_session_maker()
    async with session_maker() as session:
        yield session
