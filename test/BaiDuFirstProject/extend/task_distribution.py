# -*- coding: utf-8 -*-
import traceback
import queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager
import socket
import time
import os
import sys
from threading import Thread

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

"""
简单的分布式demo
"""


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


class TaskDistribution:
    def __init__(self, host, port, authkey, func):
        """
        :param host: 服务器ip
        :param port: 端口
        :param authkey: 授权键
        :param func: 运行的函数
        """
        self.host = host
        self.func = func
        self.manager = BaseManager(address=(host, port), authkey=authkey)
        BaseManager.register('get_task_queue', callable=return_task_queue)
        BaseManager.register('get_result_queue', callable=return_result_queue)

        self.spiders = ['1.baidu_shixin', '2.zhi_xing_xin_xi', '3.jian_she_tong', '4.baidu_yu_qing']

    def start_master(self):
        """
        主机
        """
        print('主机服务已开启')
        self.manager.start()
        signal_queue = self.manager.get_task_queue()
        result = self.manager.get_result_queue()
        sp1, sp2, sp3, sp4 = 0, 0, 0, 0
        try:
            while True:
                if sp1 >= 30:
                    print('1.百度失信mei有在采集,正在尝试重启程序-----------------')
                    os.system(r'start baidu_shixin.bat')
                    sp1 = 0
                if sp2 >= 30:
                    print('2.执行信息mei有在采集,正在尝试重启程序-----------------')
                    os.system(r'start zhi_xing.bat')
                    sp2 = 0
                if sp3 >= 30:
                    print('3.建设通mei有在采集,正在尝试重启程序-----------------')
                    os.system('start jianshetong.bat')
                    sp3 = 0
                if sp4 >= 30:
                    print('4.百度舆情mei有在采集,正在尝试重启程序-----------------')
                    os.system('start baidu_yuqing.bat')
                    sp4 = 0
                sp1 += 1
                sp2 += 1
                sp3 += 1
                sp4 += 1
                if signal_queue.qsize() > 2:
                    signal = signal_queue.get()

                    if signal == self.spiders[0]:
                        print('-----------------1.百度失信正在采集')
                        sp1 = 0
                    if signal == self.spiders[1]:
                        print('-----------------2.执行信息有在采集')
                        sp2 = 0
                    if signal == self.spiders[2]:
                        print('-----------------3.建设通有在采集')
                        sp3 = 0
                    if signal == self.spiders[3]:
                        print('-----------------4.百度舆情有在采集')
                        sp4 = 0
                else:
                    print('没用收到采集信号,等待1秒')
                    time.sleep(1)
                    # if not signal_queue.qsize():
                    #     print('没用采集在运行，正在尝试重启程序')
                    # os.system('start baidu_shixin.bat')
                    # while not task.qsize() < 10:
                    #     # 限制任务队列长度，减少占用内容
                    #     _ = result.get()
        except Exception as error:
            print(error)
            print(traceback.format_exc())
        finally:
            self.manager.shutdown()
            print('master exit.')

    def start_slave(self):
        """
        从机
        """
        print('从机服务已开启')
        self.manager.connect()
        func = self.func
        signal = self.manager.get_task_queue()
        result = self.manager.get_result_queue()
        # 多线程运行
        while True:
            try:
                signal.put(func(), timeout=10)
                # result.put('result')
            except IOError as e:
                print(e)
                break
            except queue.Empty:
                print('task queue is empty.')
        # 处理结束:
        print('worker exit.')

    def start(self):
        freeze_support()
        local_name = socket.getfqdn(socket.gethostname())
        ip = socket.gethostbyname(local_name)
        print(ip)
        # print myname, ip, self.host
        # ip = '58.221.49.26'
        # ip = '192.168.232.1'
        if 'task_distribution.py' not in sys.argv[0]:
            ip = ''
        if ip == self.host:
            self.start_master()
        else:
            self.start_slave()
        return True

    def close(self):
        print('从机已关闭')
        self.manager.shutdown()


if __name__ == '__main__':
    def func():
        time.sleep(1)
        return '哈哈'


    t = TaskDistribution('192.168.232.1', 8180, 'brady'.encode('utf-8'), func)
    t.start()
