# pylint: disable=no-self-use,line-too-long, missing-docstring
from urlparse import urljoin
from scrapy import Spider, Request
from House_Committe_on_Agriculture.items import SpiderItem
from House_Committe_on_Agriculture.pipelines import process_string

class MainSpider(Spider):
    name = "MainSpider"
    start_urls = [
        "http://docs.house.gov/Committee/Calendar/ByWeek.aspx?WeekOf=02012015_02072015&Code=AP06"]

    def parse(self, response):
        for year in range(2009, 2016):
            for month in range(1, 12):
                for week in range(0, 5):
                    if week == 0:
                        yield Request('http://docs.house.gov/Committee/Calendar/ByWeek.aspx?WeekOf=0' + str(month) + '0' + str(week + 1) + str(year)+'_0' + str(month) + '0' + str((week + 1) * 7) + str(year)+'&Code=AP06', callback=self.parse_data)
                    if week == 1:
                        yield Request('http://docs.house.gov/Committee/Calendar/ByWeek.aspx?WeekOf=0' + str(month) + '0' + str((week * 7) + 1) + str(year)+'_0' + str(month) + str(((week + 1) * 7)) + str(year)+'&Code=AP06', self.parse_data)
                    if week > 1:
                        yield Request('http://docs.house.gov/Committee/Calendar/ByWeek.aspx?WeekOf=0' + str(month) + str((week * 7) + 1) + str(year)+'_0' + str(month) + str((week + 1) * 7) + str(year)+'&Code=AP06', self.parse_data)

    def parse_data(self, response):

        rows = response.selector.xpath(
            '//*[@id="container-outer"]/div[1]/div[3]/div/div/div[2]/table/tbody/tr')
        for rows in rows:

            if rows.xpath('td/p'):
                url1_temp = rows.xpath('td/p').extract()
                count = 0
                for url1_temp in url1_temp:
                    item = SpiderItem()
                    url_tem = rows.xpath('td/p/a/@href').extract()
                    item['url'] = urljoin(response.url, url_tem[count])
                    item['publishdate'] = rows.xpath('td/div/a/@title').extract()
                    time_temp = rows.xpath('td/p[' + str(count + 1) + ']/text()[2]').extract()
                    item['publishtime'] = process_string(time_temp[0].strip().split('[')[0])
                    item['Source'] = "[House Committe on Appropriations - Subcommittee on Interior and Environment]"
                    item['_type'] = "[Hearings and Markups]"
                    item['ekwhere'] = "[Fed]"
                    link = 'http://docs.house.gov/Committee/Calendar/' + url_tem[count]
                    request = Request(link, callback=self.grab_title)
                    request.meta['item'] = item
                    yield request
                    count = count + 1
                    yield item

    def grab_title(self, response):
        item = response.meta['item']
        item['title'] = response.xpath('//*[@id="previewPanel"]/div[1]/h1/text()').extract()
        item['title'] = process_string(item['title'][0].strip().split(':')[1])

        return item



