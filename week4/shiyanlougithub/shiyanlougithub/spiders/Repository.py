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
            item = ShiyanlougithubItem()
            item['name'] = repos.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('[^\d][ ]*(.+)')
            item['update_time'] = repos.xpath('.//relative-time/@datetime').extract_first()
            cbr_url = response.urljoin(repos.xpath('.//a[@itemprop="name codeRepository"]/@href').extract_first())
            request = scrapy.Request(cbr_url,callback=self.parse_cbr)
            request.meta['item'] = item
            yield request
    def parse_cbr(self,response):
        item = response.meta['item']
        item['commits'] = response.xpath('//ul[@class="numbers-summary"]/li[1]').xpath('./a/span/text()').re_first('\n\s*(.*)\n')
        item['branches'] = response.xpath('//ul[@class="numbers-summary"]/li[2]').xpath('./a/span/text()').re_first('\n\s*(.*)\n')
        item['releases'] = response.xpath('//ul[@class="numbers-summary"]/li[3]').xpath('./a/span/text()').re_first('\n\s*(.*)\n')
        yield item
            
