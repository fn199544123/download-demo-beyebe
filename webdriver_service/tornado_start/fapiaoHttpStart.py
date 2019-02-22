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


# http://localhost:9088/spider/fapiao.go?fpdm=1100182130&fphm=15024752&kprq=20180614&kjje=18679.25
# http://localhost:9088/spider/fapiao.go?fpdm=4403174320&fphm=03738308&kprq=20181010&jym=964175
# http://localhost:9088/spider/fapiao.go?fpdm=4403181130&fphm=27671246&kprq=20180920&kjje=351.69
# http://39.108.188.34:9088/spider/fapiao.go?fpdm=1100182130&fphm=15024752&kprq=20180614&kjje=18679.25
def make_app_fapiao():
    return tornado.web.Application([
        (r"/spider/fapiao.go", ChangeModel),
    ])


if __name__ == "__main__":
    WebDriverPool(dBean=fapiaoImpl, num=1, headless=False)

    app = make_app_fapiao()
    sockets = tornado.netutil.bind_sockets(9088)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.add_sockets(sockets)
    print("Server Start Ok.....")
    # http_server.tornado_start(5)
    tornado.ioloop.IOLoop.instance().start()
