from fastapi import APIRouter, Depends

from mid_market_rates.schemas import HealthCheckSchema
from mid_market_rates.api.authentication import api_key_auth

router = APIRouter()


@router.get("/healthcheck", response_model=HealthCheckSchema, status_code=200,
dependencies=[Depends(api_key_auth)])
async def health():
    return {"status": "running!"}
