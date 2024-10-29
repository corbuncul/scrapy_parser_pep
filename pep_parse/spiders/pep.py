import re

import scrapy

from pep_parse.constants import (
    ALLOWED_DOMAINS_PEP,
    FIELD_NAME,
    FIELD_NUMBER,
    FIELD_STATUS,
    NAME_SPIDER_PEP,
    PATTERN,
    START_URLS_PEP,
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
        title = response.css('title::text').get()
        number_name_match = re.match(PATTERN, title)
        data = {
            FIELD_NUMBER: number_name_match.group(FIELD_NUMBER),
            FIELD_NAME: number_name_match.group(FIELD_NAME),
            FIELD_STATUS: response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }
        yield PepParseItem(data)
