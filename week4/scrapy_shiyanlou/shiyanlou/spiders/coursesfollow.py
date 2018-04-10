# -*- coding: utf-8 -*-
import scrapy


class CoursesfollowSpider(scrapy.Spider):
    name = 'coursesfollow'
    allowed_domains = ['shiyanlou.com']
    start_urls = ['http://shiyanlou.com/courses/63']

    def parse(self, response):
        yield {
            'name': response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author': response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        }
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href'):
            yield response.follow(url, callback=self.parse)
