from scrapy.spider import Spider
from scrapy.http import Request
import unicodedata
import re
import urllib
import pythonwhois
from tld import get_tld
from urlparse import urljoin
from Sample.items import SampleItem

class S(Spider):
	name= "S"
	start_urls =["http://blogs.botw.org"] 

	def parse(self, response):

		links = response.selector.xpath('//*[@id="TopLevelIndexPanel"]/table/tr/td/div/ul/li')
		for links in links:
			
			link = "http://blogs.botw.org"+ str(links.xpath('a/@href').extract()[0])
			yield Request(link, self.parse_data)
		
	def parse_data(self, response):
			
		links = response.selector.xpath('//*[@id="ShowSpecificCategoryPanel"]/section/div[4]/ul/li')
		
		for links in links:
			call = links.xpath('a/@href').extract()
			yield Request(urljoin(response.url,call[0]),self.parse_data2)

		links = response.selector.xpath('//*[@id="ShowSpecificCategoryPanel"]/section/div[5]/ul/li')
		
		for links in links:
			call = links.xpath('a/@href').extract()
			yield Request(urljoin(response.url,call[0]),self.parse_data2)
		links = response.selector.xpath('//*[@id="ShowSpecificCategoryPanel"]/section/div[6]/ul/li')
		
		for links in links:
			call = links.xpath('a/@href').extract()
			yield Request(urljoin(response.url,call[0]),self.parse_data2)			
		
	def parse_data2(self, response):
		items = []
		rows = response.selector.xpath('//*[@id="Listings"]/div')
		for rows in rows:
			item = SampleItem()
			
			item['Blog_URL'] = rows.xpath('a/@href').extract()
			request = Request(item['Blog_URL'][0], callback=self.Funtion)
			request.meta['item'] = item
			yield request

			item['Blog_Name'] = rows.xpath('a/text()').extract()
			item['Blog_Catigory'] = str(rows.xpath('//*[@id="ShowSpecificCategory1_CatChainBreakdown"]/h4/a/text()').extract()[1]) + " - " + str(rows.xpath('//*[@id="ShowSpecificCategory1_CatChainBreakdown"]/h4/a/text()').extract()[2])
			item['Blog_Discription'] = process_string(rows.xpath('p/text()').extract()[0])
			items.append(item)
			

	def Funtion(self, response):
		item = response.meta['item']   
		
		item['Blog_Status'] = response.status
		item['Blog_Title'] = response.xpath('/html/head/title/text()').extract()
		if item['Blog_Title']:
			item['Blog_Title'] = process_string(item['Blog_Title'][0])
		url = get_tld(response.url)
		data = pythonwhois.get_whois(url)
		item['Contact_Info'] = data['contacts']
		item['Blog_Meta'] = response.headers

		# i=0
		if response.xpath('//h1/text()').extract():
			if process_string(response.xpath('//h1/text()').extract()[0]) != " ":
				item['h1_tag'] =process_string(response.xpath('//h1/text()').extract()[0])
		# 	for r in response.xpath('//h1/text()').extract():
		# 		if i != 0 and item['h1_tag']:
		# 			if process_string(response.xpath('//h1/text()').extract()[i]) != " ":
		# 				item['h1_tag'] = str(item['h1_tag'][0])+" "+str(process_string(response.xpath('//h1/text()').extract()[i]))
		# 		i=i+1
		# i=0
		if response.xpath('//h2/text()').extract():
			if process_string(response.xpath('//h2/text()').extract()[0]) != " ":
				item['h2_tag'] = process_string(response.xpath('//h2/text()').extract()[0])
		# 	for r in response.xpath('//h2/text()').extract():
		# 		if i!=0:	
		# 			if process_string(response.xpath('//h2/text()').extract()[i]) != " ":
		# 				item['h2_tag'] = str(item['h2_tag'][0])+" "+str(process_string(response.xpath('//h2/text()').extract()[i]))
		# 		i=i+1
		# i=0
		if response.xpath('//h3/text()').extract():
			if process_string(response.xpath('//h3/text()').extract()[0]) != " ":
				item['h3_tag'] =process_string(response.xpath('//h3/text()').extract()[0])
			# for r in response.xpath('//h3/text()').extract():
			# 	if i!=0:
			# 		if process_string(response.xpath('//h3/text()').extract()[i]) != " ":
			# 			item['h3_tag'] = str(item['h3_tag'][0])+" "+str(process_string(response.xpath('//h3/text()').extract()[i]))
			# 	i=i+1
		return item





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