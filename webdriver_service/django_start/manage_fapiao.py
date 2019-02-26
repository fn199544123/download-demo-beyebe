#!/usr/bin/env python
import sys
import os

sys.path.append("../../")  # 解决潜在的路径依赖问题
sys.path.append("/root/scrapy-demo-beyebe")  # 解决潜在的路径依赖问题

from webdriver_service.factory.fapiaoImpl import fapiaoImpl

from django.http import HttpResponse
from webdriver_service.driver_pool.driverPool import WebDriverPool

"""
启动selenium
docker run -d -p 5440:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome
"""
# http://localhost:9088/spider/fapiao.go?fpdm=1100182130&fphm=15024752&kprq=20180614&kjje=18679.25
# http://localhost:9088/spider/fapiao.go?fpdm=4403174320&fphm=03738308&kprq=20181010&jym=964175
# http://localhost:9088/spider/fapiao.go?fpdm=4403181130&fphm=27671246&kprq=20180920&kjje=351.69
# http://localhost:9088/spider/fapiao.go?fpdm=011001800211&fphm=28519832&kprq=20190109&kjje=1020&jym=07842591941327323876
# http://39.108.188.34:9088/spider/fapiao.go?fpdm=011001800211&fphm=28519832&kprq=20190109&kjje=1020&jym=07842591941327323876
# http://39.108.188.34:9088/spider/fapiao.go?fpdm=1100182130&fphm=15024752&kprq=20180614&kjje=18679.25
# http://39.108.188.34:9088/spider/fapiao.go?fpdm=4403174320&fphm=03738308&kprq=20181010&jym=964175
# http://39.108.188.34:9088/spider/fapiao.go?fpdm=4403181130&fphm=27671246&kprq=20180920&kjje=351.69
# http://39.108.188.34:9088/spider/fapiao.go?fpdm=011001800211&fphm=28519832&kprq=20190109&kjje=1020&jym=07842591941327323876
# http://39.108.188.34:9088/spider/fapiao.go?fpdm=044031800211&fphm=28519832&kprq=20190215&kjje=42.93&jym=7006849628077367328

from django.conf.urls import url
from webdriver_service.django_start.django_start.urls import urlpatterns
from webdriver_service.django_start.django_start.view import changeModel

if __name__ == '__main__':

    # 演示时使用下面的代码
    # WebDriverPool(dBean=fapiaoImpl, num=1, headless=False)
    if 'inux' in sys.platform.system():
        WebDriverPool(dBean=fapiaoImpl, num=1, headless=True)
    else:
        WebDriverPool(dBean=fapiaoImpl, num=1, headless=False)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_start.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    args = [sys.argv[0], "runserver", "0.0.0.0:9088", "--noreload"]
    print(args)
    execute_from_command_line(args)
