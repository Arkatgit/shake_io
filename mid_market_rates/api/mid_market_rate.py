import logging
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from fastapi_pagination import Page, paginate
from fastapi_pagination.default import Params


from mid_market_rates.schemas import (
    ConversionRequestSchema,
    ConversionResponseSchema,
    CurrencySchema,
)
from mid_market_rates.views import ConversionView
from mid_market_rates.api.authentication import api_key_auth

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/convert",
    response_model=ConversionResponseSchema,
    status_code=201,
    name="Calculate converted amount and mid-market rate",
    dependencies=[Depends(api_key_auth)],
)
async def convert(convertion_payload: ConversionRequestSchema):
    """
    Endpoint Calculate converted amount and mid-market rate
    """
    try:
        converted = await ConversionView.create(convertion_payload)
    except Exception as e:
        message = "Error while performing convertion {}".format(str(convertion_payload))
        logger.warning(message)
        logger.warning(str(e))
        raise HTTPException(
            status_code=500,
            detail=message,
        )
    logger.info(f"The new converted figure is {str(converted)}")
    return converted


@router.get(
    "/history",
    response_model=Page[ConversionResponseSchema],
    status_code=200,
    name="List all previously made convertions",
    dependencies=[Depends(api_key_auth)],
)
async def history():
    """
    Retrieve list of all previously made conversions
    """
    try:
        convertions = await ConversionView.list()
    except Exception as e:
        message = "Error while retrieving convertion history: {}".format(str(e))
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=message)
    return paginate(convertions, Params())


@router.get(
    "/currencies",
    response_model=Page[CurrencySchema],
    status_code=200,
    name="List all supported currencies",
    dependencies=[Depends(api_key_auth)],
)
async def currencies():
    """
    Retrieve a dictionary containing all supported currencies
    """
    try:
        currencies = await ConversionView.list_currencies()
    except Exception as e:
        message = "Error while retrieving supported currencies: {}".format(str(e))
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=message)
    return paginate(currencies, Params())
