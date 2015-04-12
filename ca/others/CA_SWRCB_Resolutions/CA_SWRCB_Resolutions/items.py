# pylint:disable=missing-docstring,invalid-name,too-few-public-methods
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CaSwrcbResolutionsItem(Item):
    # define the fields for your item here like:
    _id = Field()
    title = Field()
    url = Field()
    _type = Field()
    ekwhere = Field()
    publishdate = Field()
    scrapedate = Field()
    sourceid = Field()
    subsector = Field()
    resolution_number = Field()
    source = Field()