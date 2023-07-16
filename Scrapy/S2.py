# -*- coding: utf-8 -*-
import scrapy
import re

class Products(scrapy.Item):
    name= scrapy.Field()
    price= scrapy.Field()
    discount= scrapy.Field()
    avgRating= scrapy.Field()
    ratingCount= scrapy.Field()
    reviewCount= scrapy.Field()
    memoryDetail= scrapy.Field()
    screenDimention= scrapy.Field()
    lensDetail= scrapy.Field()
    batteryCapacity= scrapy.Field()
    processor= scrapy.Field()
    warranty= scrapy.Field()
    color= scrapy.Field()
    RAM= scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['https://www.flipkart.com/']
    try:
        with open("link_lists.csv", "rt") as f:
            lines = f.readlines () [ 1 :101 ]
            start_urls = [ url.strip () for url in lines ]
    except:
        start_urls = []

    def parse(self, response):
        p = Products()

        name_xpath= '//h1/span/text()[1]'
        p['name']= response.xpath(name_xpath).getall()
        price_xpath ='//div[@class="CEmiEU"]/div//div[1]/text()'
        p['price']= response.xpath(price_xpath).getall()
        discount_xpath ='//div[@class="CEmiEU"]/div//div[3]/span/text()'
        p['discount']= response.xpath(discount_xpath).getall()
        avgRating_xpath ='//div[@class="gUuXy- _16VRIQ"]//span[1]/div/text()'
        p['avgRating']= response.xpath(avgRating_xpath).getall()
        ratingCount_xpath ='//div[@class="gUuXy- _16VRIQ"]//span[2]/span/span[1]/text()'
        p['ratingCount']= response.xpath(ratingCount_xpath).getall()[0].replace('\xa0','')
        reviewCount_xpath ='//div[@class="gUuXy- _16VRIQ"]//span[2]/span/span[3]/text()'
        p['reviewCount']= response.xpath(reviewCount_xpath).getall()[0].replace('\xa0','')
        memoryDetail_xpath ='//div[re:test(text(),"Highlights")]/following-sibling::*/ul//li[1]/text()'
        p['memoryDetail']= response.xpath(memoryDetail_xpath).getall()
        screenDimention_xpath ='//div[re:test(text(),"Highlights")]/following-sibling::*/ul//li[2]/text()'
        p['screenDimention']= response.xpath(screenDimention_xpath).getall()
        lensDetail_xpath ='//div[re:test(text(),"Highlights")]/following-sibling::*/ul//li[3]/text()'
        p['lensDetail']= response.xpath(lensDetail_xpath).getall()
        batteryCapacity_xpath ='//div[re:test(text(),"Highlights")]/following-sibling::*/ul//li[4]/text()'
        p['batteryCapacity']= response.xpath(batteryCapacity_xpath).getall()
        processor_xpath ='//div[re:test(text(),"Highlights")]/following-sibling::*/ul//li[5]/text()'
        p['processor']= response.xpath(processor_xpath).getall()
        warranty_xpath ='//div[@class="_352bdz"]/text()'
        p['warranty']= response.xpath(warranty_xpath).getall()
        color_xpath ='//span[@id="Color"]/following-sibling::*[1]/ul//li/div/div/text()'
        p['color']= response.xpath(color_xpath).getall()
        RAM_xpath ='//span[@id="RAM"]/following-sibling::*[1]/ul//li/div/div/text()'
        p['RAM']= response.xpath(RAM_xpath).getall()
        yield p
