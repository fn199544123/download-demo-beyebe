import scrapy
from scrapy import cmdline

from scrapy_service.scrapy_demo_fangnan.items import NewsDemoItem

"""
这个是一次性抓取请求的实例，是最简单的例子。
这个实例实现了抓取两个新闻站的几篇新闻,最后存储到MONGO数据库。

种子页：http://www.sohu.com https://www.sina.com.cn
难度系数：一颗星
"""


class DemoSpider(scrapy.Spider):
    name = 'single_spiderDemo'
    custom_settings = {
        'ITEM_PIPELINES': {'scrapy_demo_fangnan.pipelines.MongoPipeline': 300},
    }
    def start_requests(self):
        # 重写该方法，可以下发任务，在这里我下发两个任务，可以下发多个任务。
        # 重写该方法callback，可以用不同的解析方式。如果不写（不推荐）,默认尝试使用parse这个方法。
        # 使用FormRequest代替Request方法，即代表使用POST方式下发

        # TODO 注意callback的函数名是不带括号的！
        request1 = scrapy.Request("http://www.sohu.com", callback=self.parse_sohu)
        request2 = scrapy.Request("https://www.sina.com.cn", callback=self.parse_sina)
        return [request1, request2]

    def parse_sina(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        print("开始新浪网站的解析")
        # 可以使用xpath替代 response.xpath
        items = response.css(".newslist")[0].css('a')
        for item in items:

            if len(item.css('::text').extract()) > 0:
                newsDemoItem = NewsDemoItem()
                newsDemoItem['name'] = item.css('::text').extract()[0]
                newsDemoItem['url'] = item.css('::attr(href)').extract()[0]
                newsDemoItem['comefrom'] = 'sina'
                yield newsDemoItem


    def parse_sohu(self, response):
        print("开始搜狐网站的解析")
        items = response.css(".news")[0].css('a')
        for item in items:

            if len(item.css('::text').extract()) > 0:
                newsDemoItem = NewsDemoItem()
                newsDemoItem['name'] = item.css('::text').extract()[0]
                newsDemoItem['url'] = item.css('::attr(href)').extract()[0]
                newsDemoItem['comefrom'] = 'sohu'
                yield newsDemoItem


if __name__ == '__main__':
    cmdline.execute("scrapy crawl single_spiderDemo".split())
