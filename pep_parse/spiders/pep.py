import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        all_pep_links = response.css('a.pep::attr(href)')
        for pep_link in all_pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pattern = r'^PEP (?P<number>\d+).{3}(?P<name>\w.+)$'
        title = response.css('h1.page-title::text').get()
        number_name_match = re.match(pattern, title)
        number = int(number_name_match.group('number'))
        name = number_name_match.group('name')
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
