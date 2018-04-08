# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class RepositorySpider(scrapy.Spider):
    name = 'Repository'
    allowed_domains = ['github.com']
    @property
    def start_urls(self):
        url = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url.format(i) for i in range(1,5))
    def parse(self, response):
        for repos in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            yield{'name': repos.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('[^\d][ ]*(.+)'),
                'update_time': repos.xpath('.//relative-time/@datetime').extract_first()}
            
