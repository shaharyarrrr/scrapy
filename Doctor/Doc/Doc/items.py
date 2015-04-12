# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DocItem(scrapy.Item):
   DocName = scrapy.Field()
   Review = scrapy.Field()
   Clinic = scrapy.Field()
   Date = scrapy.Field()
   Time = scrapy.Field()
   Reviewer_Name = scrapy.Field()
