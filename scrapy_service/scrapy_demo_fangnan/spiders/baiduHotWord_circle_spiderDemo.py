import scrapy
import time
from scrapy import cmdline, Request

from scrapy_service.scrapy_demo_fangnan.items import NewsDemoItem, BaiduHotwordItem

"""
这个是循环抓取请求的实例，是最简单的例子。
这个实例实现了每五秒循环抓取百度热词,并存储入库。

种子页：http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b1
难度系数：一颗星

2019/01/02

"""


class DemoSpider(scrapy.Spider):
    name = 'circle_spiderDemo'
    custom_settings = {
        'ITEM_PIPELINES': {'scrapy_demo_fangnan.pipelines.MongoPipeline': 300},
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 5,  # 单线程每五秒抓取一次
    }

    def start_requests(self):
        # 重写该方法，可以下发任务，在这里我下发两个任务，可以下发多个任务。
        # 重写该方法callback，可以用不同的解析方式。如果不写（不推荐）,默认尝试使用parse这个方法。
        # 使用FormRequest代替Request方法，即代表使用POST方式下发

        # TODO 注意callback的函数名是不带括号的！
        request1 = scrapy.Request("http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b1",
                                  callback=self.parse_baidu_hotword, dont_filter=True)
        return [request1]

    def parse_baidu_hotword(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        print("开始百度热词的解析")
        # 可以使用xpath替代 response.xpath
        # print(response.text)
        items = response.css(".list-table")[0].css('.keyword')
        for item in items:
            itemA = item.css('a')[0]
            baiduHotwordItem = BaiduHotwordItem()
            baiduHotwordItem['word'] = itemA.css('::text').extract()[0]
            baiduHotwordItem['url'] = itemA.css('::attr(href)').extract()[0]
            yield baiduHotwordItem
        # 根据你的需要下发下一次任务，我随便修改了一下url代表这里可以变化，其实没实际的卵用
        urlNew = "http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b1&timeMyself={}".format(str(time.time()))
        request1 = scrapy.Request(urlNew, callback=self.parse_baidu_hotword, dont_filter=True)
        yield request1
        print("重新部署任务,5秒后重新抓取,在class的头部custom_settings设置")


if __name__ == '__main__':
    cmdline.execute("scrapy crawl circle_spiderDemo".split())
