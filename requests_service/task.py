import redis
import json

start_urls = ['https://www.qichacha.com/firm_182249d7736fdb68960201022c19647a.html']
redis_key = 'requests:requests_start_urls'
# REDIS池应用单例模式构造
redisPool15 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)
redisPool14 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=14)

# 为了示范使用，我先自己下发一个任务。DB15
r = redis.Redis(connection_pool=redisPool15)
for url in start_urls:
    print("上传任务", redis_key, url)
    dictNow = {'url': url, 'mid': 1, 'etc': ''}
    r.lpush(redis_key, json.dumps(dictNow))

print("上传一批任务成功")
# 消费一个任务
r = redis.Redis(connection_pool=redisPool15)