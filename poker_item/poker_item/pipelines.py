# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class PokerItemPipeline(object):

    def process_item(self, item, spider):
        """处理item， 将其写入json文件
        :param item:
        :param spider:
        :return:
        """
        with open('poker.json', 'a+') as file:
            item_json = json.dumps(dict(item))
            file.write(item_json)

        file.close()

        return item
