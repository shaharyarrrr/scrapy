from scrapy.spider import Spider
from scrapy.http import Request
import unicodedata
import re
from testing.items import TestingItem

class T(Spider):
	name ="T"
	start_urls=["http://www.bssa.org.uk/memberlist.php"]

	def parse(self, response):
		items = []
		rows = response.selector.xpath('//*[@id="memberlist"]/div/p')
		for rows in rows:
			item = TestingItem()
			item['Name_Company'] = rows.xpath('a/text()').extract()
			link = "http://www.bssa.org.uk/" + rows.xpath('a/@href').extract()[0]
			request = Request(link, callback=self.fun)
			request.meta['item'] = item
			yield request
			items.append(item)
		

	@staticmethod
	def fun(response):
		item = response.meta['item']
		item['Email_Main'] = response.xpath('//*[@id="contactbox"]/tr[3]/td[2]/a/text()').extract()
		item['Name_Person'] = response.xpath('//*[@id="contactstable"]/tr/td[1]/strong/text()').extract()
		item['Email_Person'] = response.xpath('//*[@id="contactstable"]/tr/td[4]/a/text()').extract()
		
		return item