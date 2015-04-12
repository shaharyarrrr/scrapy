# pylint:disable=no-self-use,missing-docstring,line-too-long
from scrapy.spider import Spider, Request
from senate_committe.items import SenateCommitteItem
from senate_committe.pipelines import process_string

class MainSpider(Spider):
    name = "MainSpider"
    start_urls = ["http://www.ag.senate.gov/hearings"]

    def parse(self, response):
        """docstring for parse"""
        yield Request('http://www.ag.senate.gov/hearings', self.parse_data)
        for links in range(2, 10):
            yield Request('http://www.ag.senate.gov/hearings?PageNum_rs=' + str(links), self.parse_data)


    def parse_data(self, response):
        rows = response.selector.xpath('//*[@id="main"]/table/tbody/tr')
        for rows in rows:
            if rows.select('td[2]'):
                item = SenateCommitteItem()
                item['title'] = process_string(
                    rows.select('td[1]/a/text() | td[1]/a/span/text()').extract()[0])
                if item['title'] == " ":
                    item['title'] = process_string(
                        rows.select('td[1]/a/text()').extract()[1])
                item['url'] = process_string(
                    rows.select('td[1]/a/@href').extract()[0])
                time_date = rows.select('td[3]/time/text()').extract()
                item['publishtime'] = time_date[0].strip().split(' ')[1]
                item['publishdate'] = time_date[0].strip().split(' ')[0]
                item['ekwhere'] = "Fed"
                item['Source'] = "Hearing"
                item[
                    '_type'] = "Senate Committe on Agriculture, Nutrition, and Forestry"

                yield item
