# -*- coding: UTF-8 -*-
'''
@描述：日志输入封装
@作者：CYH
@版本：V1.0
@创建时间：2016年11月28日 上午11:52:13
'''

import logging.handlers


class MyLog(logging.Logger):
    def __init__(self, filename=None):
        super().__init__(self)
        # 日志文件名
        if filename is None:
            filename = 'xincheng'
        self.filename = filename

        # 创建一个handler，用于写入日志文件 (每天生成1个，保留30天的日志)
        # # 按天输出
        # fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 7)
        # fh.suffix = "%Y-%m-%d.log"
        # 按秒输出
        fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'S', 1, 7)
        fh.suffix = "%Y-%m-%d_%H-%M-%S.log"


        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台 
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式 
        formatter = logging.Formatter(
            '[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler 
        self.addHandler(fh)
        self.addHandler(ch)


myLog = MyLog()
if __name__ == '__main__':
    myLog.error("test ERROR!")
# -*- coding: UTF-8 -*-
'''
@描述：日志输入封装
@作者：CYH
@版本：V1.0
@创建时间：2016年11月28日 上午11:52:13
'''

import logging.handlers


class MyLog(logging.Logger):
    def __init__(self, filename=None):
        super().__init__(self)
        # 日志文件名
        if filename is None:
            filename = 'pt.log'
        self.filename = filename

        # 创建一个handler，用于写入日志文件 (每天生成1个，保留30天的日志)
        fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 30)
        fh.suffix = "%Y%m%d-%H%M.log"
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.addHandler(fh)
        self.addHandler(ch)


if __name__ == '__main__':
    log = MyLog()
    log.error("test ERROR!")
