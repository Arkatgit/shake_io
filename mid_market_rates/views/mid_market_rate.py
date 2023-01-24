import logging
import datetime


from mid_market_rates.models import Conversion, Currency
from mid_market_rates import services
from mid_market_rates.config import settings

logger = logging.getLogger(__name__)


class ConversionView:
    @staticmethod
    async def create(convertion_data):

        amount = convertion_data.amount
        from_currency = convertion_data.from_currency
        to_currency = convertion_data.to_currency
        try:
            converted_amount = await services.Scrapper.scrape_rate(
                settings.CURRENCY_CONVERTER_URL, amount, from_currency, to_currency
            )
            converted_amount = float(converted_amount)
            rate = (converted_amount / amount + 1) / 2

        except Exception as e:
            raise Exception(f"Error performing convertion:{str(e)}")

        new_convertion_data = {
            "converted_amount": converted_amount,
            "rate": rate,
            "amount": float(amount),
            "metadata": {
                "time_of_conversion": str(datetime.datetime.now()),
                "from_currency": from_currency,
                "to_currency": to_currency,
            },
        }
        new_convertion_id = await services.Database.save(
            Conversion, new_convertion_data
        )

        logger.error(f"The new convertions is {str(new_convertion_id)}")
        # new_convertion_data = {"id": new_convertion_id, **convertion_data}
        return new_convertion_data

    @staticmethod
    async def list():
        all_convertions = await services.Database.fetch_all(Conversion)
        return all_convertions

    @staticmethod
    async def list_currencies():
        # currencies hardly change so let's save the result
        # to save us the round trip for subsequent access

        # If it's not in the db then we fetch from the website
        currency = await services.Database.fetch_one(Currency)
        if not currency:
            supported_currencies = await services.Scrapper.scrape_currencies(
                settings.CURRENCY_CONVERTER_URL
            )
            values = [{"currency": val} for val in supported_currencies]
            await services.Database.save_many(Currency, values)

        currencies = await services.Database.fetch_all(Currency)
        return currencies
