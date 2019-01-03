"""
一个webDriver池的简单实现
通过对webDriver池的管理,可以不再反复实例化webDriver对象,从而节约系统资源
使用方法:
1\使用单例方法实例化对象。
2\使用get方法同步（失败阻塞）或异步（失败抛出异常）获取对象。
3\使用完对象，及时归还。
"""
from queue import Queue

from scrapy_service.webdriver_demo_fangnan.driver_pool.DriverBean import WebDriverBean

DRIVER_NUM = 2


class WebDriverPool():
    # 单例模式实现
    __instance = None
    driverQueue = Queue()

    def __new__(cls, *args, **kwargs):
        print(cls.__instance)
        if not cls.__instance:
            for i in range(DRIVER_NUM):
                cls.driverQueue.put(WebDriverBean())
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def getOneDriver(self):
        return self.driverQueue.get()

    def getOneDriverNoWait(self):
        return self.driverQueue.get_nowait()

    def returnDriver(self, driver=None):
        self.driverQueue.put_nowait(driver)

    def queueSize(self):
        return self.driverQueue.qsize()


if __name__ == '__main__':
    driver1 = WebDriverPool().getOneDriverNoWait()
    print(WebDriverPool().queueSize())
    driver2 = WebDriverPool().getOneDriver()
    print(WebDriverPool().queueSize())
    WebDriverPool().returnDriver(driver2)
    print(WebDriverPool().queueSize())
    driver3 = WebDriverPool().getOneDriver()
    print(WebDriverPool().queueSize())
    driver4 = WebDriverPool().getOneDriverNoWait()
    print(WebDriverPool().queueSize())
