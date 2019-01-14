# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import traceback

import pymongo
from pymongo.errors import DuplicateKeyError

from logging_utils.log import mylog

"""
验证爬取数据，检查爬取字段。
查重并丢弃重复内容。
将爬取结果进行持久化。

1、open_spider(spider)就是打开spider时候调用的
2、close_spider(spider)关闭spider时候调用
3、from_crawler(cls, crawler)一般用来从settings.py中获取常量的
4、process_item(item, spider)是必须实现的,别的都是选用的

"""


# 一个高健壮、可复用的pipeline就像我这么写。
# 如果希望存到monog 只需要配置这个pipeline就可以了
class MongoPipeline(object):

    def open_spider(self, spider):
        self.MONGODB_HOST = spider.settings.get('LOVE_MONGODB_HOST', '192.168.10.9')
        self.MONGODB_USER = spider.settings.get('LOVE_MONGODB_USER', 'fangnan')
        self.MONGODB_PASSWORD = spider.settings.get('LOVE_MONGODB_PASSWORD', 'Fang135')
        self.MONGODB_PORT = spider.settings.get('LOVE_MONGODB_PORT', 27017)
        self.MONGODB_DBNAME = spider.settings.get('LOVE_MONGODB_DBNAME', 'hedgehog_spider')

        self.client = pymongo.MongoClient(host=self.MONGODB_HOST, port=self.MONGODB_PORT)
        self.db = self.client[self.MONGODB_DBNAME]
        self.db.authenticate(self.MONGODB_USER, self.MONGODB_PASSWORD)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 查看item是否存储了tableName字段,存储了就用tableName对应作为表名
        # 没有就使用auto_spiderName作为表名

        if item.get('tableName', None) is None:
            tableName = 'auto_' + spider.name
        else:
            tableName = item.get('tableName')
        # 如果不是特别需求,这里不要画蛇添足的添加入库时间,mongo的入库时间是可以通过自建索引_id来查询的
        try:
            self.db[tableName].insert_one(dict(item))
            print(spider.name, "mongo成功入库!")
        except DuplicateKeyError:
            print("该条主键存储重复,跳过")
        except:
            traceback.print_exc()
        # 这里返回item，后续的pipelines才能继续处理数据
        return item


class KafkaPipeline(object):
    def process_item(self, item, spider):
        print("Kafka尚未开发,暂不支持")
        return item


class LocalFilePipeline(object):
    def process_item(self, item, spider):
        print("本地文件存储尚未开发,暂不支持")
        return item


class OSSPipeline(object):
    def process_item(self, item, spider):
        print("OSSPipeline尚未开发,暂不支持")
        return item
