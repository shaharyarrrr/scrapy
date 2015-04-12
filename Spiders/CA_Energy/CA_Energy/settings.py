#pylint: disable=missing-docstring
# -*- coding: utf-8 -*-

# Scrapy settings for CA_Energy_Commission_News_Releases project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CA_Energy'

SPIDER_MODULES = ['CA_Energy.spiders']
NEWSPIDER_MODULE = 'CA_Energy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CA_Energy (+http://www.yourdomain.com)'
