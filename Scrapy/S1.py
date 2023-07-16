# -*- coding: utf-8 -*-
import scrapy

class Link(scrapy.Item):
    link= scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'link_lists'
    allowed_domains = ['https://www.flipkart.com/']
    start_urls = ['https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page={}'.format(page) for page in range(1, 11)]


    def parse(self, response):
        xpath = '//div[@class="_1YokD2 _3Mn1Gg"]//a[@class="_1fQZEK"]/@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://www.flipkart.com' + s.get()
            yield l
    
