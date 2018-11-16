# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import collections
class PokerItemPipeline(object):

    def process_item(self, item, spider):
        """处理item， 将其写入json文件
        :param item:
        :param spider:
        :return:
        """
        #创建有序字典
        od = collections.OrderedDict()
        #给字典赋值
        od['name']=item['name']
        od['head']=item['head']
        od['body']=item['body']
        with open('poker.json', 'a+') as file:
            #将有序的字典写入
            item_json = json.dumps(od, ensure_ascii=False)
            file.write(' '*5+item_json+'\n')

        file.close()

        return item
