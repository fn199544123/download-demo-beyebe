import json

import scrapy
import time
from scrapy import cmdline, Request

from logging_utils.log import mylog
from scrapy_service.scrapy_demo_fangnan.items import NewsDemoItem, BaiduHotwordItem, ShareItem

"""
抓取深圳交易所的上市公司数据

种子页：http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b1
难度系数：一颗星

2019/01/02

"""


class DemoSpider(scrapy.Spider):
    name = 'share'
    custom_settings = {
        'ITEM_PIPELINES': {'scrapy_demo_fangnan.pipelines.MongoPipeline': 300},
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 0,  # 单线程每五秒抓取一次
    }
    urlBase_shenzhen = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110x&TABKEY=tab1&PAGENO={}&random=0.7007904610394264"
    urlBase_shanghai = "http://query.sse.com.cn/security/stock/getStockListData2.do?isPagination=true&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage={}&pageHelp.pageSize=25&pageHelp.pageNo={}&pageHelp.endPage={}"

    def start_requests(self):
        # 重写该方法，可以下发任务，在这里我下发两个任务，可以下发多个任务。
        # 重写该方法callback，可以用不同的解析方式。如果不写（不推荐）,默认尝试使用parse这个方法。
        # 使用FormRequest代替Request方法，即代表使用POST方式下发

        # TODO 注意callback的函数名是不带括号的！

        for i in range(100):
            headers = {"Referer": "http://www.sse.com.cn/assortment/stock/list/share/"}
            request1 = scrapy.Request(self.urlBase_shanghai.format(str(i), str(i), str(i * 10 + 1)),
                                      callback=self.parse_shanghai_company,
                                      headers=headers)
            yield request1

        # for i in range(150):
        #     request1 = scrapy.Request(self.urlBase_shenzhen.format(str(i)), callback=self.parse_shenzhen_company)
        #     yield request1

        # 在这里写一下yield 和 return的区别
        # yield迭代器建立后，scrapy会假return执行完任务后，再用next()方法回到原来的地方继续执行
        # return就会直接停止,应用层的话，你用yield总归是没错的（嗯，多用yield)。
        # 详情：https://zhidao.baidu.com/question/1801721526050869707.html

        # 这里这块代码的逻辑结束了,你用两个都是可以的
        # return [request1]

    def parse_shenzhen_company(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        print("开始深圳上市公司的解析")

        # 可以使用xpath替代 response.xpath
        # print(response.text)
        jsonObj = json.loads(response.text)
        items = jsonObj[0]['data']
        for item in items:
            itemNow = ShareItem()
            itemNow['name'] = item['gsjc'].split('<u>')[1].split('</u>')[0]
            itemNow['code'] = item['zqdm']
            itemNow['tableName'] = "share_company"
            itemNow['etc'] = item
            yield itemNow

    def parse_shanghai_company(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        print("开始上海上市公司的解析")

        # 可以使用xpath替代 response.xpath
        # print(response.text)
        jsonObj = json.loads(response.text)
        items = jsonObj['result']
        for item in items:
            itemNow = ShareItem()
            itemNow['name'] = item['COMPANY_ABBR']
            itemNow['code'] = item['COMPANY_CODE']
            itemNow['tableName'] = "share_company"
            itemNow['etc'] = item
            yield itemNow


if __name__ == '__main__':
    cmdline.execute("scrapy crawl share".split())
