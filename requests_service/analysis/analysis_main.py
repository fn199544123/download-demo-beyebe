import time
import redis
from pymongo import MongoClient


class Anlaysis:
    def __init__(self):
        self.redis_key = 'requests:requests_start_urls'
        redisPool13 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=13)
        self.r_return = redis.Redis(connection_pool=redisPool13)
        client = MongoClient('192.168.10.9', 27017)
        db = client['hedgehog_spider']
        db.authenticate(name='fangnan', password='Fang135')
        self.col = db['auto_redis_SpiderDemo']

    def __main__(self):
        sign = 1546272000
        while True:
            DateNow = int(time.time())
            
