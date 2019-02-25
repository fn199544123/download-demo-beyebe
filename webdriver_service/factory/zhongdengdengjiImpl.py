# 发票验真平台
import base64
import datetime
import json
import os
import random

import time
import traceback
import uuid

import requests
import sys
from PIL import Image
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from logging_utils.cJsonEncoder import CJsonEncoder
from logging_utils.log import mylog
from oss_aliyun.updateFileBeyebe import fileUpdate
from webdriver_service.driverBean import WebDriverImp
from webdriver_service.driverRemoteBean import WebDriverRemoteImp
from webdriver_service.driver_pool.driverPool import WebDriverPool
from webdriver_service.loginDriverImp import LoginDriverImp
from webdriver_service.loginDriverRomoteImp import LoginDriverRomoteImp

left_Moren = 0
top_Moren = 0

# 有远程遥控Driver和本地Driver两种模拟形式
# class fapiaoImpl(WebDriverImp):

tableName = "file_zhongdeng"


class zhongDengDengJiImpl(LoginDriverImp):
    # class zhongDengImpl(LoginDriverRomoteImp):

    def getDriverPort(self):
        return 5441

    def __init__(self, MyPool, driver=None, headless=False):
        super().__init__(MyPool, driver, headless)

    def _login(self):
        user = "ytbl0010"
        password = "ytbl0010aDmin"

        driver = self.driver
        """
        登录模块
        """
        first = False
        while True:
            try:
                try:
                    driver.get('https://www.zhongdengwang.org.cn/rs/main.jsp')
                except TimeoutException:
                    print("driver超时异常,忽略并尝试提取内容")
                print("正在输入账号密码")
                driver.find_element_by_id('userCode').clear()
                driver.find_element_by_id('userCode').send_keys(user)
                if first:
                    time.sleep(1)
                    first = False
                else:
                    time.sleep(0.05)
                driver.find_element_by_id('showpassword').click()
                lstInput = driver.find_elements_by_css_selector("input")
                for item in lstInput:
                    if 'password' == item.get_attribute('id'):
                        item.click()
                        item.send_keys(password)
                        break

                imgTag = driver.find_element_by_id('imgId')
                while True:
                    # 如果为空,换一张验证码。不为空则直接输入
                    self.setAttribute(imgTag, "width", 150)
                    self.setAttribute(imgTag, "height", 40)
                    imgCode1 = self.getCodeString(imgTag)
                    if imgCode1 is None:
                        driver.find_element_by_id('imgId').click()
                    else:
                        print("成功识别", imgCode1)
                        inputa = imgCode1
                        break
                driver.find_element_by_id('validateCode').send_keys(inputa)
                time.sleep(0.5)
                print("【验证】已经完成账号密码输入")
                try:
                    driver.find_element_by_id('login_btn').click()  # 点击搜索按钮
                except TimeoutException:
                    pass
                print("正在进行登录")
                if '校验码错误' in driver.page_source:
                    print("验证码输入错误,重试流程")
                    continue
                if '按主体查询' in driver.page_source:
                    print("【验证】页面已出现", "按主体查询", "登陆流程结束")
                    break
            except:
                traceback.print_exc()
                print("本次登录失败,正在尝试重试!")
                driver.refresh()

    def _deal(self, input):
        djqx = 2
        tbrgdh = "测试填表人归档号"
        crrmc = '我是一家测试的企业'
        zzjgdm = "abcdefg"
        gszch = "abcdefg"
        fddbr = "帅比"
        shhy = 3
        qygm = 1
        zsList = [2, 2, 2]
        zsText = "美丽的地球村"

        driver = self.driver
        # 按资金融入方名称查询
        """
        资金融入方
        """
        print("初始登记")
        try:
            driver.get("https://www.zhongdengwang.org.cn/rs/bigTypechoose.do?timeset={}".format(str(
                time.time())))
        except TimeoutException:
            print("driver超时异常,忽略并尝试提取内容")
        # 查询校验码识别
        self._state = "[中登网登记]正在进行登记,正在填写基本信息阶段,进度1/4"
        while True:
            try:
                time.sleep(1)
                driver.find_element_by_css_selector("#A00200").click()
                time.sleep(1)
                driver.find_element_by_css_selector(
                    "body > div.main-table.hui > table:nth-child(4) > tbody > tr:nth-child(1) > td > input[type=\"radio\"]:nth-child(1)").click()
                driver.find_element_by_css_selector("#next").click()
                time.sleep(1)
                Select(driver.find_element_by_css_selector('#timelimit')).select_by_index(djqx)
                driver.find_element_by_css_selector('#title').send_keys(tbrgdh)
                time.sleep(1)
                driver.find_element_by_css_selector(
                    "body > div.main-table.hui > form > div > input:nth-child(1)").click()
                time.sleep(1)
                # 增加出让人 #addDebtor
                driver.find_element_by_css_selector("#addDebtor").click()
                time.sleep(1)
                # 出让人类型企业 #debtorType
                Select(driver.find_element_by_css_selector('#debtorType')).select_by_index(3)
                time.sleep(2)
                # 等待渲染内容
                # 出让人名称 #debtorName
                driver.find_element_by_css_selector('#debtorName').send_keys(crrmc)
                # 组织机构代码 #orgCode
                driver.find_element_by_css_selector('#orgCode').send_keys(zzjgdm)
                # 工商注册号 #businessCode
                driver.find_element_by_css_selector('##businessCode').send_keys(zzjgdm)
                # 全球法人机构识别代码 #lei
                driver.find_element_by_css_selector('#lei').send_keys(zzjgdm)
                # 法定代表人 #responsiblePerson
                driver.find_element_by_css_selector('#responsiblePerson').send_keys(zzjgdm)
                # 所属行业 #industryCode
                driver.find_element_by_css_selector('#industryCode').send_keys(zzjgdm)
                # 企业规模 #scale
                driver.find_element_by_css_selector('#scale').send_keys(zzjgdm)
                # 住所选项 #country #province #city
                driver.find_element_by_css_selector('#orgCode').send_keys(zzjgdm)
                # 住所内容 #address
                driver.find_element_by_css_selector('#address').send_keys(zzjgdm)




            except:
                traceback.print_exc()
                print("操作出现意外错误错误")

    def download_pdf(self, regno, companyName, ansList):
        url = "https://www.zhongdengwang.org.cn/rs/conditionquery/byid.do?method=viewfile&regno={}&type=1"
        dictNow = {}
        driver = self.driver
        try:
            try:
                driver.get(url.format(regno))
            except TimeoutException:
                print("driver超时异常,忽略并尝试提取内容")
            for tt in range(100):
                if '下载' in driver.page_source:
                    break
                time.sleep(0.1)

            for item in driver.find_elements_by_css_selector("a"):

                # 这里只下载第一个,所以第一个就Break
                name = item.text
                print("获取文件名", name)
                filePath = "./webDriver_download/" + name
                print(name, "尚未缓存,走下载上传路线")
                # 下载
                # item.click()
                # href="javascript:download('02973013000359528048');"
                """
                使用docker下载文件怎么都不好使，妈蛋！！！
                """
                driver.execute_script("download('{}');".format(name.replace('.pdf', '')))
                for i in range(10):
                    if os.path.exists(filePath):
                        time.sleep(0.2)
                        ossPath = fileUpdate(filePath)
                        # 上传成功后删除oss对象
                        os.remove(filePath)
                        dictNow['regno'] = regno
                        dictNow['name'] = name
                        dictNow['companyName'] = companyName
                        dictNow['ossPath'] = ossPath
                        dictNow['insertTime'] = datetime.datetime.now()
                        self.db[tableName].save(dictNow)
                        dictNow['_id'] = str(dictNow['_id'])
                        ansList.append(dictNow)
                        return
                    else:
                        print("文件还在浏览器下载中,请稍后！")
                        time.sleep(0.8)  # 100次0.1秒，共10秒
                if dictNow == {}:
                    print("10秒都没有下载成功,下载异常")
                    dictNow['regno'] = regno
                    dictNow['name'] = name
                    dictNow['companyName'] = companyName
                    dictNow['ossPath'] = None
                    dictNow['insertTime'] = datetime.datetime.now()
                    dictNow['errMsg'] = "ERROR 下载10秒都没有下载完,可能是中登网下载链接失效无法下载"
                    ansList.append(dictNow)
                    # 只采集第一个,其他的不采集,于是break
                    return
                return
        except:
            traceback.print_exc()
            time.sleep(1)

    # def duplicate(self, input):

    #     """
    #             去重逻辑,发票代码显示在发标的左上方，发票号码在发票的右上方。
    #     发票代码一般来说一次购票基本一样，很难得会出现不一致的情况，发票号码在本发票代码编号下为唯一。
    #     发票代码可以理解为目录，发票号码为目录下的明细。
    #
    #     :param input:
    #     :return:
    #     """
    #     dictDup = {'fpdm': input['fpdm'], 'fphm': input['fphm']}
    #     item = self.db['auto_' + type(self).__name__].find_one(dictDup)
    #     if item is not None:
    #         return dict(item)
    #     else:
    #         return False

    """
    获取验证码结果
    """

    def getCodeString(self, imgTag):
        # 多地址容错
        url_l = "http://localhost:9022/middleware/zd_identifyingEnglish/upload.go?filename=zhongdeng"
        url = "http://39.108.188.34:9022/middleware/zd_identifyingEnglish/upload.go?filename=zhongdeng"
        urlList = [url, url_l]
        ansList = []

        while True:
            # 尝试到成功为止
            for url in urlList:
                try:  # 异常处理
                    filePath = self.get_image_screen(imgTag)
                    try:
                        file = {'file': open(filePath, 'rb')}
                        print("发起对【王博】验证码接口的请求")
                        response = requests.post(url, files=file)
                        code = response.text
                        print("发起对【王博】验证码接口返回", response.text)
                        if len(code) != 4 or code == '' or code is None:
                            print("该验证码识别失败风险较大，更换验证码", code)
                            code = None
                        try:
                            dict_res = json.loads(code)
                            if dict_res.get('state') == 200:
                                code = dict_res['data']
                                ansList.append(code)
                            else:
                                print("算法返回", dict_res)
                                print("算法要求更换验证码")
                                break
                        except:
                            print("验证码接口未返回JSON格式,直接使用返回值")
                            ansList.append(code)
                            continue


                    finally:
                        os.remove(filePath)
                        print("删除验证码")
                except NoSuchElementException:
                    traceback.print_exc()
                    print("出现定位不到标签的错误，可能是登陆状态丢失，重新进行登陆,并保存截图")
                    self.driver.refresh()
                    time.sleep(1)
                    self.driver._login()
                except:
                    print("验证码接口请求异常", url)
                    traceback.print_exc()
            if len(ansList) > 0:
                print("至少有一个有正确结果,随机取一个返回")
                ans = random.sample(ansList, 1)[0]
                print("返回", ans)
                return ans
            # 更换图片再来一次
            self.click100_by_tag(self.driver.find_element_by_id('img'))

    def setAttribute(self, elementObj, attributeName, value):
        # 封装设置页面对象的属性值的方法
        # 调用JavaScript代码修改页面元素的属性值，arguments[0]－［2］分别会用后面的
        # element、attributeName和value参数值进行替换，并执行该JavaScript代码
        self.driver.execute_script("arguments[0].setAttribute\
         (arguments[1],arguments[2])", elementObj, attributeName, value)

    def click100_by_tag(self, tag):
        # 保证可以点击到的方法
        time.sleep(1)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(tag, 10, 10)
        action_chains.click()
        action_chains.perform()
        print("完成按键操作")


if __name__ == '__main__':
    pool = WebDriverPool(dBean=zhongDengDengJiImpl, num=1, headless=False)
    impl = WebDriverPool.getOneDriver(pool)
    dictNow = impl.deal({'time': str(time.time())})
    print(json.dumps(dictNow, cls=CJsonEncoder, ensure_ascii=False))
    # impl.deal({'companyName': "深圳银泰保理有限公司"})
