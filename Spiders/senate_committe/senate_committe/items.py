# pylint:disable=missing-docstring,invalid-name,too-few-public-methods
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class SenateCommitteItem(Item):
   _id = Field()
   title = Field()
   url = Field()
   _type = Field()
   ekwhere = Field()
   publishdate = Field()
   publishtime = Field()
   scrapedate = Field()
   sourceid = Field()
   subsector = Field()
   Source = Field()

