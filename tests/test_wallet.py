import uuid

import pytest
from httpx import ASGITransport, AsyncClient

from src.app.api import app


@pytest.mark.asyncio
async def test_wallet_transfer():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        email1 = f"user1_{uuid.uuid4()}@test.com"
        email2 = f"user2_{uuid.uuid4()}@test.com"

        resp1 = await client.post(
            url="/v1/users/",
            json={"name": "Dmitry", "email": email1, "balance": "100.00"},
        )
        assert resp1.status_code == 201
        user1 = resp1.json()

        resp2 = await client.post(
            url="/v1/users/",
            json={"name": "Anton", "email": email2, "balance": "50.00"},
        )
        assert resp2.status_code == 201
        user2 = resp2.json()

        resp_transfer = await client.post(
            url="/v1/wallet/transfer/",
            json={
                "from_user_id": user1["id"],
                "to_user_id": user2["id"],
                "amount": "20.00",
            },
        )
        assert resp_transfer.status_code == 200
        assert resp_transfer.json() == {"status": "ok"}

        resp_users = await client.get("/v1/users/")
        assert resp_users.status_code == 200
        users = {u["id"]: u for u in resp_users.json()}

        assert float(users[user1["id"]]["balance"]) == 80.00
        assert float(users[user2["id"]]["balance"]) == 70.00
