import json

from scrapy import cmdline
from scrapy_redis.spiders import RedisSpider

"""
这个是REDIS爬虫请求的实例。
这个实例实现了REDIS请求下发，并且持续裂变一共6次请求之后，并一并存储到本地。
因此你需要首先使用utils的redisListUpload下发任务。
另外实现了登陆的cookie使用，使用工具类cookieSave存储cookie
因此你需要首先使用utils的cookieSave获得企查查的登陆cookie,并拷贝到scrapy_demo_fangnan.cookies目录中。
裂变的信息传递难点在于request.meta标签的妙用，使得数据提交事物化。

种子页：REDIS队列下发
难度系数：四颗星

企查查账号：18923477217
密码：pk1****

"""


class DemoRedisSpider(RedisSpider):
    name = 'redis_SpiderDemo'
    redis_key = 'redisSpiderDemo:start_urls'

    fCookie = open('../cookies/cookies_qichacha.txt', 'r', encoding='utf-8')
    cookies = json.loads(fCookie.read())
    fCookie.close()

    custom_settings = {
        # 线程数
        'CONCURRENT_REQUESTS ': 1,
        # 指定redis
        'REDIS_HOST': '192.168.10.9',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {'password': '123456', 'db': 15},
        # 指定cookies
        'COOKIES_ENABLED': True,
        # 设置为True的时候scrapy就会把settings的cookie关掉，使用自定义cookie
        'LOVE_COOKIES': cookies,
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_demo_fangnan.middlewaresHedgehog.HegCookiesMiddlewars': 1,
            'scrapy_demo_fangnan.middlewaresHedgehog.HegUserAgentMiddlewares': 2,
        }

    }

    def parse(self, response):
        print(response.text)
        print("完成一个redis任务抓取")


if __name__ == '__main__':
    cmdline.execute("scrapy crawl redis_SpiderDemo".split())
