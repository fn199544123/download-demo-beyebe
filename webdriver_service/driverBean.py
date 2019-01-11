import platform

import os

import pymongo
from selenium import webdriver

from logging_utils import log
from logging_utils.log import mylog


class WebDriverImp():
    __instance = None
    myPool = None
    MONGODB_HOST = '192.168.10.9'
    MONGODB_USER = 'fangnan'
    MONGODB_PASSWORD = 'Fang135'
    MONGODB_PORT = 27017
    MONGODB_DBNAME = 'hedgehog_spider'

    def __init__(self, MyPool, driver=None, headless=False):
        self.myPool = MyPool
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        # 浏览器加载
        if driver is None:
            mylog.info("系统检测", platform.system())
            if 'inux' in platform.system():
                driverPath = self.__filePath('chromedriver/linux/chromedriver')
                mylog.info("检测到系统是", "Linux", driverPath)
            elif 'indows' in platform.system():
                driverPath = self.__filePath('chromedriver/windows/chromedriver.exe')
                mylog.info("检测到系统是", "Windows", driverPath)
            elif 'arwin' in platform.system():
                driverPath = self.__filePath('chromedriver/mac/chromedriver')
                mylog.info("检测到系统是", "Mac系统（其他系统）", driverPath)
            else:
                mylog.info("不知道是什么系统,无法实例化WebDriver对象")
                raise Exception("不知道是什么系统,无法实例化Driver对象")
            self.driver = webdriver.Chrome(executable_path=driverPath, chrome_options=options)
        # 数据库加载

        self.client = pymongo.MongoClient(host=self.MONGODB_HOST, port=self.MONGODB_PORT)
        self.db = self.client[self.MONGODB_DBNAME]
        self.db.authenticate(self.MONGODB_USER, self.MONGODB_PASSWORD)

    def setPool(self, MyPool):
        self.myPool = MyPool

    def __filePath(self, basePath):
        # 往上查5个级别,看看是否有目标文件,没有最终抛出异常
        for i in range(5):
            if os.path.exists(basePath):
                return basePath
            else:
                basePath = "../" + basePath
        raise Exception("未找到对应的ChromeDriver驱动文件")

    # 将deal私有化，可复写，框架使用deal_and_recover自动回收资源
    # 否则就需要调用者手动归还driver
    # ！！！driver资源开销很大，如果你看到这行注释，请慎行。
    def deal(self, input):
        try:
            isDup = self.duplicate(input)
            if type(isDup) == type({}):
                return isDup
            elif isDup == False:
                input.update(self._deal(input))
                self.save(input)
                mylog.info("数据存储成功")
                return input
            elif isDup == True:
                input.update({'state': 100, 'errMsg': '任务重复'})
                return input
            else:
                return isDup
        finally:
            self.myPool.returnDriver(self)
            mylog.info("自动归还Driver成功")

    # overwrite
    def _deal(self, input):
        mylog.info("覆写该方法,完成任务和操作")
        self.driver.get("http://www.baidu.com")
        input.update({'msg': 'error', 'state': 0})
        return input

    # 去重检查
    def duplicate(self, input):
        """
        请求前做去重检查
        :param input:
        :return: 返回ture代表已经重复
        返回false代表没有重复
        如果返回一个item就直接返回这个item。
        """
        return False

    # 存储方法
    def save(self, msg):
        self.db['auto_' + type(self).__name__].insert_one(msg)
