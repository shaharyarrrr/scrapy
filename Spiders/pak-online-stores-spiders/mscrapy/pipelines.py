import re, html2text

from scrapy.exceptions import DropItem


class PricePipeline(object):
    def process_item(self, item, spider):
        if item['price'] and re.search('\d+', item['price']):
            item['price'] = "".join(re.findall('([0-9.])',
                                                item['price'])).strip(".")
            return item
        else:
            raise DropItem("Missing price in %s" % item)

class DescriptionPipeline(object):
    def process_item(self, item, spider):
        if item['description']:
            item['description'] = html2text.html2text(item['description'])
            return item
        else:
            raise DropItem("Missing description in %s" % item)
