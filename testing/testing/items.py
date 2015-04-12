# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestingItem(scrapy.Item):
   Email_Main = scrapy.Field()
   Name_Company = scrapy.Field()
   Email_Person = scrapy.Field()
   Name_Person = scrapy.Field()
