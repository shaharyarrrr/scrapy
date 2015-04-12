from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from FERC_Staff_Reports_and_Papers.items import FercStaffReportsAndPapersItem
import unicodedata
import re


class FERC_Staff_Reports(Spider):
    name = "FERC_Staff_Reports"
    start_urls = ["https://www.ferc.gov/legal/staff-reports.asp"]

    def parse(self, response):
        yield Request('https://www.ferc.gov/legal/staff-reports.asp', self.parse_data)

    def parse_data(self, response):
        items = []
        i = 1
        col = response.selector.xpath('//*[@id="tabcontentcontainer"]/div')
        for col in col:

            rows = response.selector.xpath(
                '//*[@id="sc' + str(i) + '"]/table/tr')
            count = 0
            for rows in rows:
                if (count > 0 and i != 7) or (count > 1 and i == 7):
                    item = FercStaffReportsAndPapersItem()
                    item['Date'] = process_string(
                        rows.select('td[1]/text()').extract()[0])
                    item['url'] = rows.select(
                        'td[2]/a/@href | td[2]/p/a/@href').extract()
                    item['Title'] = process_string(
                        rows.select('td[2]/a/text() | td[2]/p/a/text()').extract()[0])
                    temp_type = response.selector.xpath(
                        '//*[@id="tablist"]/li[' + str(i) + ']/a/text()').extract()
                    item['Type'] = "FERC Staff Reports & Papers - " + \
                        process_string(temp_type[0])
                    item['Source'] = "FERC"
                    item['Where'] = "Fed"
                    items.append(item)
                count = count + 1
            i = i + 1
        return items






def remove_white_spaces(input_string):
    """ Removes continuous spaces in the input string """
    try:
        return re.sub(r"\s+", " ", input_string)
    except:
        raise


def remove_unicode_characters(input_string):
    """ strips unicode characters in the string """
    try:
        return unicodedata.normalize(
            'NFKD', input_string).encode('ascii', 'ignore')
    except:
        raise


def process_string(input_string):

    return remove_white_spaces(remove_unicode_characters(input_string))
