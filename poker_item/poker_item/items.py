# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PokerItemItem(scrapy.Item):
    # 定义item的字段
    head = scrapy.Field()
    body = scrapy.Field()
    name = scrapy.Field()
