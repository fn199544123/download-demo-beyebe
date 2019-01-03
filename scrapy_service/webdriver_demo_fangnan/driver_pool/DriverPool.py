"""
一个webDriver池的简单实现
通过对webDriver池的管理,可以不再反复实例化webDriver对象,从而节约系统资源
使用方法:
1\使用单例方法实例化对象。
2\使用get方法同步（失败阻塞）或异步（失败抛出异常）获取对象。
3\使用完对象，及时归还。
"""
import threading
from queue import Queue

from scrapy_service.webdriver_demo_fangnan.driver_pool.DriverBean import WebDriverBean

DRIVER_NUM = 2


def synchronized(func):
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return lock_func


class WebDriverPool():
    # 多线程安全的单例模式实现
    __instance = None
    driverQueue = Queue()

    @synchronized
    def __new__(cls, *args, **kwargs):
        print(cls.__instance)
        if not cls.__instance:
            print("成功实例化")
            for i in range(DRIVER_NUM):
                cls.driverQueue.put(WebDriverBean())
            cls.__instance = super().__new__(cls)
        else:
            pass
            print("已经实例化")
        return cls.__instance

    def getOneDriver(self):
        return self.driverQueue.get().driver

    def getOneDriverNoWait(self):
        return self.driverQueue.get_nowait().driver

    def returnDriver(self, driver=None):
        """
        归还源生driver实例
        :param driver:
        :return:
        """
        driverBean = WebDriverBean(driver)
        self.driverQueue.put_nowait(driverBean)

    def queueSize(self):
        return self.driverQueue.qsize()


def createObj():
    WebDriverPool()


if __name__ == '__main__':

    for i in range(10):
        threading.Thread(target=createObj).start()
