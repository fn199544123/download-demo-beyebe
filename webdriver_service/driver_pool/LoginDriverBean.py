from scrapy_service.webdriver_demo_fangnan.driver_pool.DriverBean import WebDriverBean


class LoginDriverBean(WebDriverBean):
    def login(self):
        self.driver