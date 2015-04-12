# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CalendersItem(scrapy.Item):
   Date = scrapy.Field()
   Time = scrapy.Field()
   Title = scrapy.Field()
   url = scrapy.Field()
   Where = scrapy.Field()
   Type = scrapy.Field()
   Source = scrapy.Field()
