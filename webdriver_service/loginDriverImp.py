from logging_utils.log import mylog
from webdriver_service.driverBean import WebDriverImp


class LoginDriverImp(WebDriverImp):

    def __init__(self, MyPool, driver=None, headless=False, data=None):
        super().__init__(MyPool, driver, headless, data=data)
        while True:
            try:
                print("正在进行登陆")
                self._login()  # 进行默认的登陆操作
                break
            except:
                print("登陆出错,重启浏览器尝试重新登陆")
                self.restartDriver()

    def _login(self):
        print("覆写该登陆方法,完成任务和操作")
        self.driver.get("http://www.163.com")
        pass

    def restartDriver(self):
        self.driver.quit()
        self.initDriver(self.driver, self.headless)
        self._login()
