from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from duty.db.engine import get_async_engine

async_session_maker = async_sessionmaker(get_async_engine(), expire_on_commit=True)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
