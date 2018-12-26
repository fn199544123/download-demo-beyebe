from scrapy import cmdline
from scrapy_redis.spiders import RedisSpider



"""
这个是REDIS爬虫请求的实例。
这个实例实现了REDIS请求下发，并且持续裂变一共6次请求之后，并一并存储入库。
难点在于meta标签的巧用，使得数据提交事物化。

种子页：REDIS队列下发
难度系数：三颗星

企查查账号：18923477217
密码：*******

REDIS地址:121.9.245.183
密码：*********
"""

class DemoRedisSpider(RedisSpider):
    name = 'redisSpiderDemo'
    redis_key = 'redisSpiderDemo:start_urls'
    custom_settings = {
        #REDIS 参数请去settings.py设置
    }
    def parse(self,response):
        print("完成一个redis任务抓取")

if __name__ == '__main__':
    cmdline.execute("scrapy crawl redisSpiderDemo".split())
