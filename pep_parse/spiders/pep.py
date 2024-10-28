import re

import scrapy

from pep_parse.constants import (
    ALLOWED_DOMAINS_PEP,
    START_URLS_PEP,
    NAME_SPIDER_PEP,
)
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Парсер документов PEP."""

    name = NAME_SPIDER_PEP
    allowed_domains = ALLOWED_DOMAINS_PEP
    start_urls = START_URLS_PEP

    def parse(self, response):
        """Сбор ссылок на документы PEP."""
        all_pep_links = response.css('a.pep::attr(href)')
        for pep_link in all_pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Сбор информации о номерах, именах и статусах документов PEP."""
        pattern = r'^PEP (?P<number>\d+) . (?P<name>.+)\s\|\s.+$'
        title = response.css('title::text').get()
        number_name_match = re.match(pattern, title)
        data = {
            'number': number_name_match.group('number'),
            'name': number_name_match.group('name'),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }
        yield PepParseItem(data)
