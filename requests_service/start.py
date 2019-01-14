import json
import redis
import time
import sys

sys.path.append("../")
from requests_service.factory.downloadFactory import getDownloadImp

start_urls = ['https://www.qichacha.com/firm_182249d7736fdb68960201022c19647a.html']
redis_key = 'requests:requests_start_urls'
redisPool15 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)

# 账号: 18923477217
# 密码: pk*****

if __name__ == '__main__':
    r_task = redis.Redis(connection_pool=redisPool15)
    # dictNow = {'url': url, 'mid': 1, 'etc': ''}
    while True:
        pipe = r_task.pipeline()
        pipe.zrange('requests:requests_start_urls', 0, 0)
        pipe.zremrangebyrank('requests:requests_start_urls', 0, 0)
        mission = pipe.execute()[0]
        # mission = r_task.lpop(redis_key)
        if len(mission) == 0:
            time.sleep(1)
            print("1秒后重试")
            continue
        url = mission[0].decode()
        if ('qichacha' in url) and ('#' not in url):
            mid = 1
        if ('qichacha' in url) and ('#' in url):
            mid = 2
        # mission = json.loads(mission.decode().replace("'", '"'))
        print(url)
        print('获取任务成功')
        try:
            getDownloadImp(mid).download(mission)
            time.sleep(10)
            # 休眠10秒，限制频率。
        except Exception as err:
            getDownloadImp(mid).error(mission, 'Error')
