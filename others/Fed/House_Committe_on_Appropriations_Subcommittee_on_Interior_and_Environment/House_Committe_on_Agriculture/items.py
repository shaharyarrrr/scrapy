# pylint:disable=missing-docstring,invalid-name,too-few-public-methods
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
   _id = scrapy.Field()
   publishdate = scrapy.Field()
   publishtime = scrapy.Field()
   title = scrapy.Field()
   url = scrapy.Field()
   ekwhere = scrapy.Field()
   _type = scrapy.Field()
   Source = scrapy.Field()
   scrapedate = scrapy.Field()
   sourceid = scrapy.Field()
   subsector = scrapy.Field()
