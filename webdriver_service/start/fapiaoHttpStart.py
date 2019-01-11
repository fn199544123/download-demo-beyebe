import tornado

from logging_utils.log import mylog
from webdriver_service.driver_pool.driverPool import WebDriverPool
from webdriver_service.factory.fapiaoImpl import fapiaoImpl
from webdriver_service.pipeline.tornadoPipe import make_app

# http://localhost:9088/test.go?fpdm=1100182130&fphm=15024752&kprq=20180614&kjje=18679.25
if __name__ == "__main__":
    WebDriverPool(dBean=fapiaoImpl, num=1, headless=False)
    app = make_app()
    sockets = tornado.netutil.bind_sockets(9088)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.add_sockets(sockets)
    mylog.info("Server Start Ok.....")
    tornado.ioloop.IOLoop.instance().start()
