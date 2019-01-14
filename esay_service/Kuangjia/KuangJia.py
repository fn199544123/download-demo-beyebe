# -*- coding:utf-8 -*-
import json
import traceback
import tornado.web
from tornado.options import define, options
from analysis import analysize
import time


define("port", default=9001, help="run on the given port", type=int)

total_num = 0
fail_num = 0

def IDEncodeDecode(str):
    strA = str[0]
    strB = str[-1]
    strMid = str[1:len(str) - 1]
    return strA + strMid[::-1] + strB

class Timer(object):
    """
    计时器，对于需要计时的代码进行with操作：
    with Timer() as timer:
        ...
        ...
    print(timer.cost)
    ...
    """
    def __init__(self, start=None):
        self.start = start if start is not None else time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.cost = self.stop - self.start
        return exc_type is None

class IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_header("Access-Control-Allow-Origin", "*")

    # get是范例数据，是假的，没有用的
    def get(self):
        global total_num, fail_num
        dataDict = {'data': {}, 'errMsg': 'success!', 'state': 200}
        dataDict['total_num'] = total_num
        dataDict['fail_num'] = fail_num
        self.write(json.dumps(dataDict, ensure_ascii=False))

    def post(self):
        global total_num, fail_num
        dataDict = {'errMsg': ['success!'], 'state': 200, 'data': {}, 'handleTime': '', 'version': 'V0.2'}
        try:
            with Timer() as timer:
                try:
                    # 没有赋值则为None
                    html = self.get_argument('html', None)
                    url = self.get_argument('url', None)
                    _cid = self.get_argument('cid', None)
                    companyName = self.get_argument('companyName', None)
                    type = self.get_argument('type', None)
                    if (type == 1 or type == 2) and html is None:
                        dataDict['state'] = 501
                        dataDict['errMsg'] = "POST-HTML data miss！"
                    if type == '1':
                        dataDict['data'] = analysize.next_list(html)
                    elif type == '2':
                        # 模块1,H5解析
                        dataDict['data'].update(analysize.parse_jibenxinxi(html))
                        if dataDict['data']['jibenxinxi']['cid']:
                            cid = dataDict['data']['jibenxinxi']['cid']
                            cid = IDEncodeDecode(cid)
                        elif _cid:
                            cid = _cid
                        # 模块2,股权穿透图
                        if cid:
                            dataDict['data'].update(analysize.parseGuQuanJiaGouTu(cid))
                    # 收费API-法律诉讼-裁判文书
                    elif type == '3':
                        if companyName:
                            FLSS_CaiPanWenShu = analysize.parse_FLSS_CaiPanWenShu(companyName)
                            # JYFX_JingYingYiChang = analysize.parse_JYFX_JingYingYiChang(companyName)
                            if FLSS_CaiPanWenShu.get('error'):
                                dataDict['errMsg'].append(FLSS_CaiPanWenShu.get('error'))
                            else:
                                dataDict['data'].update(FLSS_CaiPanWenShu)
                            # if JYFX_JingYingYiChang.get('error'):
                            #     dataDict['errMsg'].append(JYFX_JingYingYiChang.get('error'))
                            # else:
                            #     dataDict['data'].update(JYFX_JingYingYiChang)
                    #收费API-招聘信息
                    elif type == '4':
                        if companyName:
                            ZhaoPinXinXi = analysize.parse_ZhaoPinXinXi(companyName)
                            if ZhaoPinXinXi.get('error'):
                                dataDict['errMsg'].append(ZhaoPinXinXi.get('error'))
                            else:
                                dataDict['data'].update(ZhaoPinXinXi)
                    #收费API-企业年报
                    elif type == '5':
                        if companyName:
                            QYNB = analysize.parse_QYNB(companyName)
                            if QYNB.get('error'):
                                dataDict['errMsg'].append(QYNB.get('error'))
                            else:
                                dataDict['data'].update(QYNB)
                    #收费API-知识产权
                    elif type == '6':
                        if companyName:
                            ShangBiaoXinXi = analysize.parse_ZSCQ_ShangBiaoXinXi(companyName)
                            if ShangBiaoXinXi.get('error'):
                                dataDict['errMsg'].append(ShangBiaoXinXi.get('error'))
                            else:
                                dataDict['data'].update(ShangBiaoXinXi)
                            ZhuanLiXinXi = analysize.parse_ZSCQ_ZhuanLiXinXi(companyName)
                            if ZhuanLiXinXi.get('error'):
                                dataDict['errMsg'].append(ZhuanLiXinXi.get('error'))
                            else:
                                dataDict['data'].update(ZhuanLiXinXi)
                            RuanJianZhuZuoQuan = analysize.parse_ZSCQ_RuanJianZhuZuoQuan(companyName)
                            if RuanJianZhuZuoQuan.get('error'):
                                dataDict['errMsg'].append(RuanJianZhuZuoQuan.get('error'))
                            else:
                                dataDict['data'].update(RuanJianZhuZuoQuan)
                    else:
                        dataDict['state'] = 502
                        dataDict['errMsg'] = "Type not recognized"
                except AttributeError:
                    print(traceback.print_exc())
                    dataDict['state'] = 544
                    dataDict['errMsg'] = "检查post参数:" + self.get_argument('html', None)
                except:
                    print(traceback.print_exc())
                    dataDict['state'] = 599
                    dataDict['errMsg'] = traceback.format_exc()
                    fail_num = fail_num + 1
            dataDict['handleTime'] = timer.cost
        except AttributeError:
            dataDict['state'] = 545
            dataDict['errMsg'] = "检查计时器"
        self.write(json.dumps(dataDict, ensure_ascii=False))
        total_num = total_num + 1

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[('/beyebe/parse.go', IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('[hedgehog]tornado 启动')
    tornado.ioloop.IOLoop.instance().start()
