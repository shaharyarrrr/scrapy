# pylint:disable=no-self-use,missing-docstring,inherit-non-class,bare-except
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from Project1.items import Project1Item



class MainSpider(BaseSpider):
    name = "MainSpider"

    allowed_domains = ["www.calepa.ca.gov"]

    start_urls = [
        "http://www.calepa.ca.gov/PressRoom/Releases/2014/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2013/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2012/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2011/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2010/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2009/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2008/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2007/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2006/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2005/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2004/default.htm",
        "http://www.calepa.ca.gov/PressRoom/Releases/2003/default.htm"]

    def parse(self, response):

        hxs = HtmlXPathSelector(response)
        rows = hxs.select("//div[contains(@class, 'content_left_column')]/ul/li")
        if len(rows) == 0:
            rows = hxs.select("//div[contains(@class, 'add_padding')]/ul/li")
        if len(rows) == 0:
            rows = hxs.select("//div[contains(@class, 'add_padding')]/p")
        if len(rows) == 0:
            print "oops"
        items = []
        i = 0

        for rows in rows:
            item = Project1Item()

            try:
                item['title'] = rows[i].select('a/text()')[0].extract().replace(
                    '\r\n\t\t\t\t\t', " ").replace('\t', " ").replace('\r\n', " ")
                if item['title'] == "English" or item[
                        'title'] == "English version" or item['title'] == "English,":
                    item['title'] = rows[i].select('text()')[0].extract().split(':')[1].replace(
                        '\r\n\t\t\t\t\t',
                        " ").replace('\t', " ").replace('\r\n', " ")
                if '(' in item['title'] and ')' not in item['title']:
                    item['title'] = item['title'].replace('(', "")

                item['publishdate'] = rows[i].select(
                    'text()')[0].extract().split(':')[0].strip('\t\n\r')
                if "PDF" in item['publishdate'] or item['publishdate'] == "":
                    item['publishdate'] = rows[
                        i -
                        1].select('text()').extract()[0].split(':')[0]

                item['url'] = rows[i].select('a/@href').extract()[0]
                if '/PressRoom/Releases/2003/' in item['url']:
                    item['url'] = item['url'].replace(
                        '/PressRoom/Releases/2003/',
                        '')
                if 'http' not in item['url']:
                    item['url'] = str(
                        response.request.url).replace('default.htm', item['url'])
                items.append(item)

            except:
                print "oops"
            i = i + 1
        return items

    def parse_data(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.select("//div[contains(@class, 'content_left_column')]/p")
        count = 1
        if len(rows) == 0:
            rows = hxs.select("//div[contains(@class, 'add_padding')]/p")
            count = 2
        if len(rows) == 0:
            print "oops"

        item = response.meta['item']
        item['summary'] = rows[count].select('text()').extract()
        return item
