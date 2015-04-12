# pylint: disable=R0201,missing-docstring
__author__ = 'Shaharyar Ahmad'
from scrapy import Spider, Request
from House_Committee_Oversight.items import HCOItem
from House_Committee_Oversight.pipelines import process_string

class MainSpider(Spider):
    name = "MainSpider"
    start_urls = ["http://oversight.house.gov/hearings/"]
        
    def parse(self, response):

        rows = response.selector.xpath(
            '//*[@id="bodyContent"]/div[1]/div[1]/div')
        for rows in rows:
            item = HCOItem()

            item['url'] = rows.xpath('div/h3/a/@href').extract()
            item['title'] = process_string(
                rows.xpath('div/h3/a/text()').extract()[0])
            item['Subcommittee'] = rows.xpath(
                'div[1]/div[1]/a/text()').extract()
            if item['Subcommittee'] == []:
                item['Subcommittee'] = "[Not Mentioned]"
            time_date = rows.xpath('div[1]/div[2]/text()').extract()
            item['publishdate'] = time_date[0].split('|')[0]
            item['publishtime'] = time_date[0].split('|')[1].split('m')[0] + "m."
            if item['publishtime'] == "m.":
                item['publishtime'] = "Not Mentioned"
            item[
                'Source'] = "House Committee on Oversight and Government Reform"
            item['_type'] = "Hearings"
            item['ekwhere'] = "Fed"
            yield item

    def start_requests(self):
        for count in range(1, 91):
            yield Request("%spage/%d/" % (self.start_urls[0], count), self.parse)
    
