# pylint:disable=missing-docstring,too-few-public-methods
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PjmItem(Item):
    _id = Field()
    title = Field()
    url = Field()
    _type = Field()
    ekwhere = Field()
    summary = Field()
    publishdate = Field()
    scrapedate = Field()
    sourceid = Field()
    subsector = Field()
    Source = Field()
