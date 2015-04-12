"""For Review"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy import signals
from scrapy.http import TextResponse 
from scrapy.xlib.pydispatch import dispatcher
from scrapy.spider import Spider
from scrapy.http import Request
from Doc.items import DocItem
import unicodedata
import re

class SpiderMain(Spider):
    handle_httpstatus_list = [403]
    """docstring for Spider"""
    name = "SpiderMain"
    f = open('urls.txt')
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    def parse(self, response):
        driver = webdriver.Firefox()
        driver.get(response.url)
        # WebDriverWait(driver, 10)
        # assert "Doctor" in driver.title
        response = TextResponse(url=response.url, body=driver.page_source, encoding='utf-8')
        items = []
        # # rows = 3
        rows = response.selector.xpath('//*[@id="reviewsTab"]/div/div')
       
        for rows in rows:
            item = DocItem() 
            item['DocName'] = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div[2]/div[2]/h1").text
            item['Review'] = rows.xpath('div[1]/div[2]/div/span[1]/text()').extract()
            item['Clinic'] = rows.xpath('div[2]/div/div[2]/text()').extract()
            date_temp= rows.xpath('div[1]/div[3]/@datetime').extract()
            if date_temp:
                item['Date'] = date_temp[0].strip().split(' ')[0]
                item['Time'] = date_temp[0].strip().split(' ')[1]

            item['Reviewer_Name'] = process_string(rows.xpath('div[1]/div[1]/div[2]/text()').extract()[0])
            items.append(item)
        return items
        driver.close()
    
		


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