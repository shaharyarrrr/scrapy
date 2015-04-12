# pylint:disable=missing-docstring
# pylint: disable=R0201
# pylint: disable=unused-argument
# pylint: disable=too-few-public-methods
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Project1Pipeline(object):
    def process_item(self, item, spider):
        return item
