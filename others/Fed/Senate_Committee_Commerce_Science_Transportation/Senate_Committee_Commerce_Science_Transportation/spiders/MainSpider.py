# pylint: disable=R0201,missing-docstring
__author__ = 'Shaharyar Ahmad'
from dateutil import parser
from urlparse import urljoin
from scrapy import Spider, Request
from Senate_Committee_Commerce_Science_Transportation.items import SpiderItem
from Senate_Committee_Commerce_Science_Transportation.pipelines import process_string

class MainSpider(Spider):
	name = "MainSpider"
	start_urls = ["http://www.commerce.senate.gov/public/index.cfm?p=Hearings&ContentType_id=14f995b9-dfa5-407a-9d35-56cc7152a7ed&Group_id=b06c39af-e033-4cba-9221-de668ca1978a&MonthDisplay=0&YearDisplay="]
	def start_requests(self):
		for count in range(1990, 2016):
			yield Request("%s%d&Label_id=&Label_id=" % (self.start_urls[0], count), self.parse)

	def parse(self, response):
		rows = response.selector.xpath('//*[@id="copy"]/div/ul/li')
		for rows in rows:
			item = SpiderItem()
			# item['title'] = process_string(rows.xpath('div[2]/a/text()').extract()[0])
			# item['url'] = urljoin(response.url, rows.xpath('div[2]/a/@href').extract()[0])
			item['publishdate'] = parser.parse(rows.xpath('div[1]/text()').extract()[0], fuzzy=True)
			# request = Request(rows.xpath('div[2]/a/@href').extract()[0], self.Funtion)
			# request.meta['item'] = item
			# yield request
			yield item

	def Funtion(self, response):
		item = response.meta['item']
		# item['publishtime'] = response.xpath('//*[@id="copy"]/div[1]/h4/text()').extract()[2]
		# item['summary'] = response.xpath('//*[@class="content"]/p[1]/text()[1] | //*[@class="content"]/p[2]/text()[1]').extract()
		return item