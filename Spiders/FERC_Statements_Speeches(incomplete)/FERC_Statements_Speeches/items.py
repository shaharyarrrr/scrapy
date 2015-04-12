# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FercStatementsSpeechesItem(scrapy.Item):
   Date = scrapy.Field()
   Summery = scrapy.Field()
   Title = scrapy.Field()
   url = scrapy.Field()
   Where = scrapy.Field()
   Type = scrapy.Field()
   Source = scrapy.Field()
