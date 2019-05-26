# -*- coding: utf-8 -*-
import scrapy


class EpexSpider(scrapy.Spider):
    name = 'EpeX'
    allowed_domains = ['www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/2019-05-25/DE']
    start_urls = ['http://www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/2019-05-25/DE/']
 
    def parse (self,response):
        date = response.xpath("id('content')/div/table/tbody/tr[1]/th[contains(@class, 'date')]/text()").get()
        price_list = response.xpath("id('content')/div/table/tbody/tr/th[contains(@class, 'date')]/text()").get()
        time = response.xpath("id('content')/div/table/tbody/tr/td[contains(@class, 'title')]/text()").get()
        x = response.xpath("id('quarter_auction_table_wrapp')/table/tbody/tr[contains(@class, 'hour')]/td/text()").get()
        y = response.xpath("id('tab_de')/table[2]/tbody/tr/td[contains(@class, 'title')]/../td/text()").get()
        z = response.xpath("id('tab_de')/table[1]/tbody/tr/td/text()").get()

        yield{'datum':date,'tijd':time,'prijzen':price_list}
