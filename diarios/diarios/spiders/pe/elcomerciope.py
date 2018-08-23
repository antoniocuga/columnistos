# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from diarios.items import DiariosItem


class ElcomerciopeSpider(scrapy.Spider):
    name = 'elcomerciope'
    allowed_domains = ['elcomercio.pe']
    start_urls = ['https://elcomercio.pe/opinion']

    def parse(self, response):
        """
        @url https://elcomercio.pe/opinion
        @returns items 1 14
        @returns requests 0 0
        @scrapes author title url
        """
        selectors = response.xpath('//div[@class="flows-grid"]//div[@class="flow-1x1"]')
        
        for selector in selectors:
            yield self.parse_article(selector, response)

    def parse_article(self, selector, response):
        loader = ItemLoader(DiariosItem(), selector=selector)

        loader.add_xpath('title', './/h2//text()')
        loader.add_xpath('author', './/span[@class="flow-author"]/text()')
        loader.add_xpath('url', './/h2//@href')
        return loader.load_item()
