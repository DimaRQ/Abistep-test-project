import pytest
from httpx import ASGITransport, AsyncClient

from src.app.api import app


@pytest.mark.asyncio
async def test_create_user():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            url="/v1/users/",
            json={"name": "Dmitry", "email": "dmitry@gmail.com", "balance": 100},
        )
    json_data = response.json()
    assert response.status_code == 201
    assert type(json_data.get("id")) is int
    assert json_data.get("name") == "Dmitry"
    assert json_data.get("email") == "dmitry@gmail.com"
    assert float(json_data.get("balance")) == 100.0


@pytest.mark.asyncio
async def test_get_users():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get(url="/v1/users/")
    json_data = response.json()
    assert response.status_code == 200
    assert type(json_data) is list
    assert len(json_data) >= 1
