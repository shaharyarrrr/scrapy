# pylint:disable=no-self-use,missing-docstring,line-too-long,too-few-public-methods
from scrapy import Spider
from House_Committe.items import HouseCommitteItem


class MainSpider(Spider):
    name = "MainSpider"
    start_urls = [
        "http://naturalresources.house.gov/calendar/archives/list.aspx?CatagoryID=5063"]

    def parse(self, response):
        i = 0
        rows = response.selector.xpath('//*[@id="ctl00_ctl27_EventsDG"]/tr')
        for row in rows:

            if i > 1 and i < 27:
                item = HouseCommitteItem()
                record_link = row.select('td/table/tr/td/b/text()').extract()
                if i < 19:
                    time = record_link[0].strip().split('2014')[1]
                    date = record_link[0].strip().split('2014')[0]
                    item['publishdate'] = date + "2014"
                if i > 18:
                    time = record_link[0].strip().split('2013')[1]
                    date = record_link[0].strip().split('2013')[0]
                    item['publishdate'] = date + "2013"
                item['publishtime'] = time

                item['title'] = row.select(
                    'td/table/tr/td/div[1]/a/text()').extract()
                item['url'] = row.select(
                    'td/table/tr/td/div[1]/a/@href').extract()
                item['ekwhere'] = "[Fed]"
                item[
                    'Source'] = "[House Committee on Natural Resources - Subcommittee on Fisheries, Wildlife, Oceans, and Insular Affairs]"
                item['_type'] = "[Hearings and Markups]"

                yield item
            i = i + 1

