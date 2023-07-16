import pytest
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

from duty.user.models import User


@pytest.fixture()
def user_factory(db_session: AsyncSession, faker: Faker):
    async def factory(**kwargs) -> User:
        defaults = {"first_name": faker.first_name(), "last_name": faker.last_name(), "email": faker.email()}
        defaults.update(kwargs)

        user = User(**defaults)
        db_session.add(user)
        await db_session.commit()
        return user

    return factory
