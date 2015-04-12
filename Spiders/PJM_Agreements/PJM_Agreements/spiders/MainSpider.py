# pylint:disable=no-self-use, missing-docstring
__author__ = 'Shaharyar Ahmad'
from scrapy import Spider, Request
from dateutil import parser
from urlparse import urljoin
from PJM_Agreements.items import PjmItem
from PJM_Agreements.pipelines import process_string


class MainSpider(Spider):
    name = "MainSpider"
    start_urls = ["http://www.pjm.com/documents/agreements.aspx"]

    def parse(self, response):
        yield Request('http://www.pjm.com/documents/agreements.aspx', self.parse_data)
        links = response.selector.xpath('//*[@id="content"]/article/ul/li')
        for links in links:
            url = links.xpath('a/@href').extract()
            url = urljoin(response.url, url[0])
            yield Request(url, callback=self.parse_data)

    def parse_data(self, response):
        i = 0
        rows = response.selector.xpath(
            '//*[@id="content"]/article/table/tbody/tr')
        for rows in rows:
            item = PjmItem()
            url = rows.xpath('td[1]/a/@href').extract()
            item['url'] = urljoin(response.url, url[0])
            publishdate = rows.xpath('td[2]/div/text()').extract()
            item['publishdate'] = parser.parse(publishdate[0], fuzzy=True)
            item['title'] = process_string(
                rows.xpath('td[1]/a/text()').extract()[0])
            summary = rows.xpath('td[1]/text()').extract()
            item['summary'] = process_string(summary[0])
            if len(summary) > 1:
                item['summary'] = process_string(
                    summary[0]) + process_string(summary[1])
            if rows.xpath('td[2]/div/text()').extract()[0] == "11.5.2003":
                item['title'] = process_string(response.xpath(
                    '//*[@id="content"]/article/h2/text()').extract()[(i / 2)])+" - "+item['title']
                i = i + 1
            item['ekwhere'] = "PJM"
            item['Source'] = "PJM"
            item['_type'] = "Agreements"

            yield item



