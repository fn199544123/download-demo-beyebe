# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from datetime import datetime

import scrapy


class NewsDemoItem(scrapy.Item):
    # baidu_single_spiderDemo的Item
    name = scrapy.Field()
    url = scrapy.Field()
    comefrom = scrapy.Field()

class BaiduHotwordItem(scrapy.Item):
    # baidu_single_spiderDemo的Item
    word = scrapy.Field()
    url = scrapy.Field()

class IqiyiVideoItem(scrapy.Item):
    # baidu_single_spiderDemo的Item
    title = scrapy.Field()
    url = scrapy.Field()
