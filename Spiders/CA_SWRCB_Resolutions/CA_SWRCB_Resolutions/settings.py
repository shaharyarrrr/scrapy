#pylint: disable=missing-docstring
# -*- coding: utf-8 -*-

# Scrapy settings for CA_SWRCB_Resolutions project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CA_SWRCB_Resolutions'

SPIDER_MODULES = ['CA_SWRCB_Resolutions.spiders']
NEWSPIDER_MODULE = 'CA_SWRCB_Resolutions.spiders'
ITEM_PIPELINES = {'CA_SWRCB_Resolutions.pipelines.CaSwrcbResolutionsPipeline': 1000,}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CA_SWRCB_Resolutions (+http://www.yourdomain.com)'
