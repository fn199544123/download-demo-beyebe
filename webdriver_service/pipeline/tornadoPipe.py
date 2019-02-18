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

    @tornado.web.asynchronous
    def get(self):
        try:
            arguments = self.request.arguments
            for key in arguments:
                arguments[key] = arguments[key][-1].decode()
            if WebDriverPool().queueSize() > 0:
                msg = WebDriverPool().getOneDriverNoWait().deal(arguments)
            else:
                # 现在没有可用driver,所以暂时不下发任务
                msg = {"state": 577,
                       "errMsg": "当前无可用Webdriver实例,根据其他参数查看当前任务的工作状态。"}
            jsonStr=json.dumps(msg, ensure_ascii=False, cls=CJsonEncoder)
            self.write(jsonStr)
            return
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
