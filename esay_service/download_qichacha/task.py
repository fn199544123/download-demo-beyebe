import redis
import json

start_urls = [
    'https://www.qichacha.com/company_getinfos?unique=84c17a005a759a5e0d875c1ebb6c9846&companyname=%E4%B9%90%E8%A7%86%E7%BD%91%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF(%E5%8C%97%E4%BA%AC)%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&tab=susong']
redis_key = 'requests:requests_start_urls'
# REDIS池应用单例模式构造
redisPool15 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)
redisPool14 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=14)

# 为了示范使用，我先自己下发一个任务。DB15
r = redis.Redis(connection_pool=redisPool15)
for url in start_urls:
    print("上传任务", redis_key, url)
    dictNow = {'url': url, 'mid': 2, 'etc': ''}
    r.lpush(redis_key, json.dumps(dictNow))

print("上传一批任务成功")
# 消费一个任务
r = redis.Redis(connection_pool=redisPool15)
