import datetime
from uuid import UUID
from typing import Any

from pydantic import BaseModel, Field, Json


class MetaDataSchema(BaseModel):
    time_of_conversion: str
    from_currency: str
    to_currency: str


class ConversionResponseSchema(BaseModel):
    converted_amount: float
    rate: float
    metadata: MetaDataSchema


class ConversionRequestSchema(BaseModel):
    amount: float
    from_currency: str = Field(title="The source currency", max_length=3)
    to_currency: str = Field(title="The target currency", max_length=3)


class CurrencySchema(BaseModel):
    currency: str
