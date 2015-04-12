from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import SelectorList

from mscrapy.items import MScrapyItems
from mscrapy.utils import get_extracted


class MegaPk(Spider):
    name = "MegaPk"
    start_urls = ["http://www.mega.pk/"]

    store_name = "Mega"
    categories = ["Laptops", "Tablets"]

    def parse(self, response):
        menu = response.css('#top-menu').xpath('ul/li/ul')
        lis = menu.xpath('li').extract()
        if self.categories:
            lis = SelectorList([li for cat in self.categories
                                for li in menu.xpath('li[h3[contains(text(), "' + cat + '")]]')
                                if cat])
        for url in lis.xpath('ul/li/a[not(contains(text(), "All"))]/@href').extract():
            yield Request(url, callback=self.parse_items)

    def parse_items(self, response):
        for url in response.css('.item_grid h3 a::attr(href)').extract():
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = MScrapyItems()
        item["store_name"] = self.store_name
        item["store_url"] = "".join(self.start_urls)
        item["url"] = response.url
        item["title"] = "".join(response.css('#laptop_header h1 a::text').extract())
        item["code"] = "".join(response.css('#navigator .share span::text').extract()).strip("SKU: ")
        item["price"] = "".join(response.css('#laptop_header .desc-price::text').extract()).strip()
        item["make"] = "".join(response.css('#laptop_header > div > a::text').extract())
        item["category"] = get_extracted(response.css('#navigator > a::text').extract(), 1)
        item['description'] = "".join(response.css('#tab_detail2').extract())
        return item
