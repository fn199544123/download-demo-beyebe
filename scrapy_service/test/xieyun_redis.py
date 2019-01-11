import hashlib
import json
from _md5 import md5

import redis

from logging_utils.log import mylog

start_urls = ['https://www.qichacha.com/firm_182249d7736fdb68960201022c19647a.html']
redis_key = 'requests:requests_start_urls'
# REDIS池应用单例模式构造
redisPool15 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)
redisPool14 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=14)

# 账号: 18923477217
# 密码: pk*****

if __name__ == '__main__':
    # 为了示范使用，我先自己下发一个任务。DB15
    r = redis.Redis(connection_pool=redisPool15)
    for url in start_urls:
        mylog.info("上传任务", redis_key, url)
        dictNow = {'url': url, 'mid': 1, 'etc': ''}
        r.lpush(redis_key, json.dumps(dictNow))

    mylog.info("上传一批任务成功")

    # 消费一个任务
    r = redis.Redis(connection_pool=redisPool15)
    mission = r.lpop(redis_key)
    dictNow = json.loads(mission.decode())
    mylog.info("获取任务成功")
    mylog.info(dictNow)

    # 回调一个任务,我们换一个DB,用14,并且设置超时时间
    r = redis.Redis(connection_pool=redisPool14)
    html = '<html>test</html>'
    url = "http://test.com"
    hash = hashlib.md5()
    hash.update(url.encode('utf-8'))
    urlmd5 = hash.hexdigest()
    mylog.info('urlmd5', urlmd5)
    mission = r.set(urlmd5, html)
    r.expire(urlmd5, 5 * 60)
    mylog.info("回调结果成功")
    mylog.info(mission)

    # 最后这步骤也是我来,我拿到你的HTML用
    r = redis.Redis(connection_pool=redisPool14)
    hash = hashlib.md5()
    hash.update(url.encode('utf-8'))
    urlmd5 = hash.hexdigest()
    mylog.info('urlmd5', urlmd5)
    mission = r.get(urlmd5)
    dictNow = mission.decode()
    mylog.info(dictNow)
    mylog.info("获取结果成功")
