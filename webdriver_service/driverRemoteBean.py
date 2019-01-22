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
    def __init__(self, MyPool, driver=None, headless=False):
        self.myPool = MyPool
        mylog.info("正在尝试创建一个Driver实例")
        while True:
            ipList = ['localhost', 'dockerhost', '172.18.0.1', '172.18.0.2', '172.18.0.3', '172.18.0.4', '172.18.0.5',
                      '172.18.0.6','172.18.0.7','172.18.0.8','172.18.0.9']
            # cmd = """/sbin/ip route|awk '/default/ { print  $3,"\tdockerhost" }'"""
            # ipNow = os.popen(cmd).read()
            # if ipNow is not None and ipNow != "":
            #     ipStrList = self.__getIP(ipNow)
            #     if len(ipStrList) != 0:
            #         mylog.info("宿主机环境变量获取成功", ipStrList)
            #         ipList.extend(ipStrList)
            # else:
            #     mylog.info("未成功执行指令")
            for ip in ipList:
                try:
                    mylog.info("正在尝试使用", ip)
                    self.driver = webdriver.Remote(command_executor="http://{}:4444/wd/hub".format(ip),
                                                   desired_capabilities=DesiredCapabilities.CHROME)
                    self.driver.maximize_window()
                    # 数据库加载
                    self.client = pymongo.MongoClient(host=self.MONGODB_HOST, port=self.MONGODB_PORT)
                    self.db = self.client[self.MONGODB_DBNAME]
                    self.db.authenticate(self.MONGODB_USER, self.MONGODB_PASSWORD)
                    return
                except:
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
