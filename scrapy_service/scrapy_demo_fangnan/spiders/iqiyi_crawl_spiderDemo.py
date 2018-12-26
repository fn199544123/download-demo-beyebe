# -*- coding: utf-8 -*-
from scrapy import cmdline
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

from scrapy_service.scrapy_demo_fangnan.items import IqiyiVideoItem

"""
这个是深度抓取请求的实例，相对来说比较难。
这个实例实现了四层抓取爱奇艺全站的视频链接，并存储入库。
无论是在主页上，还是在大标签或者翻页，只要深度不超过4层，都会抓取下来。

种子页：https://www.iqiyi.com
难度系数：四颗星
"""


class DemoCrawlSpider(CrawlSpider):
    name = 'crawlSpiderDemo'
    custom_settings = {
        'ITEM_PIPELINES': {'scrapy_demo_fangnan.pipelines.MongoPipeline': 300},
        'CONCURRENT_REQUESTS': 16,
        'DEPTH_LIMIT': 4  # 抓取深度最大是4
    }
    # 如果放开了让scrapy随便抓，广告什么的都都会当作子页面，我们限定iqiyi的站才是子页面，其他的不关注。
    # allowed_domains = ['https://www.iqiyi.com', 'http://www.iqiyi.com']
    # 之所以被注释掉了，是因为下面的LinkExtractor进行了详细配置，包含了allowed_domains。
    # 你可以视作allowed_domains是LinkExtractor继承的简单版

    # 种子站点，可以当作start_requests继承的简单版
    start_urls = ['https://www.iqiyi.com']
    # 定义提取超链接的提取规则，这个是指什么会被当作子链接，是allowed_domains的详细设置
    page_link = LinkExtractor(
        allow=('.'),  # 符合正则表达式参数的数据会被提取,这里设置所有
        deny=('baidu'),  # 符合正则表达式参数的数据禁止提取,这里随便设置一个百度
        allow_domains=('www.iqiyi.com'),  # 包含的域名中可以提取数据,这里设置成iqiyi
        # deny_domains=(),  # 包含的域名中禁止提取数据
        # deny_extensions=(),
        # restrict_xpath=(),  # 使用xpath提取数据，和allow共同起作用
        # tags=(),  # 根据标签名称提取数据
        # attrs=(),  # 根据标签属性提取数据
        # canonicalize=(),
        # unique=True,  # 剔除重复链接请求
        # process_value=None
    )
    # 定义爬取数据的规则,也就是一旦符合LinkExtractor，那么应该调哪个函数进行处理
    rules = {
        Rule(page_link, callback='parse_content', follow=True)
    }

    # 定义处理函数
    def parse_content(self, response):
        # 定义一个Item,用于存储数据

        # 获取整个我们需要的数据区域
        aList = response.css('a')
        for aTag in aList:
            try:
                if 'www.iqiyi.com/v_' in aTag.css('::attr(href)').extract()[0]:
                    #存储这个链接
                    item = IqiyiVideoItem()
                    item['title']=aTag.css('::text').extract()[0]
                    item['url'] = aTag.css('::attr(href)').extract()[0]

                    yield item
            except:
                print("这个a标签有问题（比如没有href）,跳过")
                continue

if __name__ == '__main__':
    cmdline.execute("scrapy crawl crawlSpiderDemo".split())
