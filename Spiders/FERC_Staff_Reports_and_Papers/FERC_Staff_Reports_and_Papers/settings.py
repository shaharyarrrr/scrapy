# -*- coding: utf-8 -*-

# Scrapy settings for FERC_Staff_Reports_and_Papers project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'FERC_Staff_Reports_and_Papers'

SPIDER_MODULES = ['FERC_Staff_Reports_and_Papers.spiders']
NEWSPIDER_MODULE = 'FERC_Staff_Reports_and_Papers.spiders'
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408] 
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'FERC_Staff_Reports_and_Papers (+http://www.yourdomain.com)'
