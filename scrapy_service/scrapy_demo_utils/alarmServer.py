# -*- coding:utf-8 -*-
"""
这个服务可以自动监控数据库、redis、kafka、服务器资源、服务器进程的情况
从而时时进行回调和服务器监控

2019/01/02

"""
import datetime
import traceback

import pymongo
import tornado.web
from bson import ObjectId
from tornado.options import define, options
import cv2
import numpy as np
import requests

# import urllib.request

define("port", default=9009, help="run on the given port", type=int)
LOVE_MONGODB_HOST = '192.168.10.9'
LOVE_MONGODB_USER = 'fangnan'
LOVE_MONGODB_PORT = 27017
LOVE_MONGODB_PASSWORD = 'Fang135'
LOVE_MONGODB_DBNAME = 'hedgehog_spider'

client = pymongo.MongoClient(host=LOVE_MONGODB_HOST, port=LOVE_MONGODB_PORT)
db = client[LOVE_MONGODB_DBNAME]
db.authenticate(LOVE_MONGODB_USER, LOVE_MONGODB_PASSWORD)


class IndexHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def get(self):
        return self.post()

    def post(self):
        # 收集数据库信息,如果传了tableName,那就返回tableName的信息
        # 没传tableName,就不返回
        tableNameList = db.collection_names()
        ansDict = {'data_db': [], 'state': 200, 'errMsg': 'success!'}
        # 数据库查询
        for tableName in tableNameList:
            try:
                dataNow = {'tableName': tableName}
                dataNow['num_total'] = db[tableName].find().count()
                dataNow['num_minute'] = self.countBefore(tableName, 60)
                dataNow['num_hour'] = self.countBefore(tableName, 60 * 60)
                dataNow['num_day'] = self.countBefore(tableName, 60 * 60 * 24)
                ansDict['data_db'].append(dataNow)
            except:
                print("数据库查询出现未知异常,表名", tableName)
                traceback.print_exc()
        # TODO Redis查询
        # TODO Kafka查询
        # TODO 服务器查询
        self.write(ansDict)

    def countBefore(self, tableName, seconds):
        date2 = datetime.datetime.now()
        # date2=datetime.strftime("%Y-%m-%d %H:%M:%S", "sadasd")
        date1 = date2 + datetime.timedelta(seconds=seconds)
        objIdTimeFrom = self.__timeToObjId(date1)
        objIdTimeTo = self.__timeToObjId(date2)
        return db[tableName].find({'_id': {
            '$gt': ObjectId(objIdTimeFrom),
        }}).count()

    def __timeToObjId(self, t):
        # 转换成秒数
        t = int(t.timestamp())
        # 转换成16进制的字符串，再加补齐16个0
        # t += 60 * 8
        t16 = hex(t)[2:]
        # print(t16)
        return str(t16) + '0000000000000000'

    def __objIdToTime(self, dateStr):
        dateStr = str(dateStr)[:8]
        t10 = int(dateStr, 16)
        # print(t10)
        # print(datetime.datetime.fromtimestamp(int(t10)))
        return t10


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[('/alarm.go', IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('[alarm Demo]tornadoansDict 启动')
    tornado.ioloop.IOLoop.instance().start()
