# -*- coding: utf-8 -*-
import scrapy


class EpexSpider(scrapy.Spider):
    name = 'epex'
    allowed_domains = ['www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/2019-05-25/DE']
    start_urls = ['http://www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/2019-05-25/DE/']

    def parse(self, response):
        pass
