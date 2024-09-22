import asyncio
import re

from bs4 import BeautifulSoup as bs
from httpx import AsyncClient

from database.manager import DBManager
from database.models import URLs


class Scrape:
    """
    Scrape data from urls.
    """

    db = DBManager(URLs)

    def _get_urls(self) -> list[str]:
        """Return all urls from database."""

        return [obj.url for obj in self.db.get_all()]

    @staticmethod
    async def _create_requests(urls: list) -> list[str]:
        """Return lis of html code of all urls."""

        html_codes = []

        async with AsyncClient() as client:
            tasks = [asyncio.create_task(client.get(url)) for url in urls]
            for task in asyncio.as_completed(tasks):
                html = await task
                html_codes.append(html)
        return html_codes

    @staticmethod
    def _get_soups(html_codes: list) -> list[bs]:
        """Return list of bs4 objects."""

        soups = [bs(html, "html.parser") for html in html_codes]
        return soups

    @staticmethod
    def _get_title_and_quantity(soup: bs) -> list[list[str]]:
        cards = soup.find_all(attrs={"class": "product-item"})
        received_data = list()
        for card in cards:
            try:
                name = card.find(attrs={"class": "product-item-title"}).text.strip()
            except AttributeError:
                name = "None"
            try:
                quantity = card.find(
                    attrs={"class": "product-item-quantity"}
                ).text.strip()
                quantity = re.findall(r"\d+", quantity)
            except AttributeError:
                quantity = "0"
            received_data.append([name, *quantity])
        return received_data

    def get_data_from_urls(self) -> list[list[str]]:
        urls = self._get_urls()
        html_codes = asyncio.run(self._create_requests(urls))
        soups = self._get_soups(html_codes)
        data = [self._get_title_and_quantity(soup) for soup in soups]
        data = sum(data, [])
        return data
