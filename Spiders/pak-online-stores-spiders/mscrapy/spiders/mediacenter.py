from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import SelectorList

from mscrapy.items import MScrapyItems
from mscrapy.utils import get_extracted, get_striped


class MediaCenter(Spider):
    name = "MediaCenter"
    start_urls = ["http://mediacenterpk.com/"]

    store_name = "MediaCenter"
    categories = ["iPhone & iPod", "iPad"]

    def parse(self, response):
        menu = response.css('#nav_custom').xpath('li/ul')
        lis = menu.xpath('li')
        if self.categories:
            lis = SelectorList([li for cat in self.categories
                                for li in menu.xpath('li[a[span[text() = "' + cat + '"]]]')
                                if cat])
        for url in lis.xpath('ul/li/a[span[not(contains(text(), "Accessories"))]]/@href').extract():
            yield Request("%s?limit=all" % url, callback=self.parse_items)

    def parse_items(self, response):
        urls = response.css('.products-grid li h2 a::attr(href)').extract()
        for url in urls:
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = MScrapyItems()
        info = response.css('.breadcrumbs li a[title=""]::text').extract()
        item["store_name"] = self.store_name
        item["store_url"] = "".join(self.start_urls)
        item["url"] = response.url
        item["title"] = "".join(response.css('.product-name h1::text').extract())
        item["price"] = get_extracted(response.css('.price *::text').extract())
        item["make"] = get_extracted(info)
        item["category"] = get_extracted(info, 2)
        item["description"] = "".join(response.css('.product-specs').extract())
        return item
