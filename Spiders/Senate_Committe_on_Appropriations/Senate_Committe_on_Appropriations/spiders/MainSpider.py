# pylint:disable=no-self-use,missing-docstring,line-too-long
from scrapy import Spider, Request
from Senate_Committe_on_Appropriations.items import SenateCommitteOnAppropriationsItem
from Senate_Committe_on_Appropriations.pipelines import process_string

class MainSpider(Spider):

    name = "MainSpider"
    start_urls = ["http://www.appropriations.senate.gov"]

    def parse(self, response):
        for links in range(0, 3):
            yield Request('http://www.appropriations.senate.gov/hearings/energy-water?page=' + str(links), self.parse_data)
            yield Request('http://www.appropriations.senate.gov/hearings/interior?page=' + str(links), self.parse_data)
            yield Request('http://www.appropriations.senate.gov/hearings/transportation?page=' + str(links), self.parse_data)

    def parse_data(self, response):
        rows = response.selector.xpath(
            '//*[@id="block-system-main"]/div/div[2]/div[2]/div[3]/div/div/div[1]/div')
        for rows in rows:
            item = SenateCommitteOnAppropriationsItem()
            item['publishate'] = rows.select('div[1]/div/span/text()').extract()
            item['title'] = rows.select('div[2]/span/a/text()').extract()
            url = "http://www.appropriations.senate.gov"
            item['url'] = url + \
                process_string(rows.select('div[2]/span/a/@href').extract()[0])
            item['ekwhere'] = "Fed"
            item['_type'] = "Hearings"
            source = process_string(rows.select(
                '//*[@id="block-system-main"]/div/div[2]/div[2]/div[1]/div/h1/text()').extract()[0])
            item[
                'Source'] = "Senate Committe on Appropriations - Subcommittee on " + source
            yield item



