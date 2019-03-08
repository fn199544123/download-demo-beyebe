# 发票验真平台
import base64
import datetime
import json
import os
import random
import re

import time
import traceback
import uuid
from urllib import request

import requests
import sys

import selenium
from PIL import Image
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException, \
    ElementNotVisibleException
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

tableName = "file_zhongdengdengji"


class zhongDengDengJiImpl(LoginDriverImp):
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
                except Exception:
                    print("driver请求异常,忽略并尝试提取内容")
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
                self.restartDriver()

    def _deal(self, input):

        # 下面的可能有多个【出让人信息】
        # 按资金融入方名称查询
        """
        资金融入方
        """

        keyMustExist = [
            "timelimit",
            "title",
            "addDebtorList",
            "maincontractno",
            "maincontractcurrency",
            "maincontractsum",
            "description",
        ]
        key = 'empty'
        for key in keyMustExist:
            if key not in input:
                return {'state': 619,
                        'errMsg': "缺少必备参数{},其中timelimit、title、addDebtorList、maincontractno、maincontractcurrency、maincontractsum、description为必须存在的参数"}
        while True:
            try:
                driver = self.driver
                print("初始登记")
                try:
                    driver.get("https://www.zhongdengwang.org.cn/rs/bigTypechoose.do?timeset={}".format(str(
                        time.time())))
                except TimeoutException:
                    print("driver超时异常,忽略并尝试提取内容")
                # 查询校验码识别
                self._state = "[中登网登记]正在进行登记,正在填写基本信息阶段,进度1/4"
                time.sleep(0.5)
                driver.find_element_by_css_selector("#A00200").click()
                time.sleep(0.5)
                driver.find_element_by_css_selector(
                    "body > div.main-table.hui > table:nth-child(4) > tbody > tr:nth-child(1) > td > input[type=\"radio\"]:nth-child(1)").click()
                driver.find_element_by_css_selector("#next").click()
                time.sleep(0.5)
                # 输入基本信息
                self.__findSelectByText(driver.find_element_by_css_selector('#timelimit'), input['timelimit'])
                driver.find_element_by_css_selector('#title').send_keys(input['title'])
                time.sleep(0.5)
                driver.find_element_by_css_selector(
                    "body > div.main-table.hui > form > div > input:nth-child(1)").click()
                time.sleep(0.5)
                # 增加出让人 #addDebtor
                for item in input['addDebtorList']:
                    # 点击增加出让人
                    driver.find_element_by_css_selector("#addDebtor").click()
                    time.sleep(1)
                    # driver.refresh()

                    for key in item:
                        try:
                            # 遍历所有的类型
                            tagNow = driver.find_element_by_id(key)
                            tagName = tagNow.tag_name
                            if 'input' in tagName:
                                tagNow.send_keys(item[key])
                            elif 'select' in tagName:
                                self.__findSelectByText(tagNow, item[key])
                            # 出让人类型企业 #debtorType
                            time.sleep(0.35)
                        except:
                            return {'state': 623,
                                    'errMsg': "登记时标签定位输入出现问题,id=" + key,
                                    "err": traceback.format_exc()}
                    time.sleep(0.5)  # 等待渲染内容
                    driver.find_element_by_css_selector("#saveButton").click()
                    time.sleep(0.5)  # 等待渲染内容
                # 受让人信息
                driver.find_element_by_css_selector("#secondName").click()
                time.sleep(0.5)  # 等待渲染内容
                driver.find_element_by_css_selector("#addDebtorAuto").click()
                time.sleep(0.5)  # 等待渲染内容
                # 转让财产信息
                """
                这个地方极容易被卡住，需要特别循环强调,如果卡住点小图标即可恢复
                """
                for i in range(10):
                    driver.find_element_by_css_selector("#typeName").click()
                    time.sleep(0.1)
                    driver.find_element_by_css_selector("#typeName > img").click()
                    time.sleep(0.1)
                    if '请根据被转让的应收账款的特点进行描述' in driver.page_source:
                        break
                else:
                    return {'state': 619,
                            'errMsg': "点击*转让财产信息*按钮卡住了，重试10次失败，请重试"}
                time.sleep(0.3)  # 等待渲染内容

                # 点击这里上传转让附件
                if 'ossPathList' in input:
                    for fileNew in input['ossPathList']:
                        fileName = fileNew.get('filename')
                        ossPath = fileNew['path']
                        if not os.path.exists('./file'):
                            os.makedirs('./file')
                        fileName = "./file/" + ossPath.split('/')[-1][-30:]
                        request.urlretrieve(ossPath, fileName)
                        # 拼接绝对路径
                        localPath = os.path.abspath(fileName)
                        try:
                            driver.find_element_by_id("attachinfo").click()
                            time.sleep(1)
                            driver.find_element_by_id("file").send_keys(localPath)
                            time.sleep(0.5)
                            driver.find_element_by_css_selector(
                                "#describeUpload > table > tbody > tr:nth-child(3) > td > input[type=\"button\"]:nth-child(1)").click()
                            al = self.driver.switch_to_alert()
                            msg = al.text
                            if '附件上传成功' in msg:
                                al.accept()
                                continue
                            else:
                                al.accept()
                                return {'state': 580,
                                        'errMsg': "上传附件失败请重试,中登网提示信息:" + msg}
                        finally:
                            os.remove(localPath)
                # 转让财产价值
                driver.find_element_by_css_selector('#maincontractno').send_keys(input['maincontractno'])
                time.sleep(0.5)  # 等待渲染内容
                self.__findSelectByText(driver.find_element_by_css_selector('#maincontractcurrency'),
                                        input['maincontractcurrency'])
                time.sleep(0.5)  # 等待渲染内容
                driver.find_element_by_css_selector('#maincontractsum').send_keys(input['maincontractsum'])
                driver.find_element_by_css_selector('#description').send_keys(input['description'])
                # 保存
                driver.find_element_by_css_selector(
                    "body > div.main-table.hui > table > tbody > tr > td > table:nth-child(3) > tbody > tr > td > input").click()
                time.sleep(0.5)
                # 预览截图并返回
                driver.find_element_by_id("previewbutton").click()
                ossUrl = self.get_full_screen_oss()
                print("预览图已截取", ossUrl)

                returnObj = {'state': 200, 'ossUrl': ossUrl, 'errMsg': '成功'}
                input.update(returnObj)

                if input.get("isUpload", 0) == 1:
                    try:
                        time.sleep(2)
                        print("[WARNING]注意！！这是一个登记操作")
                        self.driver.find_element_by_id("initsubmitbutton").click()
                        print("已点击登记按钮")
                        for i in range(100):
                            if '此次登记费用' in driver.page_source:
                                break
                            time.sleep(0.1)
                        else:
                            raise Exception("ERROR，未出现字段此次登记费用")
                        # initSubmitButton 确定
                        self.driver.find_element_by_id("initSubmitButton").click()
                        for i in range(100):
                            if '登记成功' in driver.page_source and 'images/success' in driver.page_source:
                                break
                            time.sleep(0.1)
                        else:
                            raise Exception("ERROR，未出现字段(登记成功)")
                        print("已成功登记,进行截图")
                        ossUrlDengJi = self.get_full_screen_oss()
                        returnObj['ossUrlDengJi'] = ossUrlDengJi
                        print("正在获取成功附件")
                        # 获取type和id,组装URL
                        # href="javascript:filedownload('00','05617033000668301597')
                        matchObj = re.search(r'href=\"javascript:filedownload\(\'(.*)\',\'(.*?)\'\)',
                                             driver.page_source, re.M | re.I)
                        if matchObj:
                            textStr = matchObj.group(0)
                            type = matchObj.group(1)
                            fileId = matchObj.group(2)
                            print("查询->type", type, "fileId", fileId, "正文", textStr)
                        else:
                            raise Exception("没有正则匹配到文件字符串")
                        returnObj['fileNew'] = self.download_pdf(fileId)
                        returnObj['state'] = 200
                        returnObj['errMsg'] = "成功完成登记"
                        return returnObj
                    except:
                        print("ERROR登记流程出错")
                        returnError = {'state': 1099, 'ossUrl': ossUrl, 'errMsg': '未知登记错误异常,请排查登记错误'}
                        returnObj.update(returnError)
                        return returnObj
                return input

            except UnexpectedAlertPresentException:
                # 弹窗BUG
                al = self.driver.switch_to_alert()
                msg = al.text
                returnObj = {'state': 580, 'errMsg': 'ERROR浏览器意外弹窗:' + msg}
                al.accept()
                if '同名用户已在' in msg:
                    print("用户被强登，重新登陆抢回控制权")
                    self._login()
                    continue

                return returnObj

            except ElementNotVisibleException:
                print("可能输入了非法字符或者不存在的key,请检查后再试")
                return {'state': 521, 'errMsg': '可能输入了非法字符或者不符合中登网要求的字段,请检查后再试', 'err': traceback.format_exc()}

            except NoSuchElementException:
                print("可能输入了不符合中登网要求的字段,无法进行提交操作。")
                return {'state': 619, 'errMsg': '可能输入了不符合中登网要求的字段,或者必填字段未填写,无法进行提交操作,请检查后再试',
                        'err': traceback.format_exc()}

            except selenium.common.exceptions.ElementNotVisibleException:
                print("操作错误，字段不存在")
                return {'state': 521, 'errMsg': '不存在该标签:{},请查询字段表重新输入'.format(key), 'err': traceback.format_exc()}
            except:
                traceback.print_exc()
                print("操作出现意外错误，重新登陆并重试")
                self.restartDriver()
                self._login()
                return {'state': 599, 'errMsg': 'ERROR未知错误75896', 'err': traceback.format_exc()}

    def __findSelectByText(self, selectTag, textStr):
        if textStr == None or textStr == "":
            raise Exception("ERROR下拉框的输入不能为空:" + textStr)

        print("正在填写选择栏,textStr={}".format(textStr))
        for i, option in enumerate(selectTag.find_elements_by_css_selector("option")):
            if option.text == textStr:
                Select(selectTag).select_by_index(i)
                return

        raise Exception("ERROR您的输入有问题,这个输入没有在下拉栏里找到:" + textStr)

    def download_pdf(self, fileId):
        urlBase = "https://www.zhongdengwang.org.cn/rs/download.do?method=getDownload&type={}&id={}"
        # fileId = '05617033000668301597'
        dictNow = {}
        driver = self.driver
        try:
            try:
                driver.get(urlBase.format('00', fileId))
            except TimeoutException:
                print("driver超时异常,忽略并尝试提取内容")
            for tt in range(300):
                if '初始登记' in driver.page_source:
                    break
                time.sleep(0.1)

            for item in driver.find_elements_by_css_selector("span"):

                # 这里只下载第一个,所以第一个就Break
                name = item.text
                print("获取文件名", name)
                filePath = "./webDriver_download/" + name
                print(name, "开始下载")
                # 下载
                driver.get(urlBase.format('01', fileId))
                for i in range(10):
                    if os.path.exists(filePath):
                        time.sleep(0.2)
                        ossPath = fileUpdate(filePath)
                        # 上传成功后删除oss对象
                        os.remove(filePath)
                        dictNow['fileId'] = fileId
                        dictNow['name'] = name
                        dictNow['ossPath'] = ossPath
                        dictNow['insertTime'] = datetime.datetime.now()
                        try:
                            self.db[tableName].save(dictNow)
                        except:
                            print("WARNING数据库链接异常,将会导致缓存失败")
                            traceback.print_exc()
                        dictNow['_id'] = str(dictNow['_id'])
                        return dictNow
                    else:
                        print("文件还在浏览器下载中,请稍后！")
                        time.sleep(0.6)  # 100次0.1秒，共10秒
                if dictNow == {}:
                    print("10秒都没有下载成功,下载异常")
                    dictNow['fileId'] = fileId
                    dictNow['name'] = name
                    dictNow['ossPath'] = None
                    dictNow['insertTime'] = datetime.datetime.now()
                    dictNow['errMsg'] = "ERROR 下载10秒都没有下载完,可能是中登网下载链接失效无法下载"
                    # 只采集第一个,其他的不采集,于是return
                    return dictNow
                return dictNow
        except:
            traceback.print_exc()
            return None

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

    # 登记不缓存
    def duplicate(self, input):
        return False

    def getCodeString(self, imgTag):
        # 多地址容错
        # url_l = "http://localhost:9022/middleware/zd_identifyingEnglish/upload.go?filename=zhongdeng"
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
                except NoSuchElementException:
                    traceback.print_exc()
                    print("【中登网登记】出现定位不到标签的错误，可能是登陆状态丢失，重新进行登陆,并保存截图")
                    ossUrl = self.get_full_screen_oss()
                    print("截图ossURL,并休息3秒", ossUrl)
                    self.driver.refresh()
                    time.sleep(3)
                    self.driver._login()
                except:
                    print("验证码接口请求异常", url)
                    traceback.print_exc()
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
        time.sleep(1)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(tag, 10, 10)
        action_chains.click()
        action_chains.perform()
        print("完成按键操作")


