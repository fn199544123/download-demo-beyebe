# 同步修饰器
import threading

import time

"""
同步装饰器
TODO 一个巨大的缺陷，一个同步锁在代码里只能出现一次。
TODO 如果出现两次，可能会互相竞争。
"""


def synchronized(f):
    global mutex
    if not 'mutex' in dir():
        mutex = threading.Lock()
    def newDef(self):
        # print('【同步锁】修饰器装饰代码')
        mutex.acquire(True)
        f(self)
        mutex.release()
        # print('【同步锁】修饰器归还锁')
        return newDef


# @synchronized
def doSomething(i):
    print("打印", i)
    time.sleep(1)


if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=doSomething, args=(i,)).start()
