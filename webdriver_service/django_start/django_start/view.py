import json
import threading
import traceback

from django.http import HttpResponse

from logging_utils.cJsonEncoder import CJsonEncoder
from webdriver_service.driver_pool.driverPool import WebDriverPool


class MyThread(threading.Thread):
    def __init__(self, driver, input, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.driver = driver
        self.input = input

    def run(self):
        self.result = self.driver.deal(self.input)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def changeModel(request):
    try:

        if request.method == 'GET':
            arguments = dict(request.GET)
            for arg in arguments:
                if type(arguments[arg]) == type([]):
                    arguments[arg] = arguments[arg][0]
        elif request.method == 'POST':
            arguments = json.loads(request.body.decode())
        else:
            return "不支持除了GET和POST之外的请求方式"
        # 将每个参数的队列转换成单个结果

        if WebDriverPool().queueSize() > 0:
            msg = WebDriverPool().getOneDriverNoWait().deal(arguments)
        else:
            # 现在没有可用driver,所以暂时不下发任务
            msg = {"state": 701, "errMsg": "当前无可用Webdriver实例,通过参数stateMsg当前任务的工作状态。",
                   "stateMsg": WebDriverPool().getDriverState()}
        jsonStr = json.dumps(msg, ensure_ascii=False, cls=CJsonEncoder)
        return HttpResponse(jsonStr)
    except:
        if 'Empty' in traceback.format_exc():
            jsonStr = json.dumps({'state': 701, 'errMsg': "系统繁忙！无空闲实例,请稍后再试"}, ensure_ascii=False, cls=CJsonEncoder)
            traceback.print_exc()
            return HttpResponse(jsonStr)

        jsonStr = json.dumps({'state': 799, 'errMsg': "异常\n" + traceback.format_exc()}, ensure_ascii=False,
                             cls=CJsonEncoder)

        traceback.print_exc()
        return HttpResponse(jsonStr)


# 批量处理接口
def changeModelBatch(request):
    try:
        if request.method == 'GET':
            arguments = dict(request.GET)
            for arg in arguments:
                if type(arguments[arg]) == type([]):
                    arguments[arg] = arguments[arg][0]
        elif request.method == 'POST':
            arguments = json.loads(request.body.decode())
        else:
            return "不支持除了GET和POST之外的请求方式"

        # 将每个参数的队列转换成单个结果
        if WebDriverPool().queueSize() > 0:
            threads = []
            for itemData in arguments['data']:
                if 'result' in itemData:
                    for item in itemData['result']:
                        # msg = WebDriverPool().getOneDriver().deal(item)
                        driver = WebDriverPool().getOneDriver()
                        t = MyThread(driver, item)
                        threads.append(t)
                        t.start()
                else:
                    driver = WebDriverPool().getOneDriver()
                    t = MyThread(driver, itemData)
                    threads.append(t)
                    t.start()
            # 阻塞全部完成

            for threadNow in threads:
                threadNow.join()
            # 组装最终结果
            msg = {'result': [], 'errMsg': "结果请遍历result查看", 'state': 200}
            for threadNow in threads:
                msg['result'].append(threadNow.get_result())
            jsonStr = json.dumps(msg, ensure_ascii=False, cls=CJsonEncoder)
            return HttpResponse(jsonStr)
        else:
            # 现在没有可用driver,所以暂时不下发任务

            msg = {"state": 701, "errMsg": "当前无可用Webdriver实例,根据其他参数查看当前任务的工作状态。",
                   "stateMsg": WebDriverPool().getDriverState()}
        jsonStr = json.dumps(msg, ensure_ascii=False, cls=CJsonEncoder)
        return HttpResponse(jsonStr)


    except:
        if 'Empty' in traceback.format_exc():
            jsonStr = json.dumps({'state': 701, 'errMsg': "系统繁忙！无空闲实例,请稍后再试"}, ensure_ascii=False, cls=CJsonEncoder)
            traceback.print_exc()
            return HttpResponse(jsonStr)

        jsonStr = json.dumps({'state': 799, 'errMsg': "异常\n" + traceback.format_exc()}, ensure_ascii=False,
                             cls=CJsonEncoder)

        traceback.print_exc()
        return HttpResponse(jsonStr)
