# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:36:22 2019

@author: Kwabena Ofori
"""

import scrapy 

class Epexscraper(scrapy.Spider):
    name=EPEX_scraper 
    allowed_domains=[www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/2019-05-25/DE]
    start_urls = (
            https://www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/2019-05-25/DE
    )
    
    def parse (self,response):
        date = response.xpath("id('content')/div/table/tbody/tr[1]/th[contains(@class, 'date')]/text()").get()
        price_list = response.xpath("id('content')/div/table/tbody/tr/th[contains(@class, 'date')]/text()").get()
        time = response.xpath("id('content')/div/table/tbody/tr/td[contains(@class, 'title')]/text()").get()
        x = response.xpath("id('quarter_auction_table_wrapp')/table/tbody/tr[contains(@class, 'hour')]/td/text()").get()
        y = response.xpath("id('tab_de')/table[2]/tbody/tr/td[contains(@class, 'title')]/../td/text()").get()
        z = response.xpath("id('tab_de')/table[1]/tbody/tr/td/text()").get()

        yield{'datum':date,'tijd':time,'prijzen':price_list}