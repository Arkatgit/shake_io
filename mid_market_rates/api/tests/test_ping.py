import pytest
from httpx import AsyncClient

from main import app


class TestHealth:
    @pytest.mark.asyncio
    async def test_healthcheck(self):
        async with AsyncClient(app=app) as ac:
            response = await ac.get("http://mid-market-rate:8000/healthcheck")
        assert response.status_code == 200
