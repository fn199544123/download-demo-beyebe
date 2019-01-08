import json
import redis

from factory.downloadFactory import getDownloadImp

start_urls = ['https://www.qichacha.com/firm_182249d7736fdb68960201022c19647a.html']
redis_key = 'requests:requests_start_urls'
redisPool15 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)

# 账号: 18923477217
# 密码: pk*****

if __name__ == '__main__':
    r_task = redis.Redis(connection_pool=redisPool15)
    # dictNow = {'url': url, 'mid': 1, 'etc': ''}
    while True:
        mission = r_task.lpop(redis_key)
        if mission is None:
            continue
        mission = json.loads(mission.decode().replace("'", '"'))
        print(mission)
        print('获取任务成功')
        try:
            getDownloadImp(mission['mid']).download(mission)
        except Exception as err:
            getDownloadImp(mission['mid']).error(mission, err)
