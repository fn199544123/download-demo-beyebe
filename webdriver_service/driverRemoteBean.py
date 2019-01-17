import platform

import pymongo
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from webdriver_service.driverBean import WebDriverImp


class WebDriverRemoteImp(WebDriverImp):
    def __init__(self, MyPool, driver=None, headless=False):
        self.myPool = MyPool
        print("正在尝试创建一个Driver实例")
        self.driver = webdriver.Remote(command_executor="http://192.168.10.61:4444/wd/hub",
                                       desired_capabilities=DesiredCapabilities.CHROME)
        # 数据库加载
        self.client = pymongo.MongoClient(host=self.MONGODB_HOST, port=self.MONGODB_PORT)
        self.db = self.client[self.MONGODB_DBNAME]
        self.db.authenticate(self.MONGODB_USER, self.MONGODB_PASSWORD)
