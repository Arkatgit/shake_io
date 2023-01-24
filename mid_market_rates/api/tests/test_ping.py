import pytest
from httpx import AsyncClient

from main import app
from mid_market_rates.config import settings


class TestHealth:
    @pytest.mark.asyncio
    async def test_healthcheck(self):
        async with AsyncClient(app=app) as ac:
            response = await ac.get("http://mid-market-rate:8000/healthcheck",
                    headers={
                    "Authorization": f"Bearer {settings.API_KEY}",
                    "Content-Type": "application/json",
                })
        assert response.status_code == 200
