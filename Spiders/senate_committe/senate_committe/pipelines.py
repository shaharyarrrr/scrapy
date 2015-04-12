# pylint:disable=missing-docstring, disable=R0201, unused-argument, too-few-public-methods
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import unicodedata, re

class SenateCommittePipeline(object):
    def process_item(self, item, spider):
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
    """Entry function for string striping"""
    return remove_white_spaces(remove_unicode_characters(input_string))