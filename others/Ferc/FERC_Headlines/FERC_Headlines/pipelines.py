# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
class FercHeadlinesPipeline(object):
	def open_spider(self, spider):
	    self.file = codecs.open('Ferc_Headlines_Results.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
	    line = json.dumps(dict(item)) + "\n"   
	    self.file.write(line.encode('utf-8').decode("unicode_escape"))

	def spider_closed(self, spider):
	    self.file.close()
