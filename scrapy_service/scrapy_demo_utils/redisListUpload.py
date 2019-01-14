"""
# 这个类用来上传scrapy_redis任务
# 用比一比举例
"""
import uuid

import redis

from logging_utils.log import mylog

start_urls = ['https://www.qichacha.com/firm_182249d7736fdb68960201022c19647a.html']
redis_key = 'requests:requests_start_urls'
# REDIS池应用单例模式构造
redisPool = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)
# 账号: 18923477217
# 密码: pk*****
if __name__ == '__main__':

    r = redis.Redis(connection_pool=redisPool)

    for url in start_urls:
        urlNow = url + "?dup=" + str(uuid.uuid1()).replace('-', '_')
        print("上传任务" + redis_key + urlNow)
        r.lpush(redis_key, urlNow)
    print('hahaha')
