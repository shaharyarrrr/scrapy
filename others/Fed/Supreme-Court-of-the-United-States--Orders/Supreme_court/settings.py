#pylint: disable=missing-docstring
# -*- coding: utf-8 -*-

# Scrapy settings for Supreme_court project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Supreme_court'

SPIDER_MODULES = ['Supreme_court.spiders']
NEWSPIDER_MODULE = 'Supreme_court.spiders'
ITEM_PIPELINES = {'Supreme_court.pipelines.SupremeCourtPipeline': 1000,}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Supreme_court (+http://www.yourdomain.com)'
