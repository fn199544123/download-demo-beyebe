import sys

sys.path.append("/scrapy-demo-beyebe")
print("依赖路径清单", sys.path)
from logging_utils.log import mylog
import tornado
from webdriver_service.driver_pool.driverPool import WebDriverPool
from webdriver_service.factory.fapiaoImpl import fapiaoImpl
from webdriver_service.pipeline.tornadoPipe import make_app

# http://localhost:9088/test.go?fpdm=1100182130&fphm=15024752&kprq=20180614&kjje=18679.25
# http://localhost:9088/test.go?fpdm=4403174320&fphm=03738308&kprq=20181010&kjje=964175
# http://localhost:9088/test.go?fpdm=4403181130&fphm=27671246&kprq=20180920&kjje=351.69


if __name__ == "__main__":
    WebDriverPool(dBean=fapiaoImpl, num=3, headless=True)
    app = make_app()
    sockets = tornado.netutil.bind_sockets(9088)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.add_sockets(sockets)
    print("Server Start Ok.....")
    tornado.ioloop.IOLoop.instance().start()
