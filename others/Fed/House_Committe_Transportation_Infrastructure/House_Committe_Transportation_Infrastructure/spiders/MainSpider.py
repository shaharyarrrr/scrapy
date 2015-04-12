# pylint: disable=R0201,missing-docstring
__author__ = 'Shaharyar Ahmad'
from scrapy import Spider, Request
from House_Committe_Transportation_Infrastructure.items import SpiderItem
from House_Committe_Transportation_Infrastructure.pipelines import process_string

class MainSpider(Spider):

    name = "MainSpider"
    start_urls = ["http://transportation.house.gov/calendar/?EventTypeID=541"]


    def parse(self, response):
        rows = response.selector.xpath('//*[@id="ctl00_ContentCell"]/ul/li')
        for rows in rows:
            item = SpiderItem()
            item['title'] = process_string(
                rows.xpath('a/b/text()').extract()[0])
            url = process_string(rows.xpath('a/@href').extract()[0])
            item['url'] = "http://transportation.house.gov/calendar/" + url
            item['publishdate'] = process_string(rows.xpath('b/text()').extract()[1])
            item['publishtime'] = process_string(rows.xpath('b/text()').extract()[2])
            item['_type'] = "Hearings"
            item['ekwhere'] = "Fed"
            item[
                'Source'] = "House Committe on Transportation and Infrastructure"
            sub_com = process_string(rows.xpath('@class').extract()[0])

            if sub_com == "issue-107417":
                item['Subcommittee'] = "Aviation"
            if sub_com == "issue-107418":
                item[
                    'Subcommittee'] = "Coast Guard and Maritime Transportation"
            if sub_com == "issue-107419":
                item[
                    'Subcommittee'
                    ] = "Economic Development, Public Buildings, and Emergency Management"
            if sub_com == "issue-107420":
                item['Subcommittee'] = " Highways and Transit"
            if sub_com == "issue-107421":
                item[
                    'Subcommittee'] = " Railroads, Pipelines, and Hazardous Materials"
            if sub_com == "issue-107422":
                item['Subcommittee'] = "Water Resources and Environment"
            if sub_com == "issue-":
                item[
                    'Subcommittee'] = " Panel on Public-Private Partnerships/Bookmark Sign"
            yield item
            
