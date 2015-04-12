# pylint:disable=no-self-use,missing-docstring,line-too-long
from scrapy import Spider, Request
from Supreme_court.items import SupremeCourtItem


class MainSpider(Spider):
    name = "MainSpider"

    start_urls = ["http://www.supremecourt.gov/orders/ordersofthecourt/03"]

    def parse(self, response):

        i = 0
        for i in range(3, 15):
            if i < 10:
                yield Request('http://www.supremecourt.gov/orders/ordersofthecourt/0' + str(i), self.parse_data)
            if i > 9:
                yield Request('http://www.supremecourt.gov/orders/ordersofthecourt/' + str(i), self.parse_data)

    def parse_data(self, response):

        rows = response.selector.xpath(
            '//*[@id="mainbody"]/div[3]/div/div/div')
        for row in rows:
            item = SupremeCourtItem()
            item['ekwhere'] = "[Fed]"
            item['_type'] = "[Orders]"
            item['Source'] = "[Supreme Court of the United States]"
            item['url'] = row.xpath('span[2]/a/@href').extract()
            item['title'] = row.select('span[2]/a/text()').extract()
            item['publishdate'] = row.xpath('span[1]/text()').extract()
            yield item
