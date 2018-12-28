"""
小刺猬下载集群中间件

"""
import random
import json

import redis
import requests
from scrapy import Request


# Cookie中间件
class HegCookiesMiddlewars(object):

    def process_request(self, request, spider):
        if spider.settings.get('LOVE_COOKIES') is not None:
            loveCookies = spider.settings.get('LOVE_COOKIES')

            cookieScrapyDict = {}
            for cookieNow in loveCookies:
                cookieScrapyDict.update({cookieNow['name']: cookieNow['value']})
            print("cookies注入:", cookieScrapyDict)
            request.cookies = cookieScrapyDict


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
            print("去重不再抓取", request.url)
            # raise IgnoreRequest("去重不再抓取")
            r = redis.Redis(connection_pool=self.redisPool)
            name = r.lpop('name').decode()
        else:
            print("通过去重，继续抓取！", request.url)

    def process_response(self, request, response, spider):
        # 成功请求,正式添加进去重队列
        return response


# # 隧道IP中间件1
# class HegProxyMiddlewares(object):
#     print("正在尝试获取一个隧道IP代理池")
#     # 代理处理
#     appkey = 'NnR5UHJoRTlnQmJKUGJMRDpJV1FuaHpJdU4wdDlkY0pi'
#     # 代理服务器
#     proxyServer = "http://transfer.mogumiao.com:9001"
#     # appkey为你订单的key
#     proxyAuth = "Basic " + appkey
#
#     def process_request(self, request, spider):
#         request.meta["proxy"] = self.proxyServer
#         # request.meta["isIppool"]=True
#         request.headers["Authorization"] = self.proxyAuth
#
# # 隧道IP中间件2
# class HegProxy2Middlewares(object):
#     """
#     新代理中间件
#     """
#     print("正在尝试获取一个隧道IP代理池")
#
#     ipList = [
#         "47.106.230.172:10000",
#         "47.106.230.172:10001",
#         "47.106.230.172:10002",
#         "47.106.230.172:10003",
#         "47.106.230.172:10004",
#         "47.106.230.172:10005",
#         "47.106.230.172:10006",
#         "47.106.230.172:10007",
#         "47.106.230.172:10008",
#         "47.106.230.172:10009",
#     ]
#
#     def process_request(self, request, spider):
#         ip = random.choice(self.ipList)
#         print("ip-proxy", ip)
#         request.meta["proxy"] = "http://" + ip

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
        #     print("企查查搜索页url重定向")
        #     urlOld = request.url
        #     request._set_url(urlOld.replace('m.', 'www.'))
        #     print("原", urlOld, "修改", request.url)
        if 'm.qichacha.com/firm' in request.url:
            print("企查查落地页重定向")
            urlOld = request.url
            request._set_url(urlOld.replace('m.', 'www.'))
            print("原", urlOld, "修改", request.url)
        # if 'm.tianyancha.com/company/' in request.url:
        #     print("天眼查修正落地页,手机连接至http连接")
        #     urlOld = request.url
        #     request._set_url(urlOld.replace('m.', 'www.'))
        #     print("原", urlOld, "修改", request.url)

    def process_response(self, request, response, spider):
        if 'user_login' in response.url:
            print("被封了,重新发起请求")
            request = request
            return request
        return response


# 测试中间件(上线后应关闭)
class HegTestMiddlewares(object):
    def process_request(self, request, spider):
        print("【测试INFO】爬虫", spider.name)
        print("【测试INFO】正在发起一次请求", request.url)

    def process_response(self, request, response, spider):
        print("【测试INFO】爬虫", spider.name)
        print("【测试INFO】请求链接", request.url)
        print("【测试INFO】完成下载\n", response.text)
        return response


if __name__ == '__main__':
    url = "http://121.9.245.173:8001/middleware/htmlparse.go"
    print(json.loads(requests.get(url).text))
