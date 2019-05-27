# -*- coding: utf-8 -*-
import scrapy
import datetime

class EpexSpider(scrapy.Spider):
    name = 'EpeX'
    allowed_domains = ['www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/2019-05-25/DE']
    start_urls = ["https://www.epexspot.com/en/market-data/intradaycontinuous/intraday-table/" + str(datetime.date.today())+"/DE"]
    features=[Low, High, Last(€/MWh), Weight_Avg(€/MWh), Index(€/MWh), ID3_Price(€/MWh), ID1_Price(€/MWh), BuyVol(MW), SellVol(MW), Low2(€/MWh), High2(€/MWh), Last2(€/MWh), WeightAvg2(€/MWh), Index2(€/MWh), ID3Price2(€/MWh), ID1Price2(€/MWh), BuyVol2(MW) 	SellVol2]
    
    def parse (self,response):
        for i,feat in enumerate(features):
            date = response.xpath('//td[3]').extract()
            feat = response.xpath('//'+str(td[i+4])).extract()