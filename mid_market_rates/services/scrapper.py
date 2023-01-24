import logging
import json

from bs4 import BeautifulSoup
import aiohttp

from mid_market_rates.config import settings

logger = logging.getLogger(__name__)


class Scrapper:
 
    @staticmethod
    async def scrape_rate(url, amount, from_currency, to_currency):
        async with aiohttp.ClientSession() as session:
            url = f"{url}{from_currency.lower()}-to-{to_currency.lower()}-rate?amount={amount}"
            async with session.get(url) as resp:
                response = await resp.read()
            converted = BeautifulSoup(response.decode('utf-8'), 'html.parser').find('label', attrs={'for': "target-input"}).findNext('div').text
            return float(converted[0: converted.find(' ')].replace(',', '') ) #strip currency code 
    
    @staticmethod
    async def scrape_currencies(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(settings.CURRENCY_CONVERTER_URL) as resp:
                response = await resp.read()
            return [
                currency["code"]
                for currency in json.loads(
                    list(
                        BeautifulSoup(response.decode("utf-8"), "html.parser").find(
                            "script", attrs={"id": "__NEXT_DATA__"}
                        )
                    )[0]
                )["props"]["pageProps"]["model"]["currencies"]
            ]
