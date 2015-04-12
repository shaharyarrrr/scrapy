from scrapy import Spider
from scrapy.http import Request

from mscrapy.utils import get_extracted
from mscrapy.items import MScrapyItems


class SymbiosPk(Spider):
    name = "SymbiosPk"
    start_urls = ["http://www.symbios.pk/"]

    download_delay = 0.5
    store_name = "Symbios"

    categories = ["Apple Store"]

    def parse(self, response):
        menu = response.css('#column-left .nav')
        urls = menu.xpath('li/a/@href').extract()
        if self.categories:
            urls = [get_extracted(menu.xpath('li/a[strong[text() = "' + cat + '"]]/@href').extract())
                    for cat in self.categories
                    if cat]
        for url in urls:
            yield Request(url, callback=self.parse_items)

    def parse_items(self, response):
        urls = response.css('#product-list > div > ul > li li a::attr(href)').extract()
        next_page = "".join(response.css('.pagination > .links').xpath('a[text() = ">"]/@href').extract())
        if next_page:
            yield Request(next_page, callback=self.parse_items)
        for url in urls:
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = MScrapyItems()
        info = response.css('.product-info .right')
        item["store_name"] = self.store_name
        item["store_url"] = "".join(self.start_urls)
        item["url"] = response.url
        item["title"] = "".join(info.css('h1::text').extract())
        item["price"] = "".join(info.css('div[class^="price"]::text').extract()).strip()
        item["make"] = "".join(info.css('.manf a img::attr(alt)').extract())
        item["category"] = get_extracted(response.css('.breadcrumb a::text').extract(), 1)
        item["description"] = "".join(response.css('#sec-description').extract())
        return item
