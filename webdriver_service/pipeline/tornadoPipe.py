# -*- coding:utf8 -*-
import json
import traceback

import tornado.ioloop
import tornado.web
import tornado.httpserver

from logging_utils.cJsonEncoder import CJsonEncoder
from webdriver_service.driver_pool.driverPool import WebDriverPool
from webdriver_service.factory import fapiaoImpl


class ChangeModel(tornado.web.RequestHandler):
    def post(self):
        return self.get()

    def get(self):
        try:
            arguments = self.request.arguments
            for key in arguments:
                arguments[key] = arguments[key][-1].decode()
            msg = WebDriverPool().getOneDriverNoWait().deal(arguments)
            self.write(json.dumps(msg, ensure_ascii=False, cls=CJsonEncoder))

        except:
            if 'Empty' in traceback.format_exc():
                self.write({'state': 701, 'errMsg': "系统繁忙！无空闲实例,请稍后再试"})
                traceback.print_exc()
                return
            self.write({'state': 799, 'errMsg': "异常\n" + traceback.format_exc()})
            traceback.print_exc()
            return


def make_app():
    return tornado.web.Application([
        (r"/test.go", ChangeModel),
    ])
