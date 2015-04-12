# pylint:disable=no-self-use, line-too-long,missing-docstring
from scrapy import Spider, Request
from urlparse import urljoin
from CA_Energy.items import CaEnergyItem
from CA_Energy.pipelines import process_string


class MainSpider(Spider):
    name = "MainSpider"

    start_urls = ["http://www.energy.ca.gov/releases/1999_releases/index.html"]

    def parse(self, response):

        i = 0

        for i in range(1999, 2016):

            if i < 2004:
                yield Request('http://www.energy.ca.gov/releases/' + str(i) + '_releases/index.html', self.parse_data)
            if i > 2011:
                yield Request('http://www.energy.ca.gov/releases/index.php?getyear=' + str(i), self.parse_data1)
            if i > 2003 and i < 2012:
                yield Request('http://www.energy.ca.gov/releases/' + str(i) + '_releases/index.html', self.parse_data2)

    def parse_data(self, response):
        rows = response.selector.xpath('//*[@id="main_content"]/div[1]/ul/li')
        for rows in rows:
            item = CaEnergyItem()
            item['ekwhere'] = "[CA]"
            item['_type'] = "[CA Energy Commission]"
            item['Source'] = "[News Releases]"
            item['publishdate'] = rows.xpath('p/a/text()').extract()
            if item['publishdate'] == []:
                item['publishdate'] = rows.xpath('p/text()').extract()

            item['title'] = process_string(rows.xpath('p/text()').extract()[0])

            item['url'] = rows.xpath('p/a/@href').extract()
            yield item

    def parse_data1(self, response):
        rows = response.selector.xpath('//*[@id="main_content"]/div[1]/ul/li')
        for rows in rows:
            item = CaEnergyItem()
            item['ekwhere'] = "[CA]"
            item['_type'] = "[CA Energy Commission]"
            item['Source'] = "[News Releases]"
            item['publishdate'] = rows.xpath('text()').extract()
            if item['publishdate'] == []:
                item['publishdate'] = rows.xpath('text()').extract()
            item['title'] = rows.xpath('a/text()').extract()
            item['url'] = urljoin(response.url, rows.xpath('a/@href').extract()[0])
            yield item

    def parse_data2(self, response):
        rows = response.selector.xpath('//*[@id="main_content"]/div[1]/ul/li')
        for rows in rows:
            item = CaEnergyItem()
            item['ekwhere'] = "[CA]"
            item['_type'] = "[CA Energy Commission]"
            item['Source'] = "[News Releases]"
            item['publishdate'] = rows.xpath('a/text()').extract()
            if item['publishdate'] == []:
                item['publishdate'] = rows.xpath('text()').extract()
            item['title'] = process_string(rows.xpath('text()').extract()[0])
            item['url'] = urljoin(response.url, rows.xpath('a/@href').extract()[0])
            yield item
            