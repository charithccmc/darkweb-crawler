# -*- coding: utf-8 -*-
import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['dc']
    start_urls = ['http://dc/']

    def parse(self, response):
        pass
