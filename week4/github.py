#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import scrapy


class github(scrapy.Spider):
    name = 'github'

    @property
    def start_urls(self):
        url = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url.format(i) for i in range(1, 5))

    def parse(self, response):
        for item in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            yield {
                'name': item.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('[^\d][ ]*(.+)'),
                'update_time': item.xpath('.//relative-time/@datetime').extract_first() }

