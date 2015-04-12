import re

from scrapy import Spider, Item, Field
from scrapy.http import Request

from mscrapy.items import MScrapyItems
from mscrapy.utils import get_extracted, add_query_parameters, get_striped


class HomeShoppingPk(Spider):
    name = "HomeShoppingPk"
    start_urls = ["http://homeshopping.pk/"]

    download_delay = 0.5
    store_name = "Home Shopping"

    categories_1 = ["Mobiles & Tablets"]
    categories_2 = ["Mobile Phones"]
    categories_3 = ["Apple", "Samsung"]

    def parse(self, response):
        menu = response.css('.menu > li')
        urls = self.get_urls(menu, self.categories_1)
        for url in urls:
            yield Request(url, callback=self.parse_menu_item)

    def parse_menu_item(self, response):
        menu = response.css('#LayoutColumn1 > #subCat ul > li')
        urls = self.get_urls(menu, self.categories_2)
        for url in urls:
            yield Request(url, callback=self.parse_category)

    def parse_category(self, response):
        menu = response.css('#SideCategoryShopByBrand li')
        urls = self.get_urls(menu, self.categories_3)
        return Request(self.get_url_from_urls(urls),
                        callback=self.parse_subcategory)

    def get_url_from_urls(self, urls):
        url = get_extracted(urls)
        ids = [get_extracted(re.findall('brandid=(\d+)', url))
               for url in urls
                   if url]
        return add_query_parameters(url, 'brandid', "|".join(ids))

    def get_urls(self, menu, categories):
        urls = menu.xpath('a/@href').extract()
        if categories:
            urls = filter(None,
                            [get_extracted(menu.xpath('a[contains(text(), "' + cat + '")]/@href').extract())
                             for cat in categories
                                 if cat])
        return urls

    page = 2
    def parse_subcategory(self, response):
        urls = response.css('.ProductList li strong > a::attr(href)').extract()
        if not len(urls) < 12:
            if len(urls) > 0:
                yield Request(add_query_parameters(response.url, 'page', self.page),
                                callback=self.parse_subcategory)
            self.page += 1
        for url in urls:
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = MScrapyItems()
        item["store_name"] = self.store_name
        item["store_url"] = "".join(self.start_urls)
        item["url"] = response.url
        item["title"] = "".join(response.css('#ProductDetails > .BlockContent > h2::text').extract())
        item["code"] = self.get_item_detail(response, "Product ID")
        item["price"] = self.get_item_detail(response, "Price")
        item["make"] = self.get_item_detail(response, "Brand")
        item["category"] = "".join(response.css('#ProductBreadcrumb').xpath('ul[1]/li[2]//text()').extract())
        item["description"] = "".join(response.css('div#ProductDescription').extract())
        return item

    def get_item_detail(self, response, label):
        row = response.css('#ProductDetails > div > div > .ProductDetailsGrid')
        row = row.xpath('div[div[@class="Label" and contains(text(), "' + label + '")]]/div[2]')
        return "".join(get_striped(row.xpath('. | em | a').xpath('text()').extract()))
