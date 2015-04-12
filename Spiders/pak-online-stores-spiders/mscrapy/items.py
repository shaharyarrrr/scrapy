# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MScrapyItems(Item):
    store_name = Field()
    store_url = Field()
    url = Field()
    title = Field()
    code = Field()
    price = Field()
    make = Field()
    category = Field()
    description = Field()
