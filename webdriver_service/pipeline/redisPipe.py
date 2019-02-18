import hashlib
import json
import traceback
from _md5 import md5

import pymongo
import time

import redis
from pymongo.errors import DuplicateKeyError

from logging_utils.cJsonEncoder import CJsonEncoder
from logging_utils.log import mylog
from webdriver_service.driver_pool.driverPool import WebDriverPool
from webdriver_service.factory.fapiaoImpl import fapiaoImpl

# REDIS池应用单例模式构造
redisPool15 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)
redisPool14 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=14)
# 从内网Mongo获取账号密码

MONGODB_HOST = '192.168.10.9'
MONGODB_USER = 'fangnan'
MONGODB_PASSWORD = 'Fang135'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'hedgehog_spider'

client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
db = client[MONGODB_DBNAME]
db.authenticate(MONGODB_USER, MONGODB_PASSWORD)
item = db['aliyun_oss'].find_one({'name': 'beyebe'})
r15 = redis.Redis(connection_pool=redisPool15)


def getMission(redis_key, dBean, num):
    try:
        mission = r15.lpop(redis_key)
        if mission is not None:
            data = json.loads(mission.decode())
            WebDriverPool(dBean=dBean, num=num, headless=False).getOneDriver().deal(data)
        else:
            print("队列为空，间隔一段时间再尝试")
            time.sleep(1)
    except DuplicateKeyError:
        mylog.warning("存储主键重复,跳过")
    except:
        traceback.print_exc()


if __name__ == '__main__':
    # 发票验真平台举例
    redisKey = 'lst_fapiao'
    # 2
    fpdm = "4403181130"
    fphm = "27671246"
    kprq = "20180920"
    kjje = "351.69"

    data = {'fpdm': fpdm, 'fphm': fphm, 'kprq': kprq, 'kjje': kjje}
    r15.lpush(redisKey, json.dumps(data, cls=CJsonEncoder, ensure_ascii=False))
    getMission(redisKey, fapiaoImpl, 5)
