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

import selenium
from PIL import Image
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver import ActionChains

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

"""
   fpdm = input['fpdm'] 发票代码 比较长
   fphm = input['fphm'] 发票号码
   kprq = input['kprq'] 开票日期
   kjje = input['kjje'] 开具金额
    # fpdm = "1100182130"
    # fphm = "15024752"
    # kprq = "20180614"
    # kjje = "18679.25"
"""

# 有远程遥控Driver和本地Driver两种模拟形式
# class fapiaoImpl(WebDriverImp):

tableName = "file_zhongdeng"


class zhongDengImpl(LoginDriverImp):
    # class zhongDengImpl(LoginDriverRomoteImp):

    def getDriverPort(self):
        return 5441

    def _login(self):
        if self.data is None:
            # 如果没传账号,就是比一比的测试账号
            user = "beyebe"
            password = "asdf1234"
        else:
            user = self.data['account']
            password = self.data['keyword']
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
                driver.get('https://www.zhongdengwang.org.cn/rs/main.jsp')

    def _deal(self, input):
        companyName = input['companyName']
        afterDate = input.get('afterDate', '19000101')
        try:
            afterDate = datetime.datetime.strptime(afterDate, "%Y%m%d")
        except:
            return {'state': 622, 'errMsg': 'ERROR您的日期格式输入错误,请从新输入'}

        driver = self.driver
        while True:
            # 按资金融入方名称查询
            """
            资金融入方
            """
            print("按金融融资方查询")
            try:
                driver.get(
                    "https://www.zhongdengwang.org.cn/rs/conditionquery/byname.do?method=init&timeset={}".format(str(
                        time.time())))
            except TimeoutException:
                print("driver超时异常,忽略并尝试提取内容")
            # 查询校验码识别
            self._state = "[中登网登记]正在查询的公司是:{},正在验证码查询阶段,进度1/4".format(input['companyName'])

            try:

                driver.find_element_by_id('name').clear()
                driver.find_element_by_id('name').send_keys(companyName)
                # 找到对应tr，从而定位验证码图片
                imgCode = None
                for item in driver.find_elements_by_css_selector('tr'):
                    if imgCode is not None:
                        break
                    if '校验码' in item.text:
                        # 继续定位img标签
                        imgTag = item.find_element_by_css_selector('img')
                        self.setAttribute(imgTag, "style", "")
                        self.setAttribute(imgTag, "width", 150)
                        self.setAttribute(imgTag, "height", 40)
                        while True:
                            try:
                                # 如果为空,换一张验证码。不为空则直接输入
                                imgCode = self.getCodeString(imgTag)
                                if imgCode is None:
                                    self.click100_by_tag(imgTag)
                                else:
                                    print("成功识别", imgCode)
                                    break
                            except:
                                traceback.print_exc()
                # 输入内容
                driver.find_element_by_id('validateCode').send_keys(imgCode)
                try:
                    driver.find_element_by_id('query').click()
                except:
                    print("点击超时,最多等待30秒查询")
                    self._state = "{},已点击查询按钮，正在等待中登网返回信息。最多等待30秒 2/4".format(input['companyName'])
                for i in range(300):
                    if '查看应收账款质押和转让登记' in driver.page_source:
                        print("【查看应收账款质押和转让登记】进入成功")
                        break
                    if '校验码错误' in driver.page_source:
                        print("校验码错误,重新尝试")
                        raise Exception("ERROR校验码错误")
                    time.sleep(0.1)
                else:
                    print("30秒内中登网没返回该公司信息")
                    return {'state': 700, 'errMsg': 'ERROR中登网30秒内查询不到该公司信息'}
            except UnexpectedAlertPresentException:
                # 弹窗BUG

                al = self.driver.switch_to_alert()
                msg = al.text
                returnObj = {'state': 580, 'errMsg': 'ERROR浏览器意外弹窗:' + msg}
                al.accept()
                if '同名用户已在别处登陆' in msg:
                    print("用户被强登，重新登陆抢回控制权")
                    self._login()
                    continue
                return returnObj

            except selenium.common.exceptions.NoSuchElementException:
                traceback.print_exc()
                print("【中登网】出现定位不到标签的错误，可能是登陆状态丢失，重新进行登陆,并保存截图")
                ossUrl = self.get_full_screen_oss()
                print("截图ossURL,并休息3秒", ossUrl)
                time.sleep(3)
                self._login()
                continue
            except:
                traceback.print_exc()
                if '校验码错误' in traceback.format_exc():
                    print("校验码错误,重试验证码,刷新")
                    driver.refresh()
                    continue
                return {'state': 599, "errMsg": "ERROR未知错误20054,请联系开发者修改", "err": traceback.format_exc()}
            # 查看应收账款质押和转让登记
            for item in driver.find_elements_by_css_selector('a'):
                if item.text == '查看应收账款质押和转让登记':
                    print("【点击】查看应收账款质押和转让登记")
                    item.click()
                    break
            # 查看是否有记录

            for tt in range(100):
                if '下载' in driver.page_source:
                    break
                if '本次查询共查询到登记0笔' in driver.page_source:
                    returnObj = {'state': 210, 'errMsg': 'ERROR错误,没有任何保理记录', 'regnoList': [], 'pdfs': []}
                    return returnObj
                time.sleep(0.1)
            # 记录所有regno
            lstRegno = []
            # 首先查看有几页,如果有n页,那么就要采集n次
            try:
                numTotal = int(driver.find_element_by_id("totalNum").text)
            except:
                numTotal = 1
            for page in range(numTotal):
                # 添加内容
                for i, item in enumerate(driver.find_elements_by_css_selector("tr[class=\'baibiao\']")):
                    if item.get_attribute("name") == 'noData' or 'pager' == item.get_attribute("name"):
                        continue
                    if item.get_attribute("style") is not None and 'display' in item.get_attribute("style"):
                        continue
                    itemNow = {}
                    itemNow['date_start'] = item.find_elements_by_css_selector('td')[2].text.strip()
                    dateNow = datetime.datetime.strptime(itemNow['date_start'], '%Y-%m-%d %H:%M:%S')
                    if dateNow < afterDate:
                        continue
                    itemNow['index'] = item.find_elements_by_css_selector('td')[0].text
                    itemNow['no'] = item.find_elements_by_css_selector('td')[1].text
                    itemNow['date_end'] = item.find_elements_by_css_selector('td')[3].text
                    itemNow['class'] = item.find_elements_by_css_selector('td')[4].text
                    itemNow['pledgee'] = item.find_elements_by_css_selector('td')[5].text
                    # "td[name=\"no\"]"
                    lstRegno.append(itemNow)
                # 点击下一页
                self.click100_by_tag(driver.find_element_by_css_selector("a[name=\"next\"]"))
                time.sleep(0.1)
            print("登记证明编号记录完成", lstRegno)
            print("正在依次下载")
            self._state = "[中登网登记]正在查询的公司是:{},登记证明编号记录完成,正在依次下载,总进度2/4,应下载文件共{}个".format(input['companyName'],
                                                                                         len(lstRegno))

            pdfs = []
            for i, regnoDict in enumerate(lstRegno):
                regno = regnoDict['no']
                # 大量下载极易造成卡死,要进行重试,最次最多重试5次
                self._state = "[中登网登记]正在查询的公司是:{},登记证明编号记录完成,正在依次下载,总进度3/4,应下载文件共{}个,正在下载第{}个".format(
                    input['companyName'],
                    len(lstRegno), i)
                try:
                    dbItem = self.db[tableName].find_one({'regno': regno})
                except:
                    print("WARNING MONGODB链接异常,缓存功能失效")
                    dbItem = None
                if dbItem is not None:
                    print(dbItem['regno'], "已经下载过了,走缓存")
                    # 已经下载过了,使用下载结果
                    dictNow = dbItem
                    dictNow['_id'] = str(dictNow['_id'])
                    dictNow.update(regnoDict)
                    pdfs.append(dictNow)
                    continue

                for h in range(5):
                    print(i, regno)
                    self.download_pdf(regno, companyName, pdfs)
                    break
                else:
                    print("5次重试失败,跳过该页")
                    traceback.print_exc()

            # 全部完成并且回复代码至首页
            try:
                driver.get("https://www.zhongdengwang.org.cn/rs/conditionquery/byname.do?method=init")
            except TimeoutException:
                print("driver超时异常,忽略并尝试提取内容")
            returnObj = {'state': 200, 'errMsg': 'success!', 'regnoList': lstRegno, 'pdfs': pdfs}
            return returnObj

    def download_pdf(self, regno, companyName, pdfs):
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
                        dictNow['pdfName'] = name
                        dictNow['companyName'] = companyName
                        dictNow['ossPath'] = ossPath
                        dictNow['insertTime'] = datetime.datetime.now()
                        self.db[tableName].insert(dictNow)
                        dictNow['_id'] = str(dictNow['_id'])
                        pdfs.append(dictNow)
                        return dictNow
                    else:
                        print("文件还在浏览器下载中,请稍后！")
                        time.sleep(0.8)  # 100次0.1秒，共10秒
                if dictNow == {}:
                    print("10秒都没有下载成功,下载异常")
                    dictNow['regno'] = regno
                    dictNow['pdfName'] = name
                    dictNow['companyName'] = companyName
                    dictNow['ossPath'] = None
                    dictNow['insertTime'] = datetime.datetime.now()
                    dictNow['errMsg'] = "ERROR 下载10秒都没有下载完,可能是中登网下载链接失效无法下载"
                    pdfs.append(dictNow)
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

        url = "http://39.108.188.34:9022/middleware/zd_identifyingEnglish/upload.go?filename=zhongdeng"
        urlList = [url]
        pdfs = []
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
                                pdfs.append(code)
                            else:
                                print("算法返回", dict_res)
                                print("算法要求更换验证码")
                                break
                        except:
                            print("验证码接口未返回JSON格式,直接使用返回值")
                            pdfs.append(code)
                            continue


                    finally:
                        os.remove(filePath)
                        print("删除验证码")
                except:
                    print("WARNING验证码接口请求异常", url)
                    # traceback.print_exc()
            if len(pdfs) > 0:
                print("至少有一个有正确结果,随机取一个返回")
                ans = random.sample(pdfs, 1)[0]
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
        time.sleep(0.1)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(tag, 10, 10)
        action_chains.click()
        action_chains.perform()
        print("完成按键操作")


if __name__ == '__main__':
    pool = WebDriverPool(dBean=zhongDengImpl, num=1, headless=False)
    impl = WebDriverPool.getOneDriver(pool)
    dictNow = impl.deal({'companyName': "上海中建航建筑工业发展有限", "afterDate": "20170501"})
    print(json.dumps(dictNow, cls=CJsonEncoder, ensure_ascii=False))
    # impl.deal({'companyName': "深圳银泰保理有限公司"})
