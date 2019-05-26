# -*- coding: utf-8 -*-
import scrapy


class EpexScraperSpider(scrapy.Spider):
    name = 'EPEX_scraper'
    allowed_domains = ['https://www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/2019-05-25/DE']
    start_urls = ['http://https://www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/2019-05-25/DE/']

    def parse(self, response):
        pass
