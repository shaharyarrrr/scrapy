# pylint: disable=R0201, line-too-long,missing-docstring
__author__ = 'Shaharyar Ahmad'
from scrapy import Spider, Request
from House_Appropriations_Subcommittee_on_Interior_and_Environment.items import HouseItem
from House_Appropriations_Subcommittee_on_Interior_and_Environment.pipelines import process_string

class MainSpider(Spider):

    name = "MainSpider"
    start_urls = [
        "http://appropriations.house.gov/news/documentquery.aspx?SearchPhrase=&CatagoryID=34778&Year=&DocumentTypeID=2151&EventTypeID=&Page=1"]

    def parse(self, response):
        for links in range(1, 8):
            yield Request('http://appropriations.house.gov/news/documentquery.aspx?SearchPhrase=&CatagoryID=34778&Year=&DocumentTypeID=2151&EventTypeID=&Page=' + str(links), self.parse_data)

            yield Request('http://appropriations.house.gov/news/documentquery.aspx?SearchPhrase=&CatagoryID=34778&Year=&DocumentTypeID=2318&EventTypeID=&Page=' + str(links), self.parse_data)

    def parse_data(self, response):
        rows = response.xpath('//*[@id="ctl00_ContentCell"]/ul/li')
        for rows in rows:
            item = HouseItem()
            item['url'] = "http://appropriations.house.gov/news/" + \
                rows.xpath('table/tr/td/a[1]/@href').extract()[0]
            item['title'] = process_string(
                rows.xpath('table/tr/td/a[1]/b/text()').extract()[0])
            item['publishdate'] = process_string(
                rows.xpath('table/tr/td/b/text()').extract()[0].split('-')[0])
            item['_type'] = process_string(
                rows.xpath('//*[@id="ctl00_PageLink"]/text()').extract()[0])
            item['ekwhere'] = "Fed"
            item[
                'Source'] = "House Appropriations Subcommittee on Interior and Environment"
            item['summary'] = process_string(
                rows.xpath('table/tr/td/text()').extract()[3])

            yield item




