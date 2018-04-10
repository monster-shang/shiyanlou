# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseImageItem

class CoursesimageSpider(scrapy.Spider):
    name = 'coursesimage'
    allowed_domains = ['shiyanlou.com']
    start_urls = ['http://shiyanlou.com/courses/']

    def parse(self, response):
        item = CourseImageItem()
        item['image_urls'] = response.css('div.course-img img::attr(src)').extract()
        yield item
