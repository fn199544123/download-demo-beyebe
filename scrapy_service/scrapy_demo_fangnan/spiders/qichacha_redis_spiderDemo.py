import json

from scrapy import cmdline, Request
from scrapy_redis.spiders import RedisSpider
import sys
sys.path.append("../../../")
from logging_utils.log import mylog
from scrapy_service.scrapy_demo_fangnan.items import QichachaHtmlItem

"""
这个是REDIS爬虫请求的实例。
这个实例实现了REDIS请求下发，并且持续裂变一共6次请求之后，并一并存储到本地。
因此你需要首先使用utils的redisListUpload下发任务。
另外实现了登陆的cookie使用，使用工具类cookieSave存储cookie
因此你需要首先使用utils的cookieSave获得企查查的登陆cookie,并拷贝到scrapy_demo_fangnan.cookies目录中。
裂变的信息传递难点在于item标签的妙用，使得数据提交事物化。

种子页：REDIS队列下发
难度系数：四颗星

企查查账号：18923477217
密码：pk1****

2019/01/02

"""


class DemoRedisSpider(RedisSpider):
    name = 'redis_SpiderDemo'
    redis_key = 'redisSpiderDemo:start_urls'
    URL_BASE = "https://www.qichacha.com/company_getinfos?unique={}&companyname={}&tab={}"

    custom_settings = {
        # 关闭重定向
        'REDIRECT_ENABLED': True,  # 关掉重定向, 不会重定向到新的地址
        # 'HTTPERROR_ALLOWED_CODES': [301, 302],
        # 深度优先
        'SCHEDULER_QUEUE_CLASS': 'scrapy_redis.queue.LifoQueue',
        # 线程数
        'CONCURRENT_REQUESTS ': 1,
        # 指定redis
        'REDIS_HOST': '192.168.10.9',
        'REDIS_PORT': 6379,
        'REDIS_PARAMS': {'password': '123456', 'db': 15},
        'DOWNLOADER_MIDDLEWARES': {
            # 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
            # 'scrapy_demo_fangnan.middlewaresHedgehog.HegCookiesMiddlewars': 1,
            'scrapy_demo_fangnan.middlewaresHedgehog.HegUserAgentMiddlewares': 2,
            'scrapy_demo_fangnan.middlewaresHedgehog.requestsMiddlewars': 999,

        }

    }



    def parse(self, response):
        # TODO 你需要首先使用utils的redisListUpload下发任务。否则会一直等待直到有任务来！

        url = response.url
        print("当前解析页", url)
        request = response.request
        if '玄鸟' not in response.text and 'company_getinfos' not in url:
            print("虽然正常可达,但登陆失败,需要更新cookie")
            print(response.text)
            with open("../web_msg/qcc_loginErr.html", "w", encoding='utf-8') as fp:
                fp.write(response.text)
            raise Exception("虽然正常可达,但登陆失败,需要更新cookie")
        elif '#ipo' in url:
            print("该页为上市信息，不采集")
            # IPO不采集
            request._set_url = (request.url.replace('#ipo', '#base'))
            request.dont_filter = True

            yield request
        elif 'base' in url or 'firm' in url:
            print("该页为基本信息")
            item = QichachaHtmlItem()
            item['base_html'] = response.text
            item['name'] = response.css('h1::text')[0].extract()
            item['id'] = url.split('firm_')[1].split('.')[0]
            item['mid_requests'] = 1  # 谢鋆Request下载框架MID
            print("企查查首页解析成功:", item['name'], item['id'])
            requestNew = Request(url=self.URL_BASE.format(item['id'], item['name'], 'susong'))
            requestNew.meta['item'] = item
            requestNew.meta['item']['mid_requests'] = 2
            requestNew.priority = request.priority + 100
            requestNew.dont_filter = True
            yield requestNew
        elif 'susong' in url:
            print("该页为法律诉讼")
            request.meta['item']['susong_html'] = response.text
            request.meta['item']['mid_requests'] = 2  # 谢鋆Request下载框架MID

            requestNew = Request(url=request.url.replace('susong', 'run'))
            requestNew.meta['item'] = request.meta['item']
            requestNew.priority = request.priority + 100
            requestNew.dont_filter = True
            yield requestNew
        elif 'run' in url:
            print("该页为经营状况")
            request.meta['item']['run_html'] = response.text
            request.meta['item']['mid_requests'] = 2  # 谢鋆Request下载框架MID

            requestNew = Request(url=request.url.replace('run', 'fengxian'))
            requestNew.meta['item'] = request.meta['item']
            requestNew.priority = request.priority + 100
            requestNew.dont_filter = True
            yield requestNew
        elif 'fengxian' in url:
            print("该页为经营风险")
            request.meta['item']['fengxian_html'] = response.text
            request.meta['item']['mid_requests'] = 2  # 谢鋆Request下载框架MID

            requestNew = Request(url=request.url.replace('fengxian', 'report'))
            requestNew.meta['item'] = request.meta['item']
            requestNew.priority = request.priority + 100
            requestNew.dont_filter = True
            yield requestNew
        elif 'report' in url:
            print("该页为企业年报")
            request.meta['item']['report_html'] = response.text
            request.meta['item']['mid_requests'] = 2  # 谢鋆Request下载框架MID

            requestNew = Request(url=request.url.replace('report', 'history'))
            requestNew.meta['item'] = request.meta['item']
            requestNew.priority = request.priority + 100
            requestNew.dont_filter = True
            yield requestNew
        elif 'history' in url:
            print("该页为历史股东")
            request.meta['item']['history_html'] = response.text
            request.meta['item']['mid_requests'] = 2  # 谢鋆Request下载框架MID
            print('存储数据')
            yield request.meta['item']

        else:
            print("跳转到了异常页,停止抓取")
            print(response.text)
            raise Exception("抓取异常,url不包括关键字,停止抓取")


if __name__ == '__main__':
    cmdline.execute("scrapy crawl redis_SpiderDemo".split())
