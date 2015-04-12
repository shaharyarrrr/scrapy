# pylint:disable=missing-docstring,invalid-name,too-few-public-methods
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project1Item(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    publishdate = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()
    body = scrapy.Field()
    scrapedate = scrapy.Field()
    sourceid = scrapy.Field()
    subsector = scrapy.Field()
