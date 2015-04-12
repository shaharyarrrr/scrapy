# -*- coding: utf-8 -*-

# Scrapy settings for FERC_Filings project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'FERC_Filings'

SPIDER_MODULES = ['FERC_Filings.spiders']
NEWSPIDER_MODULE = 'FERC_Filings.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'FERC_Filings (+http://www.yourdomain.com)'
