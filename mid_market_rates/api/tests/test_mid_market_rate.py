from unittest import mock

import pytest
from httpx import AsyncClient

from main import app
from mid_market_rates.config import settings


class TestMidMarketRate:
    @mock.patch(
        "mid_market_rates.services.Database.save_many",
        side_effect=mock.AsyncMock(return_value=True),
    )
    @mock.patch(
        "mid_market_rates.services.Database.fetch_all",
        side_effect=mock.AsyncMock(
            return_value=[{"currency": "GHS"}, {"currency": "USD"}]
        ),
    )
    @mock.patch(
        "mid_market_rates.services.Database.fetch_one",
        side_effect=mock.AsyncMock(return_value=[{"currency": "USD"}]),
    )
    @pytest.mark.asyncio
    async def test_currencies(self, one, all, many):
        async with AsyncClient(app=app) as ac:
            response = await ac.get(
                "http://mid-market-rate:8000/currencies",
                headers={
                    "Authorization": f"Bearer {settings.API_KEY}",
                    "Content-Type": "application/json",
                },
            )
        assert response.json() == {
            "items": [{"currency": "GHS"}, {"currency": "USD"}],
            "total": 2,
            "page": 1,
            "size": 50,
        }

    @mock.patch(
        "mid_market_rates.services.Database.fetch_all",
        side_effect=mock.AsyncMock(return_value=[]),
    )
    @pytest.mark.asyncio
    async def test_history(self, mock_save_db):
        async with AsyncClient(app=app) as ac:
            response = await ac.get(
                "http://mid-market-rate:8000/history",
                headers={
                    "Authorization": f"Bearer {settings.API_KEY}",
                    "Content-Type": "application/json",
                },
            )
        return response.status_code == 200
