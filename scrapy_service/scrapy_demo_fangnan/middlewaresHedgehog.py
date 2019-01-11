"""
小刺猬下载集群中间件

"""
import hashlib
import random
import json

import redis
import requests
from scrapy import Request
from scrapy.http import HtmlResponse

from logging_utils.log import mylog

redisPool14 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=14)
redisPool15 = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=15)
redis_key = 'requests:requests_start_urls'


# 【谢鋆维护】requests下载中间件
class requestsMiddlewars(object):
    def process_request(self, request, spider):
        url = request.url
        mylog.info("上传任务", redis_key, url)
        # 首先判断是否下载完了,尝试取结果
        r14 = redis.Redis(connection_pool=redisPool14)
        r15 = redis.Redis(connection_pool=redisPool15)
        hash = hashlib.md5()
        hash.update(url.encode('utf-8'))
        urlmd5 = hash.hexdigest()
        mid = request.meta['item'].get('mid_requests', 0)  # 谢鋆Request下载框架MID

        mylog.info('urlmd5', urlmd5)
        mission = r14.get(urlmd5)
        if mission is not None:
            html = mission.decode()
            return HtmlResponse(request.url, body=html, encoding='utf-8', request=request)
        # 如果没能找到结果,就查看是否在临时去重库里,这个是一级去重库
        if not r14.get('Dup_' + urlmd5):
            r14.expire(urlmd5, 10 * 60)
            mylog.info("回调结果成功")
            mylog.info(mission)
            # 如果都没有找到最后下发给谢鋆的下载框架
            dictNow = {'url': request.url, 'mid': mid, 'etc': ''}
            r14.set('Dup_' + urlmd5, 'Duplicate_removal')
            r15.lpush(redis_key, json.dumps(dictNow))
        return request


# Cookie中间件
class HegCookiesMiddlewars(object):

    def process_request(self, request, spider):
        cookieNow = {"QCCSESSID": "ck3e09qbhsqn2eh8g6195i4cm1"}
        mylog.info("cookies注入:", cookieNow)
        request.cookies = cookieNow
        request.meta.update({'dont_merge_cookies': True})


# Proxy中间件
class HegProxyMiddlewars(object):
    """
    新城负责维护的代理池（隧道代理），每次请求返回当前高可用的IP。
    """

    def process_request(self, request, spider):
        ip = requests.get('http://192.168.10.74:5555/random').text
        request.meta['proxy'] = 'http://' + ip
        mylog.info(request.meta['proxy'])


# 去重中间件
class HegDuplicateFilterMiddlewares(object):
    """
    小刺猬去重中间件的设计达到了保证分布式请求高可用和业务高容错的平衡
    TODO 请求前，进行key-value形式存储，定时过期（比如10秒），在这段时间不会再请求。
    请求成功，进行hash存储，彻底持久化。
    """

    def open_spider(self):
        self.redisPool = redis.ConnectionPool(host="192.168.10.9", password="123456", port=6379, db=14)

    def process_request(self, request, spider):
        r = redis.Redis(connection_pool=self.redisPool)
        isFilter = r.sadd(spider.name, request.url)
        if isFilter == 0:
            # 已经存在了,不再抓取
            mylog.info("去重不再抓取", request.url)
            # raise IgnoreRequest("去重不再抓取")
            r = redis.Redis(connection_pool=self.redisPool)
            name = r.lpop('name').decode()
        else:
            mylog.info("通过去重，继续抓取！", request.url)

    def process_response(self, request, response, spider):
        # 成功请求,正式添加进去重队列
        return None


# UA中间件
class HegUserAgentMiddlewares(object):

    def process_request(self, request, spider):
        # user agent 列表
        USER_AGENT_LIST = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15"
        ]
        PHONE_USER_AGENT_LIST = [
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
        ]
        # 导入random
        if 'm.' in request.url:
            agent = random.choice(PHONE_USER_AGENT_LIST)
        else:
            agent = random.choice(USER_AGENT_LIST)

        request.headers['User-Agent'] = agent
        request.headers['Accept-Charset'] = 'utf-8'
        request.headers['Accept-Language'] = 'zh-CN'
        request.headers['Accept-Encoding'] = 'deflate'


# urlChange-URL匹配订正
class HegurlChangeMiddlewares(object):
    def process_request(self, request, spider):
        # if 'm.qichacha.com/search?key=' in request.url:
        #     mylog.info("企查查搜索页url重定向")
        #     urlOld = request.url
        #     request._set_url(urlOld.replace('m.', 'www.'))
        #     mylog.info("原", urlOld, "修改", request.url)
        if 'm.qichacha.com/firm' in request.url:
            mylog.info("企查查落地页重定向")
            urlOld = request.url
            request._set_url(urlOld.replace('m.', 'www.'))
            mylog.info("原", urlOld, "修改", request.url)
        # if 'm.tianyancha.com/company/' in request.url:
        #     mylog.info("天眼查修正落地页,手机连接至http连接")
        #     urlOld = request.url
        #     request._set_url(urlOld.replace('m.', 'www.'))
        #     mylog.info("原", urlOld, "修改", request.url)

    def process_response(self, request, response, spider):
        if 'user_login' in response.url:
            mylog.info("被封了,重新发起请求")
            request = request
            return request
        return response


# 测试中间件(上线后应关闭)
class HegTestMiddlewares(object):
    def process_request(self, request, spider):
        mylog.info("【测试INFO】爬虫", spider.name)
        mylog.info("【测试INFO】正在发起一次请求", request.url)

    def process_response(self, request, response, spider):
        mylog.info("【测试INFO】爬虫", spider.name)
        mylog.info("【测试INFO】请求链接", request.url)
        mylog.info("【测试INFO】完成下载\n", response.text)
        return response


if __name__ == '__main__':
    hash = hashlib.md5()
    hash.update('12354'.encode('utf-8'))
    urlmd5 = hash.hexdigest()
    mylog.info('urlmd5', urlmd5)
