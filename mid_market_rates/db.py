from sqlalchemy import create_engine, MetaData
from databases import Database

from mid_market_rates.config import settings

engine = create_engine(settings.DATABASE_URL)

database = Database(settings.DATABASE_URL)

metadata = MetaData()


def create_tables():
    metadata.create_all()


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(metadata.create_all)
