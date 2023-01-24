from sqlalchemy import (
    Column,
    String,
    Float,
    DateTime,
    Table,
    text,
    Boolean,
)

from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy_jsonfield


from mid_market_rates.db import metadata


Conversion = Table(
    "conversions",
    metadata,
    Column(
        "id",
        UUID(),
        primary_key=True,
        index=True,
        server_default=text("gen_random_uuid()"),
    ),
    Column("amount", Float),
    Column("converted_amount", Float),
    Column("rate", Float),
    Column(
        "metadata",
        sqlalchemy_jsonfield.JSONField(
            enforce_string=False,
            enforce_unicode=False,
        ),
        nullable=False,
    ),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
)

Currency = Table(
    "currencies",
    metadata,
    Column(
        "id",
        UUID(),
        primary_key=True,
        index=True,
        server_default=text("gen_random_uuid()"),
    ),
    Column("currency", String(3)),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
)
