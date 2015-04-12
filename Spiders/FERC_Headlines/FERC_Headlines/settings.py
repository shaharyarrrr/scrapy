# -*- coding: utf-8 -*-

# Scrapy settings for FERC_Headlines project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'FERC_Headlines'

SPIDER_MODULES = ['FERC_Headlines.spiders']
NEWSPIDER_MODULE = 'FERC_Headlines.spiders'
ITEM_PIPELINES = {'FERC_Headlines.pipelines.FercHeadlinesPipeline': 1000,}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'FERC_Headlines (+http://www.yourdomain.com)'
