# pylint:disable=no-self-use, line-too-long, missing-docstring
__author__ = 'Shaharyar Ahmad'
from scrapy import Spider, Request
from dateutil import parser
from urlparse import urljoin
from PJM_Manual_Updates.items import PjmItem
from PJM_Manual_Updates.pipelines import process_string

class MainSpider(Spider):
    name = "MainSpider"
    start_urls = ["http://www.pjm.com/documents/manuals/manual-updates.aspx"]

    def parse(self, response):
        yield Request('http://www.pjm.com/documents/manuals/manual-updates.aspx', self.parse_data)
        yield Request('http://www.pjm.com/documents/manuals/manual-updates/2014-updates.aspx', self.parse_data)
        yield Request('http://www.pjm.com/documents/manuals/manual-updates/2013-updates.aspx', self.parse_data)
        yield Request('http://www.pjm.com/documents/manuals/manuals-archive.aspx', self.parse_data2)

    def parse_data(self, response):
        i = 0
        rows = response.selector.xpath('//*[@id="tblUpdates"]/tbody/tr/td')
        for rows in rows:
            i = 0
            if rows.xpath('h4/a[1]'):
                item = PjmItem()
                url = rows.xpath('h4/a[1]/@href').extract()
                item['url'] = urljoin(response.url, url[0])
                publishdate = rows.xpath('text()[3]').extract()
                item['publishdate'] = parser.parse(publishdate[0], fuzzy=True)
                item['title'] = process_string(
                    rows.xpath('h4/a[1]/text()').extract()[0])
                item['summary'] = ""
                summary = rows.xpath('ul/li/text()').extract()
                while len(summary) > i:
                    item['summary'] = item['summary'] + \
                        process_string(summary[i])
                    i = i + 1
                item['ekwhere'] = "PJM"
                item['Source'] = "PJM"
                item['_type'] = "Manual Updates"

                yield item

    def parse_data2(self, response):
        sections = response.selector.xpath('//*[@id="body_0_pnlUpdates"]/div')
        for sections in sections:
            rows = sections.xpath('div/table/tbody/tr')
            for rows in rows:
                item = PjmItem()
                url = rows.xpath('td[2]/a/@href').extract()
                item['url'] = urljoin(response.url, url[0])
                publishdate = rows.xpath('td[1]/text()').extract()
                item['publishdate'] = parser.parse(publishdate[0], fuzzy=True)
                item['title'] = process_string(sections.xpath('h4/a/text()').extract()[0]) + " - " + process_string(rows.xpath('td[2]/a/text()').extract()[0])

                item['ekwhere'] = "PJM"
                item['Source'] = "PJM"
                item['_type'] = "Manual Updates"

                yield item


