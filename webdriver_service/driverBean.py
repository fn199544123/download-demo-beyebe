import datetime
import hashlib
import json
import platform

import os
import traceback
import uuid

import pymongo
import time

import redis
import sys
from PIL import Image
from selenium import webdriver

from logging_utils import log
from logging_utils.cJsonEncoder import CJsonEncoder
from logging_utils.log import mylog
from oss_aliyun.updateFileBeyebe import fileUpdate

"""
WebDriver基类
所有的Driver对象继承该对象完成任务
"""
try:
    redisPool14 = redis.ConnectionPool(host="121.9.245.183", password="BybAZ!@12", port=6379, db=14)
except:
    print("WARNING REDIS缓存服务器失效,不使用缓存进行处理")


class WebDriverImp():
    __instance = None
    myPool = None
    _state = "正在工作中...开发者并没有特别标记该实例的工作状态"
    # MONGODB_HOST = '192.168.10.9'
    # MONGODB_USER = 'fangnan'
    # MONGODB_PASSWORD = 'Fang135'
    # MONGODB_PORT = 27017
    # MONGODB_DBNAME = 'hedgehog_spider'
    REDIS_BUFFER = True  # 默认缓存
    REDIS_BUFFER_TIME = 60 * 60 * 24  # 默认缓存一天

    MONGODB_HOST = '58.221.49.26'
    MONGODB_USER = 'developer'
    MONGODB_PASSWORD = '123!@#qaz'
    MONGODB_PORT = 27017
    MONGODB_DBNAME = 'hedgehog_spider'
    driver = None
    headless = None

    def __init__(self, MyPool, driver=None, headless=False, data=None):
        self.myPool = MyPool
        self.headless = headless
        self.data = data
        self.initDriver(driver, headless)
        # 数据库加载

        self.client = pymongo.MongoClient(host=self.MONGODB_HOST, port=self.MONGODB_PORT)
        self.db = self.client[self.MONGODB_DBNAME]
        self.db.authenticate(self.MONGODB_USER, self.MONGODB_PASSWORD)

    def initDriver(self, driver, headless):
        options = webdriver.ChromeOptions()
        options.add_argument("--kiosk")
        options.add_argument("--start-maximized")
        options.add_argument("--start-fullscreen")
        store_path = './webDriver_download'
        if not os.path.exists(store_path):
            os.makedirs(store_path)

        prefs = {'download.default_directory': store_path,
                 'profile.default_content_settings.popups': 0,
                 "download.prompt_for_download": False}
        options.add_experimental_option("prefs", prefs)

        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')

        # 浏览器加载
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
            # self.driver.maximize_window()
            self.driver.implicitly_wait(7)
            self.driver.set_page_load_timeout(7)
            self.driver.set_script_timeout(7)

            self.enable_download_in_headless_chrome(store_path)

    def restartDriver(self):
        self.driver.close()
        self.driver.quit()
        self.driver = None
        self.initDriver(self.driver, self.headless)

    def setPool(self, MyPool):
        self.myPool = MyPool

    # 将deal私有化，可复写，框架使用deal_and_recover自动回收资源
    # 否则就需要调用者手动归还driver
    # ！！！driver资源开销很大，如果你看到这行注释，请慎行。
    def deal(self, input):
        try:
            try:
                isDup = self.duplicate(input)
            except:
                print("缓存服务器出现异常,有可能是输入参数不符合缓存结构或者缓存服务器异常,默认执行")
                isDup = False
            if type(isDup) == type({}) or type(isDup) == type("string"):
                return isDup
            elif isDup == False:
                inputMD5 = self.__getInputMD5(input)
                input.update(self._deal(input))
                if 'ERROR' not in str(input) and 'Traceback' not in str(input):
                    a = time.time()
                    try:
                        print('存储数据中不存在ERROR字符串,代表完全成功,进行缓存存储。（存储只是记录,不一定走缓存,不用担心）')
                        # MONGO缓存
                        print("【WARNING】mongo老卡，就不做MONGO缓存了暂时")
                        # self.insert(input)
                        # REDIS缓存
                        # r = redis.Redis(connection_pool=redisPool14)
                        # pipe = r.pipeline()
                        # pipe.set(inputMD5, json.dumps(input, cls=CJsonEncoder, ensure_ascii=False))
                        # pipe.expire(inputMD5, 60 * 60 * 24)
                        # pipe.execute()
                    except:
                        traceback.print_exc()
                        print("缓存失败")
                    finally:
                        print("缓存耗时", time.time() - a)
                else:
                    print("存储数据中存在ERROR字符串，代表着有部分失败，所以不进行缓存存储")
                print("数据存储成功")
                input['version'] = 'V1.4'
                return input
            elif isDup == True:
                input.update({'state': 100, 'errMsg': '任务重复并且调度期决定不做任何操作'})
                return input
            else:
                return isDup
        except:
            traceback.print_exc()
            return {'errMsg': traceback.format_exc(), 'state': 599}
        finally:
            self.myPool.returnDriver(self)
            print("自动归还Driver成功")

    # 去重检查
    def duplicate(self, input):
        """
        请求前做去重检查
        :param input:
        :return: 返回ture代表已经重复
        返回false代表没有重复
        如果返回一个item就直接返回这个item。
        """
        # 默认的去重还是有一点复杂的。首先依赖redis，拿到请求就缓存一个正在运行
        # 随后如果成功,还要覆盖缓存一个结果。
        # 这个结果默认在deal流程里是关闭的
        # 如要打开,在duplicate方法中操作实例对象的

        self.REDIS_BUFFER = True
        inputMD5 = self.__getInputMD5(input)
        r = redis.Redis(connection_pool=redisPool14)
        bufferItem = r.get(inputMD5)
        if bufferItem is not None:
            print("已存在缓存,进一步确定缓存形式")
            if 'DOING_MISSION!!wait_for_few_time!' in bufferItem.decode():
                raise Exception("数据正在处理!,请稍后再试(相同任务1秒内只能请求一次)" + bufferItem)
            else:
                print("走缓存返回结果")
                bufferItemStr = bufferItem.decode()
                return json.loads(bufferItemStr)
        else:
            print("不存在缓存,加入一个临时缓存(1秒),并直接运行")
            pipe = r.pipeline()
            pipe.set(inputMD5,
                     "DOING_MISSION!!wait_for_few_time!\n" + str(datetime.datetime.now()))
            pipe.expire(inputMD5, 1)
            pipe.execute()
            return False

    # 存储方法
    def insert(self, msg):
        self.db['auto_' + type(self).__name__].insert_one(msg)

    left_Moren = 10
    top_Moren = 300

    # 获取浏览器标签截图（返回本地地址）
    def get_image_screen(self, imgTag):  # 对验证码所在位置进行定位，然后截取验证码图片
        global left_Moren, top_Moren

        while True:
            loc = imgTag.location
            size = imgTag.size
            # if 'darwin' in sys.platform:
            #     print("如果是MAC系统,分辨率位置翻倍")
            #     loc['x'] = loc['x'] * 2
            #     loc['y'] = loc['y'] * 2
            #     size['width'] = size['width'] * 2
            #     size['height'] = size['height'] * 2
            # 图片和标签大小不一致的,不能通过size获取图片,截图会偏移
            for i in range(100):
                if loc['x'] == 0:
                    time.sleep(0.01)
                    continue
                else:
                    # left_Moren = loc['x']
                    # top_Moren = loc['y']
                    # print("已对验证码图片位置做死定位,从而降低定位不到时候的命中率")
                    break
            else:
                if left_Moren == 0:
                    raise Exception("定位错误,尚未死定位")
                else:
                    loc['x'] = left_Moren
                    loc['y'] = top_Moren
            left = loc['x']
            top = loc['y']
            right = left + size['width']
            bottom = top + size['height']
            print("截图定位坐标", left, top, right, bottom)
            page_snap_obj = self.get_snap()
            image_obj = page_snap_obj.crop((left, top, right, bottom))

            if not os.path.exists('./code'):
                os.makedirs('./code')
            filePath = './code/' + str(time.time()).replace('.', '_') + '.png'
            image_obj.insert(filePath)
            # 验证码识别
            return filePath  # 得到的就是验证码文件地址

    # 返回浏览器整个截图截图（返回OSS链接地址）
    def get_full_screen_oss(self):

        js = "var action=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        fileName = str(uuid.uuid1()) + 'full_snap.png'
        self.driver.save_screenshot(fileName)
        ossUrl = fileUpdate(fileName)
        os.remove(fileName)
        return ossUrl

    def get_snap(self):  # 对目标网页进行截屏.这里截的是全屏
        fileName = str(uuid.uuid1()) + 'full_snap.png'
        self.driver.save_screenshot(fileName)
        page_snap_obj = Image.open(fileName)
        os.remove(fileName)
        return page_snap_obj  # 发票验真平台

    # 如果在处理过程中覆写__state，那么在该实例工作过程中是可以查看该实例的状态的
    def getState(self):
        return self._state

    # 封装设置页面对象的属性值的方法
    # 调用JavaScript代码修改页面元素的属性值，arguments[0]－［2］分别会用后面的
    # element、attributeName和value参数值进行替换，并执行该JavaScript代码
    def setAttribute(self, elementObj, attributeName, value):
        self.driver.execute_script("arguments[0].setAttribute\
        (arguments[1],arguments[2])", elementObj, attributeName, value)

    # 启动webdriver的文件下载功能
    def enable_download_in_headless_chrome(self, download_dir):
        """
        there is currently a "feature" in chrome where
        headless does not allow file download: https://bugs.chromium.org/p/chromium/issues/detail?id=696481
        This method is a hacky work-around until the official chromedriver support for this.
        Requires chrome version 62.0.3196.0 or above.
        """

        # add missing support for chrome "send_command"  to selenium webdriver
        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        command_result = self.driver.execute("send_command", params)
        print("response from browser:")
        for key in command_result:
            print("result:" + key + ":" + str(command_result[key]))

    # overwrite
    def _deal(self, input):
        print("覆写该方法,完成任务和操作")
        self.driver.get("http://www.baidu.com")
        input.update({'msg': 'error', 'state': 0})
        return input

    def __filePath(self, basePath):
        # 往上查5个级别,看看是否有目标文件,没有最终抛出异常
        if os.path.exists("/root/scrapy-demo-beyebe/chromedriver"):
            return "/root/scrapy-demo-beyebe/" + basePath
        for i in range(5):
            if os.path.exists(basePath):
                return basePath
            else:
                basePath = "../" + basePath

        raise Exception("未找到对应的ChromeDriver驱动文件")

    def __getInputMD5(self, input):
        jsonStrInput = json.dumps(input, cls=CJsonEncoder, ensure_ascii=False)
        inputMD5 = hashlib.md5(jsonStrInput.encode(encoding='UTF-8')).hexdigest()
        return inputMD5
