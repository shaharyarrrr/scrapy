# pylint:disable=no-self-use,missing-docstring,line-too-long,too-many-statements,too-many-branches,unused-argument,inherit-non-class,missing-final-newline
from scrapy import Spider, Request
from urlparse import urljoin
from CA_SWRCB_Resolutions.items import CaSwrcbResolutionsItem
from CA_SWRCB_Resolutions.pipelines import process_string

class MainSpider(Spider):
    name = "MainSpider"
    allowed_domains = ["www.waterboards.ca.gov"]

    start_urls = [
        "http://www.waterboards.ca.gov/board_decisions/adopted_orders/resolutions/"]
    def start_requests(self):
        i = 0
        for i in range(0, 100):

            if i < 16 or i > 66:
                if i < 10:
                    yield Request("%sres0%d.shtml" % (self.start_urls[0], i), self.parse)
                if i > 9:
                    yield Request("%sres%d.shtml" % (self.start_urls[0], i), self.parse)
    def parse(self, response):
        hxs = response
        i = 0
        rows = hxs.selector.xpath('//div[contains(@id, "page_contents")]/table/tr')
        for row in rows:
            i = i + 1
            if i > 1:

                item = CaSwrcbResolutionsItem()
                item['source'] = "CA SWRCB"
                item['_type'] = "Resolutions"
                item['ekwhere'] = "CA"
                item['resolution_number'] = row.select(
                    'td[1]/p/a/text()').extract()
                if item['resolution_number'] == []:
                    item['resolution_number'] = row.select(
                        'td[1]/p/text()').extract()
                if item['resolution_number'] == []:
                    item['resolution_number'] = row.select(
                        'td[1]/a/text()').extract()
                if item['resolution_number'] == []:
                    item['resolution_number'] = row.select(
                        'td[1]/div/a/text()').extract()
                if item['resolution_number'] == []:
                    item['resolution_number'] = row.select(
                        'td[1]/text()').extract()
                if item['resolution_number'] == []:
                    item['resolution_number'] = row.select(
                        'td[1]/div/text()').extract()
                if item['resolution_number'] == []:
                    item['resolution_number'] = row.select(
                        'td[1]/div/span/a/text()').extract()
                if item['resolution_number'] == []:
                    item['resolution_number'] = row.select(
                        'td[1]/span/a/text()').extract()
                if item['resolution_number'] == []:
                    item['resolution_number'] = row.select(
                        'td[1]/center/a/text()').extract()
                if item['resolution_number'] == ["\n\t\t\t", "\n\t\t"]:
                    item['resolution_number'] = row.select(
                        'td[1]/center/a/text()').extract()
                if item['resolution_number'] == [
                        "\n      ",
                        "\n      ",
                        "\n    "]:
                    item['resolution_number'] = row.select(
                        'td[1]/div/p[1]/a/text()').extract()
                    item['resolution_number'].append(
                        row.select('td[1]/div/p[2]/a[1]/text()').extract())
                    item['resolution_number'].append(
                        row.select('td[1]/div/p[2]/a[2]/text()').extract())
                if item['resolution_number'] == ["\n      ", "\n    "]:
                    item['resolution_number'] = row.select(
                        'td[1]/div/p/a[1]/text()').extract()
                    item['resolution_number'].append(
                        row.select('td[1]/div/p/a[2]/text()').extract())
                item['url'] = row.select('td[1]/p/a/@href').extract()
                if item['url'] == []:
                    item['url'] = row.select('td[1]/center/a/@href').extract()

                if item['url'] == []:
                    item['url'] = row.select('td[1]/a/@href').extract()
                if item['url'] == []:
                    item['url'] = row.select('td[1]/div/a/@href').extract()
                if item['url'] == []:
                    item['url'] = row.select(
                        'td[1]/div/span/a/@href').extract()
                if item['url'] == []:
                    item['url'] = row.select('td[1]/span/a/@href').extract()
                if item['url'] == []:
                    item['url'] = row.select(
                        'td[1]/div/p[1]/a/@href').extract()
                item['publishdate'] = row.select('td[2]/p/text()').extract()
                if item['publishdate'] == []:
                    item['publishdate'] = row.select('td[2]/div/text()').extract()
                if item['publishdate'] == []:
                    item['publishdate'] = row.select('td[2]/text()').extract()
                if item['publishdate'] == []:
                    item['publishdate'] = row.select('td[2]/center/text()').extract()
                if item['publishdate'] == ["\n\t\t\t", "\n\t\t"]:
                    item['publishdate'] = row.select('td[2]/center/text()').extract()
                item['title'] = row.select('td[3]/p/text()').extract()
                if item['title'] == []:
                    item['title'] = row.select('td[3]/text()').extract()
                if item['title'] == []:
                    item['title'] = row.select('td[3]/a/text()').extract()
                if item['title'] == []:
                    item['title'] = row.select('td[3]/div/text()').extract()
                if item['title'] == []:
                    item['title'] = row.select('td[3]/font/text()').extract()
                if item['title'] == [" "]:
                    item['title'] = row.select('td[3]/p/font/text()').extract()
                if item['title'] == []:
                    item['title'] = row.select('td[3]/span/*/text()').extract()
                if item['publishdate'] == [2 / 20 / 1986]:
                    item['title'] = row.select('td[3]/text()').extract()
                    item['url'].append(
                        row.select('td[1]/center/a/@href').extract())
                    item['resolution_number'].append(
                        row.select('td[1]/center/a/text()').extract())
                item['title'] = process_string(item['title'][0])
                item['url'] = urljoin(response.url, item['url'][0])
                yield item

