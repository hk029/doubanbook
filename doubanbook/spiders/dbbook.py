# -*- coding: utf-8 -*-
import scrapy
import re

class DbbookSpider(scrapy.Spider):
    name = "dbbook"
    #allowed_domains = ["https://www.douban.com/doulist/1264675/"]
    start_urls = (
        'https://www.douban.com/doulist/1264675/',
    )

    def parse(self, response):
        #print response.body
        selector = scrapy.Selector(response)
        books = selector.xpath('//div[@class="bd doulist-subject"]')
        for each in books:
            title = each.xpath('div[@class="title"]/a/text()').extract()[0]
            rate = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            author = re.search('<div class="abstract">(.*?)<br',each.extract(),re.S).group(1)
            title = title.replace(' ','').replace('\n','')
            author = author.replace(' ','').replace('\n','')
            print 'title:' + title
            print 'rate:' + rate
            print author
            print ''


