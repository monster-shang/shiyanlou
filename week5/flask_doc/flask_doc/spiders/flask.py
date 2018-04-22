# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from flask_doc.items import FlaskDocItem
class FlaskSpider(CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/0.12/']
    rules = (
        Rule(LinkExtractor(allow=r'http://flask.pocoo.org/docs/0.12/.*'), callback='parse_item', follow=True),)
    def parse_item(self, response):
        item = FlaskDocItem()
        item['url'] = response.url
        item['text'] = response.xpath('//text()').extract()
        yield item
