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

from selenium.webdriver.chrome.webdriver import WebDriver

from logging_utils.log import mylog
from webdriver_service.driverBean import WebDriverImp
from webdriver_service.loginDriverImp import LoginDriverImp


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
    def __new__(cls, dBean=WebDriverImp, num=1, headless=False, *args, **kwargs):

        if not cls.__instance:
            mylog.info("成功实例化")
            cls.__instance = super().__new__(cls)
            for i in range(num):
                cls.driverQueue.put(dBean(cls.__instance, headless=headless))

        else:
            mylog.info("已经实例化")
            pass
        return cls.__instance

    def getOneDriver(self):
        return self.driverQueue.get()

    def getOneDriverNoWait(self):
        return self.driverQueue.get_nowait()

    def returnDriver(self, driverBean):
        """
        归还源生driver实例
        :param driver:
        :return:
        """
        self.driverQueue.put_nowait(driverBean)

    def queueSize(self):
        return self.driverQueue.qsize()


if __name__ == '__main__':
    WebDriverPool(dBean=LoginDriverImp, num=1).getOneDriver().deal()
