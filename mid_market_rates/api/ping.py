from fastapi import APIRouter

from mid_market_rates.schemas import HealthCheckSchema

router = APIRouter()


@router.get("/healthcheck", response_model=HealthCheckSchema, status_code=200)
async def health():
    return {"status": "running!"}
