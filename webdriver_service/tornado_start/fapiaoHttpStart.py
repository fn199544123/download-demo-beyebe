import sys
import codecs


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())  # 解决潜在的中文编码问题
sys.path.append("../../")  # 解决潜在的路径依赖问题
sys.path.append("/root/scrapy-demo-beyebe")  # 解决潜在的路径依赖问题

print("依赖路径清单", sys.path)
from logging_utils.log import mylog
import tornado
import requests
from webdriver_service.driver_pool.driverPool import WebDriverPool
from webdriver_service.factory.fapiaoImpl import fapiaoImpl
from webdriver_service.pipeline.tornadoPipe import make_app, ChangeModel


def make_app_fapiao():
    return tornado.web.Application([
        (r"/spider/fapiao.go", ChangeModel),
    ])


if __name__ == "__main__":
    WebDriverPool(dBean=fapiaoImpl, num=1, headless=True)

    app = make_app_fapiao()
    sockets = tornado.netutil.bind_sockets(9088)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.add_sockets(sockets)
    print("Server Start Ok.....")
    # http_server.tornado_start(5)
    tornado.ioloop.IOLoop.instance().start()