if __name__ == '__main__':
    input = {
        "timelimit": "1年",
        "title": "测试归档号",
        "maincontractno": "转让合同编码",
        "maincontractcurrency": "人民币",
        "maincontractsum": "10000",
        "description": "我是可爱的小描述",
        "addDebtorList": [
            {
                # 金融机构
                "debtorType": "金融机构",
                "debtorName": "出让人名称",
                "financeCode": "abc123abc123abc123",
                "businessCode": "abc",
                "lei": "123",
                "responsiblePerson": "江泽民",
                "country": "中国",
                "province": "黑龙江省",
                "city": "哈尔滨市",
                "address": "美丽的松花江",
            }, {
                # 企业
                "debtorType": "企业",
                "debtorName": "可爱的比一比",
                "orgCode": "abcd",
                "businessCode": "1234",
                "lei": "777",
                "responsiblePerson": "毛泽东",
                "industryCode": "农、林、牧、渔业",
                "scale": "大型企业",
                "country": "中国",
                "province": "广东省",
                "city": "深圳市",
                "address": "可爱的南山区",
            }, {
                # 机关事业单位
                "debtorType": "机关事业单位",
                "debtorName": "可爱的比一比",
                "orgCode": "abcd",
                "legalCertificateNo": "1234",
                "lei": "777",
                "responsiblePerson": "毛泽东",
                "country": "中国",
                "province": "广东省",
                "city": "深圳市",
                "address": "可爱的南山区",
            }, {
                # 个体工商户
                "debtorType": "个体工商户",
                "tradeName": "字号名称",
                "idType": "身份证",
                "idCode": "230104199504041215",
                "country": "中国",
                "province": "广东省",
                "city": "深圳市",
                "address": "可爱的南山区",
            }, {
                # 个人
                "debtorType": "个人",
                "idType": "身份证",
                "idCode": "230104199504041215",
                "country": "中国",
                "province": "广东省",
                "city": "深圳市",
                "address": "可爱的南山区",
            }, {
                # 其他
                "debtorType": "其他",
                "debtorName": "出让人名称",
                "orgCodeNoVerify": "abc123abc123abc123",
                "registrationCertificateNo": "abc",
                "lei": "123",
                "responsiblePerson": "江泽民",
                "country": "中国",
                "province": "黑龙江省",
                "city": "哈尔滨市",
                "address": "美丽的松花江",
            }
        ]
    }
    print(json.dumps(input, ensure_ascii=False))
    pool = WebDriverPool(dBean=zhongDengDengJiImpl, num=1, headless=False)
    impl = WebDriverPool.getOneDriver(pool)
    dictNow = impl.deal(input)
    print(json.dumps(dictNow, cls=CJsonEncoder, ensure_ascii=False))
    # impl.deal({'companyName': "深圳银泰保理有限公司"})
