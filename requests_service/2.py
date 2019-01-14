import redis
import time

redisPool15 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)
r15 = redis.Redis(connection_pool=redisPool15)

# 下发任务
r15.zadd('test_sorted_set', 'mission1', float(time.time()))
r15.zadd('test_sorted_set', 'mission2', float(time.time()))
r15.zadd('test_sorted_set', 'mission3', float(time.time()))
r15.zadd('test_sorted_set', 'mission4', float(time.time()))
# 查看一下所有任务
items = r15.zrange('test_sorted_set', 0, 10)
print("所有任务", items)
# 获取队列尾部（事务）
pipe = r15.pipeline()
pipe.zrange('test_sorted_set', 0, 0)
pipe.zremrangebyrank('test_sorted_set', 0, 0)
item = pipe.execute()[0]
print("拿出了一个任务", item)
# 查看一下所有任务
items = r15.zrange('test_sorted_set', 0, 10)
print("所有任务", items)