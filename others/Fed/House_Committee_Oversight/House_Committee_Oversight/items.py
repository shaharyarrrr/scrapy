# pylint: disable=too-few-public-methods,missing-docstring
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field, Item


class HCOItem(Item):
    _id = Field()
    title = Field()
    url = Field()
    _type = Field()
    ekwhere = Field()
    publishdate = Field()
    scrapedate = Field()
    sourceid = Field()
    subsector = Field()
    publishtime = Field()
    Subcommittee = Field()
    Source = Field()
    