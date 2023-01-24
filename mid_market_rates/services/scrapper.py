import logging
import json

from bs4 import BeautifulSoup
import aiohttp
from arsenic import get_session, browsers, services

from mid_market_rates.config import settings

logger = logging.getLogger(__name__)


class Scrapper:
    @staticmethod
    def set_up_service_and_browser():
        service = services.Chromedriver(binary=settings.CHROME_DRIVER_URL)
        browser = browsers.Chrome()
        browser.capabilities = {
            "goog:chromeOptions": {
                "args": [
                    "--headless",
                    "--disable-gpu",
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                ]
            }
        }
        return service, browser

    @staticmethod
    async def scrape_rate(url, amount, from_currency, to_currency):
        service, browser = Scrapper.set_up_service_and_browser()
        async with get_session(service, browser) as session:
            url = f"{url}{from_currency.lower()}-to-{to_currency.lower()}-rate?amount={amount}"
            await session.get(url)
            converted = await session.get_element("#target-input")
            value = await converted.get_attribute("value")
            return value

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
