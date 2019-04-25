# -*- coding:utf-8 -*-
# @Time    : 2018/7/24 10:54
# @Author  : Brady
# @File    : toolkit.py
# @Software: PyCharm
# @Contact : bradychen1024@gmail.com

import re
import os
import sys
import time
import pymongo
import logging
import shutil
import threading
import configparser
from functools import wraps

from pymongo import MongoClient

config = configparser.ConfigParser()
local_path = os.getcwd()
# print((local_path if 'extend' in local_path else local_path+'\extend') + '\config.ini')
config.read((local_path if 'extend' in local_path else local_path+'\extend') + '\config.ini')


def replace_all(filter_: list, string: str) -> str:
    """
    过滤所有字符
    :param filter_:要过滤的字符列表
    :param string:
    :return:
    """
    for filter_word in filter_:
        string = string.replace(filter_word, '')
    return string


def format_headers(string)->dict:
    """
    将在Chrome上复制下来的浏览器UA格式化成字典，以\n为切割点
    :param string: 使用三引号的字符串
    :return:
    """
    string = string.strip().replace(' ', '').split('\n')
    dict_ua = {}
    for key_value in string:
        dict_ua.update({key_value.split(':')[0]: key_value.split(':')[1]})
    return dict_ua


class SpiderLog(object):
    """
    日志模块
    """
    def __init__(self, level=logging.INFO):
        """
        获取日志对象
        :param level:  输出级别，写入级别为WARING
        :return: 日志对象
        """
        self.log_name = config['error_log']['log_name']
        # 日志文件夹名
        self.file_folder = (local_path if 'extend' in local_path else local_path+'\extend') + '\\' + config['error_log']['log_folder']
        self.level = level
        # 是否删除已存在的日志
        self.delete_existed_log = True if config['error_log']['delete_existed_log'] == 'True' else False
        self.logger = self.spider_log()

    @ staticmethod
    def format_error_msg(file_name, func_name, error_msg, func_stack, error_url=None):
        """
        格式化输出错误
        :param file_name: 文件名
        :param func_name: 函数名
        :param error_msg: 错误信息
        :param func_stack: 错误栈堆
        :param error_url: 异常的链接
        :return:
        """
        if error_url:
            error_info = '''
                detail_error_info
                ##################
                file_name: {},
                func_name: {},
                error_msg: {},
                error_url: {},
                func_stack:
                \t{}
                ##################
            '''.replace(' ', '').format(file_name, func_name, error_msg, error_url, func_stack)
        else:
            error_info = '''
                            detail_error_info
                            ##################
                            file_name: {},
                            func_name: {},
                            error_msg: {},
                            func_stack:
                            \t{}
                            ##################
                        '''.replace(' ', '').format(file_name, func_name, error_msg, func_stack)
        return error_info

    def spider_log(self):
        if os.path.exists(self.file_folder):
            try:
                if self.delete_existed_log:
                    shutil.rmtree(self.file_folder)
                    os.mkdir(self.file_folder)
                else:
                    # 每隔一段时间就删除日志文件
                    files_name = next(os.walk(self.file_folder))[2]
                    old_files = re.search('_([\d-]+)', files_name[0]).group(1)
                    new_files = re.search('_([\d-]+)', files_name[-1]).group(1)
                    old_time = time.mktime(time.strptime(old_files, "%Y-%m-%d"))
                    new_time = time.mktime(time.strptime(new_files, "%Y-%m-%d"))
                    _result = (int(new_time) - int(old_time)) / 24 / 60 / 60
                    if _result >= int(config['error_log']['save_days']):
                        shutil.rmtree(self.file_folder)
                        os.mkdir(self.file_folder)
            except PermissionError:
                # print('删除与创建日志文件夹异常')
                pass
        else:
            os.mkdir(self.file_folder)

        # logs_dir = os.path.realpath(logs_dir)
        create_time = time.strftime('%Y-%m-%d %H-%M-%S')
        # 创建一个logger
        logger = logging.getLogger(self.log_name)
        # 设置日志级别

        logger.setLevel(self.level)

        # 创建文件处理器
        file_handler = logging.FileHandler('%s/%s_%s.txt' % (self.file_folder, self.log_name, create_time),
                                           encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        # 创建输出处理器
        stream_handler = logging.StreamHandler()

        # 定义输出格式
        formatter = logging.Formatter('[%(asctime)s] - %(filename)s - [line:%(lineno)d] - [%(levelname)s]: %(message)s')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # 给logger添加处理器
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        return logger

    '''日志的五个级别对应以下的5个函数'''

    def debug(self, msg):
        """
        详细的信息,通常只出现在诊断问题上
        :param msg:
        :return:
        """
        self.logger.debug(msg)

    def info(self, msg):
        """
        确认一切按预期运行
        :param msg:
        :return:
        """
        self.logger.info(msg)

    def warn(self, msg):
        """
        一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低)。这个软件还能按预期工作。
        :param msg:
        :return:
        """
        self.logger.warning(msg)

    def error(self, msg):
        """
        更严重的问题,软件没能执行一些功能
        :param msg:
        :return:
        """
        self.logger.error(msg)

    def critical(self, msg):
        """
        一个严重的错误,这表明程序本身可能无法继续运行
        :param msg:
        :return:
        """
        self.logger.critical(msg)


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


def retry_wrapper(retry_times, exception=Exception, error_handler=None, interval=0.1):
    """
    函数重试装饰器
    :param retry_times: 重试次数
    :param exception: 需要重试的异常
    :param error_handler: 出错时的回调函数
    :param interval: 重试间隔时间
    :return:
    """
    def out_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    count += 1
                    if error_handler:
                        result = error_handler(func.__name__, count, e, *args, **kwargs)
                        if result:
                            count -= 1
                    if count >= retry_times:
                        raise
                    time.sleep(interval)
        return wrapper

    return out_wrapper


class KThread(threading.Thread):
    """A subclass of threading.Thread, with a kill()
    method.

    Come from:
    Kill a thread in Python:
    http://mail.python.org/pipermail/python-list/2004-May/260937.html
    """

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run  # Force the Thread to install our trace.
        threading.Thread.start(self)

    def __run(self):
        """Hacked run function, which installs the
        trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True


def timeout(seconds):
    """超时装饰器，指定超时时间
    若被装饰的方法在指定的时间内未返回，则抛出Timeout异常"""

    def timeout_decorator(func):
        """真正的装饰器"""

        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))

        def _(*args, **kwargs):
            result = []
            new_kwargs = {  # create new args for _new_func, because we want to get the func return val to result list
                'oldfunc': func,
                'result': result,
                'oldfunc_args': args,
                'oldfunc_kwargs': kwargs
            }
            thd = KThread(target=_new_func, args=(), kwargs=new_kwargs)
            thd.start()
            thd.join(seconds)
            alive = thd.isAlive()
            thd.kill()  # kill the child thread
            if alive:
                raise TimeoutException(u'function run too long, timeout %d seconds.' % seconds)
            else:
                try:
                    return result[0]
                except IndexError:
                    return result

        _.__name__ = func.__name__
        _.__doc__ = func.__doc__
        return _

    return timeout_decorator


class TimeoutException(Exception):
    """function run timeout"""


def get_datetime_now():
    """
    获取当前的日期与时间
    :return: 当前的日期与时间
    """
    return time.strftime('%Y-%m-%d %H:%M:%S')


config = configparser.ConfigParser()
config.read('extend/config.ini')
config.sections()
host = config['mongodb']['mg_host']
port = int(config['mongodb']['mg_port'])
db_name = config['mongodb']['mg_name']
user = config['mongodb']['mg_user']
pwd = config['mongodb']['mg_password']
client = pymongo.MongoClient(
    host=host,
    username=user,
    password=pwd,
    port=port
)
# dbClient=client[db_name]

def conn():
    CONN_ADDR1 = 'dds-wz95de22a1ba5c141819-pub.mongodb.rds.aliyuncs.com:3717'
    CONN_ADDR2 = 'dds-wz95de22a1ba5c142645-pub.mongodb.rds.aliyuncs.com:3717'
    REPLICAT_SET = 'mgset-14090243'
    username = 'root'
    password = 'Yinda2009'
    # 获取mongoclient
    client = MongoClient([CONN_ADDR1, CONN_ADDR2], replicaSet=REPLICAT_SET)
    client.admin.authenticate(username, password)

    return client
dbClient=conn()[db_name]

class MongoDbClient:
    def __init__(self, collection):
        self.collection = collection
        self.client = client

    def __enter__(self):
        return self.client[db_name][self.collection]

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def filter_all_char(filter_char: list, string: str)->str:
    """
    过滤所有字符
    :param filter_char:要过滤的字符列表
    :param string:
    :return:
    """
    for filter_word in filter_char:
        string = string.replace(filter_word, '')
    return string




if __name__ == '__main__':
    log = SpiderLog()
    print(log.format_error_msg('file_name', 'func_name', 'error_msg',  'func_stack', 'error_url'))