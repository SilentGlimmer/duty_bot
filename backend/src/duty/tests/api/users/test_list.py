import pytest
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture()
def url(app):
    return app.url_path_for("list_users")


async def test_empty(db_session: AsyncSession, url, client):
    resp = client.get(url)
    assert resp.json() == {"items": [], "next_page": None, "previous_page": None}


async def test_ok(db_session, url, client, user_factory):
    user = await user_factory()

    resp = client.get(url)
    assert resp.json() == {
        "items": [{"first_name": user.first_name, "id": user.id, "last_name": user.last_name}],
        "next_page": None,
        "previous_page": None,
    }
