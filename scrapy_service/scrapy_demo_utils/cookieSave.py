"""
这个模块使用webdriver保存登陆cookie
"""
import json
import time
import uuid

import requests
import sys
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

# 企查查账号:18923477217
from logging_utils.log import mylog

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    # 更换头部
    mylog.info("启动driver")
    # driver = webdriver.Chrome(executable_path='mac/chromedriver', chrome_options=options)
    mylog.info(sys.platform)
    if 'indow' in sys.platform:
        mylog.info("识别是Windows机器,启动webdriver")
        driver = webdriver.Chrome(executable_path='webdriver/windows/chromedriver.exe', chrome_options=options)
    elif 'darwin' in sys.platform:
        mylog.info("识别是MacOS机器,启动webdriver")
        driver = webdriver.Chrome(executable_path='webdriver/mac/chromedriver', chrome_options=options)
    elif 'linux' in sys.platform:
        mylog.info("识别是Linux机器,启动webdriver")
        driver = webdriver.Chrome(executable_path='webdriver/linux/chromedriver', chrome_options=options)
    else:
        mylog.info("未能识别机器")
        raise Exception("机器型号未知")
    # driver.maximize_window()
    # mylog.info("发起请求")
    # driver.get('https://www.baidu.com')
    driver.get('https://www.qichacha.com/')


    passMsg = input("输入任意值完成操作")
    try:
        mylog.info("保存截图")
        driver.save_screenshot('web_msg/full_snap.png')

    # alert() confirm() prompt()异常处理
    except UnexpectedAlertPresentException as errAlert:
        mylog.info(errAlert)
        mylog.info("这个异常是指还有弹出的alert没有处理")
        alertTag = driver.switch_to_alert()
        mylog.info("弹出内容消息", alertTag.text)
        alertTag.send_keys()
        alertId = uuid.uuid1()
        mylog.info("弹出内容ID", alertId)
        driver.save_screenshot('web_msg/full_snap_alert_{}.png'.format(alertId))
        with open("web_msg/alert_{}.txt", "w") as fp:
            fp.write(alertTag.text)

    mylog.info("保存cookie")
    cookies = driver.get_cookies()
    with open("web_msg/cookies_qichacha.txt", "w") as fp:
        json.dump(cookies, fp)
    mylog.info("保存html")
    html = driver.page_source
    with open("web_msg/test.web_msg", "w") as fp:
        fp.write(html)
