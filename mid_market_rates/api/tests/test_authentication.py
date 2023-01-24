from unittest import mock

import pytest
from httpx import AsyncClient

from main import app
from mid_market_rates.config import settings



class TestAuthentication:
    @pytest.mark.asyncio
    async def test_history_without_auth(self):
        async with AsyncClient(app=app) as ac:
            response = await ac.get("http://mid-market-rate:8000/history")
        assert response.status_code == 401

    @pytest.mark.asyncio
    async def test_history_with_wrong_auth_key(self):
        async with AsyncClient(app=app) as ac:
            response = await ac.get(
                "http://mid-market-rate:8000/history",
                headers={
                    "Authorization": "Bearer 004cec70-142d-4535-961b-4919a5d58ad3xxxxxxxx",
                    'Content-Type': 'application/json'
                },
            )
        assert response.status_code == 401
    
    @mock.patch(
        "mid_market_rates.services.Database.fetch_all", side_effect=mock.AsyncMock(return_value=[])
    )
    @pytest.mark.asyncio
    async def test_history_with_correct_auth_key(self, mock_save_db):
        async with AsyncClient(app=app) as ac:
            response = await ac.get(
                "http://mid-market-rate:8000/history",
                headers={"Authorization": f"Bearer {settings.API_KEY}",
                'Content-Type': 'application/json'},
            )
        assert response.status_code == 200
