# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem


class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['shiyanlou.com']
    @property
    def start_urls(self):
        url = 'https://www.shiyanlou.com/user/{}'
        return (url.format(i) for i in range(524800,525000,10))

    def parse(self, response):
        yield UserItem({'name':response.css('span.username::text').extract_first(),'type':response.css('img.user-icon::attr(title)').extract_first(default='普通用户'),'status':response.xpath('//div[@class="userinfo-banner-status"]/span[1]/text()').extract_first(),'job':response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),'school':response.xpath('//div[@class="userinfo-banner-status"]/a/text()').extract_first(),'join_date':response.css('span.join-date::text').extract_first(),'level':response.css('span.user-level::text').extract_first(),'learn_courses_num':response.css('span.latest-learn-num::text').extract_first()})
        
