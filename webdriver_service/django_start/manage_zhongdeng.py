#!/usr/bin/env python
import datetime
import sys
import os
import platform

sys.path.append("../../")  # 解决潜在的路径依赖问题
sys.path.append("/root/scrapy-demo-beyebe")  # 解决潜在的路径依赖问题

from webdriver_service.factory.zhongdengImpl import zhongDengImpl
from webdriver_service.driver_pool.driverPool import WebDriverPool

"""
启动selenium
docker run -d -p 5441:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome
"""
# http://localhost:9089/spider/zhongdeng.go?companyName=深圳银泰保理有限公司
# http://39.108.188.34:9089/spider/zhongdeng.go?companyName=深圳银泰保理有限公司

# 中登网
if __name__ == '__main__':
    # 测试使用
    # WebDriverPool(dBean=zhongDengImpl, num=1, headless=False)
    print("启动时间startTime", datetime.datetime.now())
    onlineAccount = [
        {'account': 'ytbl007', 'keyword': 'ytbl007aDmin'},
        {'account': 'ytbl008', 'keyword': 'ytbl008aDmin'},
        {'account': 'ytbl009', 'keyword': 'ytbl009aDmin'}
    ]
    testAccount = [
        {'account': 'ytbl009', 'keyword': 'ytbl009aDmin'}
    ]
    if 'inux' in platform.system():
        WebDriverPool(dBean=zhongDengImpl, num=onlineAccount, headless=True)
    else:
        WebDriverPool(dBean=zhongDengImpl, num=testAccount, headless=False)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_start.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    args = [sys.argv[0], "runserver", "0.0.0.0:9089", "--noreload"]
    print(args)
    execute_from_command_line(args)
