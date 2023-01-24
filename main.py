import logging

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from mid_market_rates.db import database
from mid_market_rates.api import ping, mid_market_rate

logger = logging.getLogger(__name__)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(mid_market_rate.router, tags=["convertions"])

add_pagination(app)
