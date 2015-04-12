"""Scraper for FERC Fillings"""

from scrapy.spider import Spider
from scrapy.http import Request
from FERC_Filings.items import FercFilingsItem
import unicodedata
import re


class FERC(Spider):

    """Main Class"""
    name = "FERC"
    start_urls = [
        "http://nepool.com/FERC_Filings_-_2015.php",
        "http://nepool.com/FERC_Filings_2014.php",
        "http://nepool.com/FERC_Filings_-_2013.php"]

    def parse(self, response):
        """start_urls gets here"""
        yield Request('http://nepool.com/FERC_Filings_-_2015.php', callback=self.parse_data)
        yield Request('http://nepool.com/FERC_Filings_2014.php', callback=self.parse_data_2)
        yield Request('http://nepool.com/FERC_Filings_-_2013.php', callback=self.parse_data_2)

    def parse_data(self, response):
        """For scraping Data"""
        items = []
        i = 0
        rows = response.selector.xpath(
            '//body/div[1]/div[3]/div[11]/div/div/div[2]/div/div')
        for rows in rows:
            if i > 0 and (i % 2) == 0:
                col = response.selector.xpath(
                    '//body/div[1]/div[3]/div[11]/div/div/div[2]/div/div' +
                    '[' + str(i + 1) + ']/div/table/tbody/tr')

                for col in col:

                    url1 = col.xpath('td[2]/font/a')

                    for url1 in url1:
                        item = FercFilingsItem()
                        item['url'] = url1.select('@href').extract()

                        item['Docket_No'] = url1.select(
                            'font/strong/text()').extract()

                        if not url1.select('font/strong/text()').extract():
                            item['Docket_No'] = url1.select(
                                'strong/text()').extract()

                        date_var = col.xpath(
                            'td[1]/font/text() | td[1]/font/font/text()').extract()
                        if response.url == "http://nepool.com/FERC_Filings_-_2015.php":
                            item['Date'] = process_string(
                                date_var[0]) + str(2015)
                        else:
                            item['Date'] = process_string(date_var[0])

                        title_var = col.select('td[2]/font/text()').extract()

                        if title_var[0].strip():
                            item['Title'] = process_string(title_var[0])
                        else:
                            if response.url != "http://nepool.com/FERC_Filings_-_2013.php":
                                item['Title'] = process_string(title_var[1])

                        item['Source'] = "[NEPOOL]"
                        item['Where'] = "[NEPOOL]"
                        item['Type'] = "FERC Filings"

                        items.append(item)
            i = i + 1
        return items

    def parse_data_2(self, response):
        """For scraping other Data"""
        items = []
        i = 0
        rows = response.selector.xpath(
            '//body/div[1]/div[3]/div[11]/div/div/div[2]/div/div')
        for rows in rows:
            if i > 0 and (i % 2) == 0:
                col = response.selector.xpath(
                    '//body/div[1]/div[3]/div[11]/div/div/div' +
                    '[2]/div/div[' + str(i + 1) + ']/div/table/tbody/tr')

                for col in col:
                    url2 = col.xpath('td[2]/font/strong')
                    url1 = col.xpath('td[2]/font[1]/a')
                    url3 = col.xpath('td[2]/a')
                    url4 = col.xpath('td[2]/strong')

                    item = FercFilingsItem()
                    item['url'] = url1.select('@href').extract()
                    if item['url'] == []:
                        item['url'] = col.select(
                            'td[2]/font/font/strong/a/@href | td[2]/p/a/@href' +
                            ' | td[2]/div/font/strong/a/@href |' +
                            ' td[2]/span/a/@href | td[2]/p/font/a/@href').extract()
                    if item['url'] == []:
                        item['url'] = url3.select('@href').extract()

                    if item['url'] == []:
                        item['url'] = url2.select('a/@href | @href').extract()
                    if item['url'] == []:
                        item['url'] = url4.select(
                            'a/@href | font/a/@href | font/a/strong/font/text()').extract()

                    item['Docket_No'] = url1.select(
                        'strong/font/text() | font/strong/text() |' +
                        ' font/font/strong/text() |' +
                        ' strong/text() | text()').extract()

                    if item['Docket_No'] == []:
                        item['Docket_No'] = col.select('td[2]/p/font/a/font/strong/text()').extract(
                        ) + col.select('td[2]/p/font/a/font/strong/strong/text()').extract()

                    if item['Docket_No'] == []:
                        item['Docket_No'] = url3.select(
                            'strong/font/text() | font/text()').extract()

                    if item['Docket_No'] == []:
                        item['Docket_No'] = url2.select(
                            'a/font/strong/text()').extract()
                    if item['Docket_No'] == []:
                        item['Docket_No'] = url4.select(
                            'a/font/strong/font/text()').extract()
                    if item['Docket_No'] == []:
                        item['Docket_No'] = col.select(
                            'td[2]/a/font/strong/text() | ' +
                            'td[2]/div/font/strong/a/font/strong/text() | ' +
                            'td[2]/span/a/font/font/font/strong/font/text() |' +
                            ' td[2]/font/font/strong/a/font/font/strong/text() |' +
                            ' td[2]/strong/a/strong/font/text() |' +
                            ' td[2]/a/font/font/strong/u/text() | ' +
                            'td[2]/a/font/u/strong/text() |' +
                            ' td[2]/p/a/font/strong/text() |' +
                            ' td[2]/font/strong/text()').extract()

                    if len(item['Docket_No']) != 0:
                        item['Docket_No'] = process_string(
                            item['Docket_No'][0])

                    item['Date'] = col.select(
                        'td[1]/font/text() |' +
                        ' td[1]/font/font/text() |' +
                        ' td[1]/p/font/text()').extract()

                    item['Date'] = process_string(item['Date'][0])

                    item['Title'] = col.select('td[2]/font/text() ' +
                                               '| td[2]/div/div/font/text() | ' +
                                               'td[2]/span/text() |' +
                                               ' td[2]/p/font/text() |' +
                                               ' td[2]/p/font[2]/text() | ' +
                                               'td[2]/div/font/text() |' +
                                               ' td[2]/p/font/font/text()').extract()

                    if item['Title'] == [" "]:
                        item['Title'] = col.select(
                            'td[2]/span/font/text()').extract()
                    if item['Title'] == []:
                        item['Title'] = col.select(
                            'td[2]/font/font/text()').extract()
                    temp_title = ""
                    tem_count = 0
                    while tem_count < len(item['Title']):
                        temp_title = temp_title + \
                            process_string(item['Title'][tem_count])
                        tem_count = tem_count + 1
                    item['Title'] = temp_title

                    item['Source'] = "[NEPOOL]"
                    item['Where'] = "[NEPOOL]"
                    item['Type'] = "FERC Filings"

                    items.append(item)

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
    """Entry point to string striping"""
    return remove_white_spaces(remove_unicode_characters(input_string))
