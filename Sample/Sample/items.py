# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SampleItem(scrapy.Item):
	h1_tag = scrapy.Field()
	h2_tag = scrapy.Field()
	h3_tag = scrapy.Field()
	Blog_Meta = scrapy.Field()
	Blog_Catigory = scrapy.Field()
	Blog_Discription = scrapy.Field()
	Blog_Title = scrapy.Field()
	Blog_Status = scrapy.Field()
	Contact_Info = scrapy.Field()
	Alexa_Rank = scrapy.Field()
	Blog_Name =scrapy.Field()
	Blog_URL = scrapy.Field()
