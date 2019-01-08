import platform

import os
from selenium import webdriver

options = webdriver.ChromeOptions()


class WebDriverBean():
    __instance = None

    def __init__(self, driver=None):
        if driver is None:
            print("系统检测", platform.system())
            if 'inux' in platform.system():
                driverPath = self.__filePath('chromedriver/linux/chromedriver')
                print("检测到系统是", "Linux", driverPath)
            elif 'indows' in platform.system():
                driverPath = self.__filePath('chromedriver/windows/chromedriver.exe')
                print("检测到系统是", "Windows", driverPath)
            elif 'arwin' in platform.system():
                driverPath = self.__filePath('chromedriver/mac/chromedriver')
                print("检测到系统是", "Mac系统（其他系统）", driverPath)
            else:
                print("不知道是什么系统,无法实例化WebDriver对象")
                raise Exception("不知道是什么系统,无法实例化Driver对象")
            self.driver = webdriver.Chrome(executable_path=driverPath, chrome_options=options)

    def __filePath(self, basePath):
        # 往上查5个级别,看看是否有目标文件,没有最终抛出异常
        for i in range(5):
            if os.path.exists(basePath):
                return basePath
            else:
                basePath = "../" + basePath
        raise Exception("未找到对应的ChromeDriver驱动文件")
