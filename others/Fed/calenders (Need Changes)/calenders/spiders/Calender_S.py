
from scrapy.spider import Spider
from scrapy.http import Request
from calenders.items import CalendersItem


class Calender_S(Spider):
    name = "Calender_S"

    # allowed_domains = ["http://docs.house.gov"]
    start_urls = [
        "http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=AP10",
        "http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=AG00",
        "http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=AP06"]

    def parse(self, response):

        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=AG00', self.parse_data1)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=AP10', self.parse_data2)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=AP06', self.parse_data3)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=II00', self.parse_data4)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=II06', self.parse_data5)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=II24', self.parse_data6)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=II13', self.parse_data7)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=II10', self.parse_data8)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=SY20', self.parse_data9)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=SY15', self.parse_data10)
        yield Request('http://docs.house.gov/Committee/Calendar/ByMonth.aspx?Code=SY18', self.parse_data11)

    def parse_data1(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item['Source'] = "[House Committe on Agriculture]"
                        item['Type'] = "[Committee Schedule]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data2(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()

                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item[
                            'Source'] = "[House Committe on Appropriations - Subcommittee on Energy and Water Development]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data3(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item[
                            'Source'] = "[House Committe on Appropriations - Subcommittee on Interior and Environment]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data4(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item[
                            'Source'] = "[House Committe on Natural Resources - Full Committee]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data5(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item[
                            'Source'] = "[House Committe on Natural Resources - Subcommittee on Energy and Mineral Resources]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data6(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()

                        item[
                            'Source'] = "[House Committe on Natural Resources - Subcommittee on Indians, Insular and Alaska Native Affairs]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data7(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item[
                            'Source'] = "[House Committe on Natural Resources - Subcommittee on Water, Power and Oceans]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data8(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item[
                            'Source'] = "[House Committe on Natural Resources - Subcommittee on Federal Lands]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data9(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item[
                            'Source'] = "[House Committee on Science, Space and Technology - Subcommittee on Energy]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data10(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = url1_temp[count]
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item[
                            'Source'] = "[House Committee on Science, Space and Technology - Subcommittee on Research and Technology]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    def parse_data11(self, response):
        items = []

        rows = response.selector.xpath('//*[@id="body"]/table/tbody/tr')
        for rows in rows:
            col = response.selector.xpath('//*[@id="body"]/table/tbody/tr/td')
            for col in col:
                if col.select('p/a/@href').extract() != []:
                    url1_temp = col.select('p/a/@href').extract()
                    count = 0
                    for url1_temp in url1_temp:
                        item = CalendersItem()
                        url1_temp = col.select('p/a/@href').extract()
                        item['url'] = "[" + url1_temp[count] + "]"
                        item['Date'] = col.select('div/a/@title').extract()
                        item['Time'] = col.select(
                            'p[' + str(count + 1) + ']/a/b/text()').extract()
                        item[
                            'Source'] = "[House Committee on Science, Space and Technology - Subcommittee on Environment]"
                        item['Type'] = "[Hearings and Markups]"
                        item['Where'] = "[Fed]"
                        link = 'http://docs.house.gov/Committee/Calendar/' + \
                            url1_temp[count]
                        request = Request(link, callback=self.Funtion)
                        request.meta['item'] = item
                        yield request
                        count = count + 1
                        items.append(item)

    @staticmethod
    def Funtion(response):
        item = response.meta['item']
        title_temp = response.xpath(
            '//*[@id="previewPanel"]/div[1]/h1/text()').extract()
        title_temp =  title_temp[0].strip().split(':\r\n    ')[1]
        item['Title'] = "[" + title_temp + "]"
        return item
