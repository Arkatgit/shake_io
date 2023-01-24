import logging
from mid_market_rates.db import database

logger = logging.getLogger(__name__)


class Database:
    @staticmethod
    async def save(model, values):
        query = model.insert().values(**values)
        new_record = await database.execute(query)
        logger.info(
            f"Successfully inserted new" f"{str(model)} with values {str(values)}"
        )
        return new_record

    @staticmethod
    async def save_many(model, values):
        query = model.insert()
        result = await database.execute_many(query=query, values=values)
        return result

    @staticmethod
    async def update(model, values):
        query = model.update().values(**values)
        await database.execute(query)

    @staticmethod
    async def fetch_all(model):
        query = model.select()
        rows = await database.fetch_all(query=query)
        return rows

    @staticmethod
    async def fetch_one(model):
        query = model.select()
        row = await database.fetch_one(query=query)
        return row
