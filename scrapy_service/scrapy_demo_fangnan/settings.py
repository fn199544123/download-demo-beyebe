# -*- coding: utf-8 -*-
# 一般来讲你不用改的设置
BOT_NAME = 'scrapy_demo_fangnan'

SPIDER_MODULES = ['scrapy_demo_fangnan.spiders']
NEWSPIDER_MODULE = 'scrapy_demo_fangnan.spiders'

ROBOTSTXT_OBEY = False  # 是否遵守ROBOTS协议,False为不遵守
# 你大概率需要关注的参数（都有注释）

# DOWNLOAD_DELAY = 1  # 在这里写delay远远好于代码中的sleep，这代表了一批多线程任务的间隔时间
CONCURRENT_REQUESTS = 1  # 异步线程数
DOWNLOADER_MIDDLEWARES = {

}  # 中间件,数越大优先级越小,在我的规范里一般在spider里定义
ITEM_PIPELINES = {
    'scrapy_demo_fangnan.pipelines.MongoPipeline': 1,
    # 'scrapy_demo_fangnan.pipelines.KafkaPipeline': 200,
    # 'scrapy_demo_fangnan.pipelines.LocalFilePipeline': 300,
    # 'scrapy_demo_fangnan.pipelines.OSSPipeline': 400,
}  # 管道

# MONGO数据库参数

# 友情提示,对于setting中的字段到底是什么,最好不要去网上查。
# 大部分都是自己写在中间件的from_crawler方法里。并不是强制的而是很随性的，查到也不一定对。
# 我这里加个LOVE来提醒大家，你可以全局搜索LOVE_来找到引用他的地方，并查看其不填写的默认值。


LOVE_MONGODB_HOST = '192.168.10.9'
LOVE_MONGODB_USER = 'fangnan'
LOVE_MONGODB_PORT = 27017
LOVE_MONGODB_PASSWORD = 'Fang135'
# LOVE_MONGODB_DBNAME = 'test'


REDIS_HOST = '192.168.10.9'
REDIS_PORT = 6379

# 指定 redis链接密码，和使用哪一个数据库
REDIS_PARAMS = {
    'password': '123456',
    'db': 15
}
