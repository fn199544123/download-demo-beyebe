import redis
import hashlib

class Anlaysis:
    def __init__(self):
        self.redis_key = 'requests:requests_start_urls'
        redisPool14 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=14)
        self.r_return = redis.Redis(connection_pool=redisPool14)
        self.hash_ = hashlib.md5()

