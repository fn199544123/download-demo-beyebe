# 下载器基类
import traceback

import redis
from pymongo import MongoClient


def format_headers(string) -> dict:
    """
    将在Chrome上复制下来的浏览器UA格式化成字典，以\n为切割点
    :param string: 使用三引号的字符串
    :return:
    """
    string = string.strip().replace(' ', '').split('\n')
    new_headers = {}
    for key_value in string:
        key_value_list = key_value.split(':')
        if len(key_value_list) > 2:
            new_headers.update({key_value_list[0]: ':'.join(key_value_list[1::])})
        else:
            new_headers.update({key_value_list[0]: key_value_list[1]})
    return new_headers


class DownloadImp:
    def __init__(self):
        client = MongoClient('192.168.10.9', 27017)
        db = client['hedgehog_spider']
        db.authenticate(name='fangnan', password='Fang135')
        header = """
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9
        Cache-Control: max-age=0
        Connection: keep-alive
        Host: www.qichacha.com
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134
        """
        self.headers = format_headers(header)
        self.col = db['qichacha_cookies']
        self.redis_key = 'requests:requests_start_urls'
        self.redisPool15 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)
        redisPool14 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=14)
        self.r_return = redis.Redis(connection_pool=redisPool14)


    def download(self, mission):
        pass

    def mid(self):
        raise Exception("该实例未覆写mid方法")

    def state(self):
        pass

    def error(self, mission, err):
        url = mission['url']
        print(err)
        print(url)
        self.r_return.set(url, err)
        self.r_return.expire(url, 5 * 60)
        print(url)
        print('返回结果异常，url:', url)
