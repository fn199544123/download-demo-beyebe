from logging_utils.log import mylog
from webdriver_service.driverBean import WebDriverImp


class LoginDriverImp(WebDriverImp):

    def _login(self):
        print("覆写该登陆方法,完成任务和操作")
        self.driver.get("http://www.163.com")
        pass

    def login(self):
        msg = self._login()
        self.myPool.returnDriver(self)
        print("完成登陆操作,自动归还Driver")
        return msg
