import platform
import traceback

import os

import pymongo
import time

import re
import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from logging_utils.log import mylog
from webdriver_service.driverBean import WebDriverImp


class WebDriverRemoteImp(WebDriverImp):
    def __init__(self, MyPool, driver=None, headless=False, data=None):
        self.myPool = MyPool
        mylog.info("正在尝试创建一个Driver实例")
        while True:
            # 这里一大长串地址,是可以作为webdriver对象的地址
            # 但是,你不要错误理解了,比如你觉得前面的优先级大，互相实例会抢，从而修改这个基类
            # 其实这下面的地址无论你怎么设置，理论上只有一个可以ping通（各自ping通自己的），哪怕你起了10个webdriver
            # 神奇吧！你好奇怎么控制的分发？
            # 使用docker network create指令
            ipList = ['localhost', 'dockerhost',
                      '172.18.0.1', '172.18.0.2', '172.18.0.3',
                      '172.19.0.1', '172.19.0.2', '172.19.0.3',
                      '172.20.0.1', '172.20.0.2', '172.20.0.3',
                      '172.21.0.1', '172.21.0.2', '172.21.0.3',
                      '172.22.0.1', '172.22.0.2', '172.22.0.3',
                      ]

            for ip in ipList:
                urlTest = "http://{}:{}/".format(ip, str(self.getDriverPort()))
                try:
                    requests.get(urlTest, timeout=3)
                except:
                    print("测试失败", "跳过该webdriver", urlTest)
                    continue
                try:
                    mylog.info("正在尝试使用", ip)
                    self.driver = webdriver.Remote(
                        command_executor="http://{}:{}/wd/hub".format(ip, str(self.getDriverPort())),
                        desired_capabilities=DesiredCapabilities.CHROME)

                    self.driver.implicitly_wait(7)
                    self.driver.set_page_load_timeout(7)  # 数据库加载
                    self.driver.set_script_timeout(7)
                    self.client = pymongo.MongoClient(host=self.MONGODB_HOST, port=self.MONGODB_PORT)
                    self.db = self.client[self.MONGODB_DBNAME]
                    self.db.authenticate(self.MONGODB_USER, self.MONGODB_PASSWORD)
                    return
                except:
                    mylog.info(traceback.format_exc())
                    mylog.info("尝试失败,尝试使用下一个", ip)
                    pass
                    # traceback.mylog.info_exc()

            mylog.error("构建DOCKER-WEBDRIVER出现异常,最大的可能是因为未开启宿主机WEBDRIVER-DOCKER服务")
            mylog.error("请遵循文档,启动standalone-chrome:3.141.59-dubnium DOCKER服务,暴露内网4444端口服务再试")
            mylog.error(
                "并且关闭防火墙或开通指定端口，比如运行systemctl stop firewalld 或者 firewall-cmd --zone=public --add-port=2181/tcp --permanent + firewall-cmd --reload")
            mylog.info("系统将会在30秒后重试")
            time.sleep(30)

    def __getIP(self, ipStr):
        ip_list = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', ipStr, re.S)
        return ip_list

    def test(self):
        ipStr = """
        [2019-01-21 10:58:44,829] - log.py [Line:45] - [INFO]-[thread:139682587109120]-[process:1] - ('宿主机量获取成功', '172.17.0.1 \tdockerhost\n')
        """
        return self.__getIP(ipStr)

    def getDriverPort(self):
        return 4444
