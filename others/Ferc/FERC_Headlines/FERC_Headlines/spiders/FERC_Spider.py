from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from FERC_Headlines.items import FercHeadlinesItem


class FERCSpider(BaseSpider):
    name = "ferc"
    allowed_domains = ["www.ferc.gov"]

    start_urls = ["http://www.ferc.gov/media/headlines/archives.asp"]

    def parse(self, response):

        hxs = HtmlXPathSelector(response)
        yield Request('http://www.ferc.gov/media/headlines.asp', self.parse_data)

        archive_links = hxs.select(
            "//div[contains(@class, 'container')]/ul/ul/a/@href")
        i = 0
        for link in archive_links:
            i = i + 1
            href = link.extract()
            yield Request('http://www.ferc.gov' + href, self.parse_data)

    def parse_data(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        dates = hxs.select("//ul[contains(@class, 'indented')]/strong/text()")
        titles = hxs.select("//ul[contains(@class, 'indented')]/ul")
        i = 0
        if response.request.url == "http://www.ferc.gov/media/headlines/2013/2013-4.asp" or response.request.url == "http://www.ferc.gov/media/headlines/2013/2013-2.asp" or response.request.url == "http://www.ferc.gov/media/headlines/2013/2013-3.asp":
            i = 1
        for date in dates:
            item = FercHeadlinesItem()
            item['date'] = date.extract().strip('\t\n\r  ')
            if item['date'] == "December 21, 200":
                item['date'] = "December 21, 2006"
            if item['date'] == "" or item['date'] == "6":
                continue
            if i == 4 and response.request.url == "http://www.ferc.gov/media/headlines/2013/2013-2.asp":
                i = 5
            if response.request.url == "http://www.ferc.gov/media/headlines/2014/2014-3.asp":
                if i == 34 or i == 36:
                    i = i + 1
            try:
                item['title'] = titles[i].select('text()').extract()[0].strip('\t\n\r  ').replace(
                    '\r\n   ',
                    '').replace(
                    '\r\n',
                    '').replace(
                    ' \r\n',
                    '')
            except:
                item['title'] = ""
            if item['title'] == "":
                try:
                    item['title'] = titles[i].select('text()').extract()[1].strip(':\t\n\r  ').replace(
                        '\r\n   ',
                        '').replace(
                        '\r\n',
                        '').replace(
                        ' \r\n',
                        '')
                except:
                    item['title'] = ""
            if item['title'] == "\"":
                try:
                    item['title'] = titles[i].select('text()').extract()[2].strip(':\t\n\r  ').replace(
                        '\r\n   ',
                        '').replace(
                        '\r\n',
                        '').replace(
                        ' \r\n',
                        '')
                except:
                    item['title'] = ""
            if item['title'] == "":
                try:
                    item['title'] = titles[i].select('./a//text()').extract()[0].strip(':\t\n\r  ').replace(
                        '\r\n   ',
                        '').replace(
                        '\r\n',
                        '').replace(
                        ' \r\n',
                        '')
                except:
                    item['title'] = ""
            item['url'] = titles[i].select('./a//@href').extract()
            if item['url'] == []:
                item['url'] = titles[i].select(
                    './ul/li/span/a/@href').extract()
            k = 0
            for url in item['url']:
                if 'http' not in url:
                    item['url'][k] = 'http://www.ferc.gov' + url
                k = k + 1
            i = i + 1
            items.append(item)
        return items
