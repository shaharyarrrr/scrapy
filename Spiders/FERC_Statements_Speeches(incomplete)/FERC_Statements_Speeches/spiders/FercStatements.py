from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
import unicodedata
import re
from FERC_Statements_Speeches.items import FercStatementsSpeechesItem

class FercStatements(Spider):
	name = "FercStatements"
	start_urls = ["http://www.ferc.gov/media/statements-speeches/2013.asp"]

	def parse(self, response):
		yield Request('http://www.ferc.gov/media/statements-speeches/2013.asp', self.parse_data)

	def parse_data(self, response):
		i=2
		url_count = 1
		items = []
		rows= response.selector.xpath('/html/body/table[1]/tr/td[2]/table/tr/td[1]/div/div/p/strong')
		for rows in rows:
			neg = 0
			item = FercStatementsSpeechesItem()
			item['Title'] = process_string(rows.select('/html/body/table[1]/tr/td[2]/table/tr/td[1]/div/div/p/text()['+str(i)+']').extract()[0])
			item['Date'] = process_string(rows.select('text()[1]').extract()[0].strip().split('-')[0])
			
			while item['Title'] == " " or item['Title'] == " | " or item['Title'] == "\" " or item['Title'] == " - \"":
				i=i+1
				
				item['Title'] = process_string(rows.select('/html/body/table[1]/tr/td[2]/table/tr/td[1]/div/div/p/text()['+str(i)+']').extract()[0])
				neg=1
			
			if item['Title'] == "Tony Clark & Robin Z. Meidhof, ":
				i=i+1
				item['Title'] = item['Title']+(process_string(rows.select('/html/body/table[1]/tr/td[2]/table/tr/td[1]/div/div/p/text()['+str(i)+']').extract()[0]))

			# item['Date'] = process_string(rows.select('text()[1]').extract()[0].strip().split('-')[0])
			
			# url_temp =  rows.select('/html/body/table[1]/tr/td[2]/table/tr/td[1]/div/div/p/a['+str(url_count)+']/text()').extract()
			# if url_temp:
			# 	url_temp=process_string(url_temp[0])
			
			# if url_temp == "Event Details":
			# 	url_count = url_count+1
			# item['url'] ="http://www.ferc.gov" + process_string(rows.select('/html/body/table[1]/tr/td[2]/table/tr/td[1]/div/div/p/a['+str(url_count)+']/@href').extract()[0])
			# if url_temp == "Management Alert" or url_temp == "Part 1" or url_temp == "Managing The Nation's Electricity Needs" or url_temp == "FERC Orders 745 & 755":
			# 	url_count= url_count+1
			# 	item['url'] =item['url']+ ", http://www.ferc.gov" + process_string(rows.select('/html/body/table[1]/tr/td[2]/table/tr/td[1]/div/div/p/a['+str(url_count)+']/@href').extract()[0])
			# if item['Title'] == " - ":
			# 	item['Title'] = url_temp
			# if item['Title'] == []:
			# 	item['Title'] = "url_temp"
			# 	i= i+2


			i=i+1
			# url_count = url_count+1
			items.append(item)
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
