from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import SelectorList

from mscrapy.items import MScrapyItems
from mscrapy.utils import get_extracted


class Vmart(Spider):
    name = "Vmart"
    start_urls = ["http://www.vmart.pk/"]

    store_name = "Vmart"
    categories = ["Mobile Phones", "Tablets", "Laptops"]

    def parse(self, response):
        menu = get_extracted(response.css('#vmenu_69'))
        lis = menu.xpath('li')
        if self.categories:
            lis = SelectorList([li for cat in self.categories
                                for li in menu.xpath('li[div/a[text() = "' + cat + '"]]')
                                if cat])
        for url in lis.xpath('div/a/@href').extract():
            yield Request(url, callback=self.parse_items)

    def parse_items(self, response):
        urls = response.css('.grid-list div a.product-title::attr(href)').extract()
        next_page = "".join(response.css('.ty-pagination__next::attr(href)').extract())
        if next_page:
            yield Request(next_page, callback=self.parse_items)

        for url in urls:
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = MScrapyItems()
        info = response.css('.ty-breadcrumbs a::text').extract()
        item["store_name"] = self.store_name
        item["store_url"] = "".join(self.start_urls)
        item["url"] = response.url
        item["title"] = "".join(response.css('.ty-product-block-title::text').extract())
        item["price"] = "".join(response.css('.ty-price-num::text').extract())
        item["make"] = get_extracted(info, 1)
        item["category"] = get_extracted(info, 2)
        item["description"] = "".join(response.css('#content_description').extract())
        return item
