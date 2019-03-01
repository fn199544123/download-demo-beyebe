# 发票验真平台
import base64
import json
import os
import random

import time
import traceback
import uuid

import requests
import sys
from PIL import Image
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains

from logging_utils.log import mylog
from oss_aliyun.updateFileBeyebe import fileUpdate
from webdriver_service.driverBean import WebDriverImp
from webdriver_service.driverRemoteBean import WebDriverRemoteImp
from webdriver_service.driver_pool.driverPool import WebDriverPool
from webdriver_service.loginDriverImp import LoginDriverImp

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
class fapiaoImpl(WebDriverImp):

    # class fapiaoImpl(WebDriverRemoteImp):
    def _parseInvoice(self, html):
        if '查无此票' in html:
            return {'errMsg': '国家税务局返回查无此票'}
        if '不一致' in html:
            return {'errMsg': '国家税务局返回不一致'}
        data = {'goods': [], 'errMsg': 'success!'}
        soup = BeautifulSoup(html, 'lxml')
        idH1 = soup.select_one('h1')['id']
        idkey = idH1.split('_')[1]
        data['invoiceType'] = soup.select_one("h1[id=\"fpcc_{}\"]".format(idkey)).text  # 发票类型
        data['invoiceDate'] = soup.select_one("#kprq_{}".format(idkey)).text  # 开票日期
        data['invoiceNo'] = soup.select_one("#fphm_{}".format(idkey)).text  # 发票号
        data['invoiceNumber'] = soup.select_one("#fpdm_{}".format(idkey)).text  # 发票代码
        data['cheakNumber'] = soup.select_one("#jym_{}".format(idkey)).text  # 校验码
        try:
            data['machineNumber'] = soup.select_one("#sbbh_{}".format(idkey)).text  # 机器编号
        except:
            data['machineNumber'] = soup.select_one("#jqbh_{}".format(idkey)).text  # 机器编号

        data['buyer'] = soup.select_one("#gfmc_{}".format(idkey)).text  # 购买方 add
        data['borderNo'] = soup.select_one("#gfsbh_{}".format(idkey)).text  # 纳税人识别号add
        for i, tr in enumerate(soup.select_one("table[class=\"fppy_table_box\"]").select('tr')):
            # 第一行是标题，倒数第二行是合计，倒数第一行是价税合计
            if i == 0:
                continue
            item = {}
            key = tr.select_one("td").text
            if key == '合计':
                data['totalPrice'] = soup.select_one("#je_{}".format(idkey)).text  # 合计
                continue
            elif key == '价税合计（大写）':
                data['totalTaxAndPrice'] = soup.select_one("#jshjxx_{}".format(idkey)).text  # 价税合计
                data['totalTaxAndPriceChinese'] = soup.select_one("#jshjdx_{}".format(idkey)).text  # 价税合计(大写)
                continue
            else:
                for i, span in enumerate(tr.select('span')):
                    if i == 0:
                        item['goodsName'] = key  # 货物或应税劳务、服务名称
                    if i == 1:
                        item['goodsType'] = span.text  # 规格型号
                    if i == 2:
                        item['unit'] = span.text  # 单位
                    if i == 3:
                        item['num'] = span.text  # 数量
                    if i == 4:
                        item['unitPrice'] = span.text  # 单价
                    if i == 5:
                        item['billPrice'] = span.text  # 金额
                    if i == 6:
                        item['taxRate'] = span.text  # 税率(%)
                    if i == 7:
                        item['taxPrice'] = span.text  # 税额
                data['goods'].append(item)
        return data

    def getDriverPort(self):
        return 5440

    def _deal(self, input):
        keyMustExist = [
            "fpdm",
            "fphm",
            "kprq",
            "kjje"
        ]
        for key in keyMustExist:
            if key not in input:
                return {'state': 619,
                        'errMsg': "缺少必备参数{},fpdm、fphm、kprq、kjje、（校验码如果有必须填jym）为必须存在的参数"}

        driver = self.driver
        while True:
            try:
                dictNow = input
                try:
                    driver.get('https://inv-veri.chinatax.gov.cn/index.html')
                except TimeoutException:
                    print("driver超时异常,忽略并尝试提取内容")
                print("正在输入发票信息")
                # 1
                fpdm = input['fpdm']
                fphm = input['fphm']
                kprq = input['kprq']
                if input.get('jym') is not None and len(input.get('jym')) >= 6:
                    kjje = input['jym'][-6:]
                else:
                    kjje = input['kjje']
                for i in range(100):
                    if 'fpdm' in driver.page_source:
                        break
                    time.sleep(0.1)
                # 发票代码
                driver.find_element_by_id('fpdm').clear()
                driver.find_element_by_id('fpdm').send_keys(fpdm)
                # 发票号码

                driver.find_element_by_id('fphm').clear()
                driver.find_element_by_id('fphm').send_keys(fphm)
                # 开票日期
                driver.find_element_by_id('kprq').clear()
                driver.find_element_by_id('kprq').send_keys(kprq)
                # 开具金额
                driver.find_element_by_id('kjje').clear()
                driver.find_element_by_id('kjje').send_keys(kjje)
                # 首先调整验证码大小
                # imgTag = driver.find_element_by_id('yzm_img')
                # self.setAttribute(imgTag, "width", 90)
                # self.setAttribute(imgTag, "height", 35)
                # imgTag2 = driver.find_element_by_id('yzm_unuse_img')
                # self.setAttribute(imgTag2, "width", 90)
                # self.setAttribute(imgTag2, "height", 35)

                # 看输入是否有错误

                for i in range(100):
                    if "发票代码有误!" in driver.page_source:
                        print("发票代码有误")
                        dictNow = {'errMsg': "ERROR发票代码有误！无法返回信息，请输入正确的数据或格式", 'state': 601}
                        return dictNow
                    if "发票号码有误!" in driver.page_source:
                        print("发票号码有误")
                        dictNow = {'errMsg': "ERROR发票号码有误！无法返回信息，请输入正确的数据或格式", 'state': 602}
                        return dictNow
                    if "开票日期有误!" in driver.page_source:
                        print("开票日期有误")
                        dictNow = {'errMsg': "ERROR开票日期有误！无法返回信息，请输入正确的数据或格式", 'state': 603}
                        return dictNow
                    if "开票金额有误!" in driver.page_source:
                        print("开票金额有误")
                        dictNow = {'errMsg': "ERROR开票金额有误！无法返回信息，请输入正确的数据或格式", 'state': 604}
                        return dictNow
                    if "校验码有误!" in driver.page_source:
                        print("校验码有误!")
                        dictNow = {'errMsg': "ERROR校验码有误!无法返回信息，请输入正确的数据或格式", 'state': 605}
                        return dictNow
                    if "请输入发票号码" in driver.page_source:
                        print("请输入发票号码")
                        dictNow = {'errMsg': "ERROR请输入发票号码！", 'state': 606}
                        return dictNow
                    if "请输入发票代码" in driver.page_source:
                        print("请输入发票代码")
                        dictNow = {'errMsg': "ERROR请输入发票代码", 'state': 607}
                        return dictNow
                    if "请输入开具金额" in driver.page_source:
                        print("请输入开具金额")
                        dictNow = {'errMsg': "ERROR请输入开具金额", 'state': 608}
                        return dictNow
                    if "请输入开票日期" in driver.page_source:
                        print("请输入开票日期")
                        dictNow = {'errMsg': "ERROR请输入开票日期", 'state': 609}
                        return dictNow
                    if "请输入校验码" in driver.page_source:
                        print("请输入校验码")
                        dictNow = {'errMsg': "ERROR请输入校验码", 'state': 610}
                        return dictNow

                    if 'yzm_img' in driver.page_source:
                        self._state = "已经出现验证码标签"
                        print("出现验证码标签")
                        break
                    time.sleep(0.1)

                """
                验证码
                """
                time.sleep(0.5)
                try:
                    for i in range(50):
                        if '请输入验证码图片' in driver.page_source:
                            self._state = "已经成功渲染验证码"
                            print("成功渲染验证码")
                            break
                        time.sleep(0.1)
                    else:
                        print("5秒钟验证码还没有出现,重启")
                        print("错误截图", self.get_full_screen_oss())
                        self.driver.refresh()
                        continue
                    try:
                        # 不存在会抛异常
                        driver.find_element_by_id('yzminfo') \
                            .find_element_by_css_selector('font') \
                            .get_attribute('color')
                    except:
                        print("不打不带颜色的码,跳过")
                        continue

                    # 处理逻辑是：如果为空,换一张验证码.不为空则直接输入
                    imgCode1 = self.getCodeString()
                except:
                    print("未知错误")
                    traceback.print_exc()
                    continue

                print("成功识别", imgCode1)
                inputa = imgCode1
                driver.find_element_by_id('yzm').clear()
                driver.find_element_by_id('yzm').send_keys(inputa)
                print("【验证】已经完成所有信息输入")
                time.sleep(1)  # 这里延时未来可以调低一点,为了录屏
                action_chains = ActionChains(self.driver)
                action_chains.double_click(driver.find_element_by_id('checkfp')).perform()
                print("正在进行查验")
                time.sleep(1)
                for i in range(100):
                    if 'popup_ok' in driver.page_source or 'iframe' in driver.page_source:
                        break
                    time.sleep(0.1)
                if '超过该张发票当日查验次数' in driver.page_source:
                    print("超过次数")
                    dictNow = {'errMsg': "ERROR超过次数！无法返回信息", 'state': 601}
                    return dictNow
                    # 看输入是否有错误
                elif "发票代码有误!" in driver.page_source:
                    print("发票代码有误")
                    dictNow = {'errMsg': "ERROR发票代码有误！无法返回信息，请输入正确的数据或格式", 'state': 601}
                    return dictNow
                elif "发票号码有误!" in driver.page_source:
                    print("发票号码有误")
                    dictNow = {'errMsg': "ERROR发票号码有误！无法返回信息，请输入正确的数据或格式", 'state': 602}
                    return dictNow
                elif "开票日期有误!" in driver.page_source:
                    print("开票日期有误")
                    dictNow = {'errMsg': "ERROR开票日期有误！无法返回信息，请输入正确的数据或格式", 'state': 603}
                    return dictNow
                elif "开票金额有误!" in driver.page_source:
                    print("开票金额有误!")
                    dictNow = {'errMsg': "ERROR开票金额有误！无法返回信息，请输入正确的数据或格式", 'state': 604}
                    return dictNow
                elif '校验码有误!' in driver.page_source:
                    print("校验码有误")
                    dictNow = {'errMsg': "校验码有误！无法返回信息,请输入校验码或查看是否正确", 'state': 602}
                    return dictNow
                elif '一分钟' in driver.page_source:
                    print("访问过于频繁，休息60秒后再试")
                    # popup_ok
                    # driver.find_element_by_id('popup_ok').click()  # 点击搜索按钮
                    self._state = "由于访问频率太快,系统强制占用进程休息60秒"
                    time.sleep(60)
                    continue
                elif 'popup_ok' in driver.page_source:
                    print("验证码输入错误,重试流程")
                    continue
                elif 'iframe' in driver.page_source:
                    print("验证成功,跳转Iframe")
                    driver.switch_to_frame(0)
                    print(driver.page_source)
                    filePath = 'fapiao/' + fpdm + '.png'
                    driver.save_screenshot(filePath)
                    ossPath = fileUpdate(filePath)
                    invoiceData = {}
                    try:
                        invoiceData = self._parseInvoice(driver.page_source)
                    except:
                        invoiceData['errMsg'] = "ERROR解析结构异常,发现新模板或者改版,请将这个返回交付开发者进行模板添加"
                        invoiceData['html'] = driver.page_source
                        invoiceData['errMsgText'] = traceback.format_exc()
                    dictNow.update({'data': invoiceData,
                                    'imgFile': ossPath,
                                    'errMsg': "success!",
                                    'state': 200})
                    return dictNow
            except:
                print("未知异常,进行上报")
                traceback.print_exc()
                dictNow = {}
                dictNow.update({'errMsg': traceback.format_exc(), 'state': 599})
                return dictNow

    def duplicate(self, input):
        """
                去重逻辑,发票代码显示在发标的左上方，发票号码在发票的右上方。
        发票代码一般来说一次购票基本一样，很难得会出现不一致的情况，发票号码在本发票代码编号下为唯一。
        发票代码可以理解为目录，发票号码为目录下的明细。

        :param input:
        :return:
        """
        dictDup = {'fpdm': input['fpdm'], 'fphm': input['fphm'], 'kprq': input['kprq'], 'kjje': input['kjje']}
        item = self.db['auto_' + type(self).__name__].find_one(dictDup)
        if item is not None:
            return dict(item)
        else:
            return False

    """
    获取验证码主方法,直接被deal调用
    """

    def getCodeString(self):

        url_cw = "http://39.108.188.34:9020/middleware/identifyingChinese/upload.go?filename=fapiao"  # 中文外网
        url_ew = "http://39.108.188.34:9021/middleware/identifyingEnglish/upload.go?filename=fapiao"  # 英文外网
        # url_c = "http://localhost:9020/middleware/identifyingChinese/upload.go"  # 中文本地
        # url_e = "http://localhost:9021/middleware/identifyingEnglish/upload.go"  # 英文本地
        urlList = [url_cw, url_ew]
        # urlList = [url_c, url_e, url_cw, url_ew]

        ansList = []

        while True:
            # 尝试到成功为止
            for url in urlList:
                try:  # 异常处理
                    try:
                        filePath = self.get_image()
                    except:
                        traceback.print_exc()
                        filePath = self.get_image_old()
                        # TODO 未来删除
                        ossUrl = fileUpdate(filePath)
                        self.db['test_yanzhengma'].insert_one({'ossUrl': ossUrl})
                    try:  # 图片删除
                        file = {'file': open(filePath, 'rb')}
                        colorStr = filePath.split('_')[-1].replace('.png', '')
                        file.update({'etc': colorStr})
                        print("发起对【王博】验证码接口的请求 颜色", colorStr, "文件", filePath)
                        response = requests.post(url, files=file)
                        print("发起对【王博】验证码接口返回", response.text)
                        try:
                            dict_res = json.loads(response.text)
                        except:
                            print("验证码接口未返回JSON格式")
                            continue
                        if dict_res['state'] == 200:
                            code = dict_res['data']
                            ansList.append(code)
                        else:
                            print("算法要求更换验证码")
                            break
                    finally:
                        os.remove(filePath)
                        print("删除验证码")
                except NoSuchElementException:
                    traceback.print_exc()
                    print("【发票验真平台】出现定位不到标签的错误，可能是登陆状态丢失，重新进行登陆,并保存截图")
                    ossUrl = self.get_full_screen_oss()
                    print("截图ossURL,并休息3秒", ossUrl)
                    self.driver.refresh()
                    time.sleep(3)


                except:
                    print("验证码接口请求异常", url)
                    traceback.print_exc()
            if len(ansList) > 0:
                print("至少有一个有正确结果,随机取一个返回")
                ans = random.sample(ansList, 1)[0]
                print("返回", ans)
                return ans
            # 更换图片再来一次
            self.click100('yzm_img')

    """
    获取验证码图片
    """

    def get_image(self):
        global left_Moren, top_Moren

        img = self.driver.find_elements_by_css_selector("img")[-1]
        pictureData = img.get_attribute('src').split('base64,')[-1]
        # print("base64Encode", pictureData)
        try:
            pictureDataB64 = base64.b64decode(pictureData)
        except:
            if (len(pictureData) % 3 == 1):
                pictureData += "=="
            elif (len(pictureData) % 3 == 2):
                pictureData += "="
            pictureDataB64 = base64.b64decode(pictureData)
        colorStr = self.driver.find_element_by_id('yzminfo') \
            .find_element_by_css_selector('font') \
            .get_attribute('color')
        if not os.path.exists('./code'):
            os.makedirs('./code')
        if not os.path.exists('./fapiao'):
            os.makedirs('./fapiao')

        filePath = 'code/imgCode2' + str(time.time()).replace('.', '_') + '_new_{}.png'.format(colorStr)

        with open(filePath, 'wb')as fp:
            fp.write(pictureDataB64)

        # 验证码识别
        return filePath  # 得到的就是验证码

    def get_snap(self):  # 对目标网页进行截屏.这里截的是全屏
        fileName = str(uuid.uuid1()) + 'full_snap.png'
        self.driver.save_screenshot(fileName)
        page_snap_obj = Image.open(fileName)
        os.remove(fileName)
        return page_snap_obj

    def setAttribute(self, elementObj, attributeName, value):
        # 封装设置页面对象的属性值的方法
        # 调用JavaScript代码修改页面元素的属性值，arguments[0]－［2］分别会用后面的
        # element、attributeName和value参数值进行替换，并执行该JavaScript代码
        self.driver.execute_script("arguments[0].setAttribute\
     (arguments[1],arguments[2])", elementObj, attributeName, value)

    def get_image_old(self):  # 对验证码所在位置进行定位，然后截取验证码图片
        global left_Moren, top_Moren
        while True:
            img = self.driver.find_elements_by_css_selector("img")[-1]
            loc = img.location
            size = img.size
            # 图片和标签大小不一致的,不能通过size获取图片,截图会偏移
            for i in range(100):
                if loc['x'] == 0:
                    time.sleep(0.1)
                    continue
                else:
                    left_Moren = loc['x']
                    top_Moren = loc['y']
                    print("已对验证码图片位置做死定位,从而降低定位不到时候的命中率")
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
            colorStr = self.driver.find_element_by_id('yzminfo') \
                .find_element_by_css_selector('font') \
                .get_attribute('color')
            filePath = 'code/imgCode2' + str(time.time()).replace('.', '_') + '_{}.png'.format(colorStr)
            image_obj.save(filePath)
            # 验证码识别
            return filePath  # 得到的就是验证码

    def click100(self, tagId):
        time.sleep(1)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(self.driver.find_element_by_id(tagId), 10, 10)
        action_chains.click()
        action_chains.perform()
        print("完成按键操作", tagId)


if __name__ == '__main__':
    # # 1

    # fpdm = "4403181130"
    # fphm = "27671246"
    # kprq = "20180920"
    # kjje = "351.69"
    # #2
    # fpdm = "4403181130"
    # fphm = "27671246"
    # kprq = "20180920"
    # kjje = "351.69"
    # # 3
    fpdm = "1100182130"
    fphm = "15024752"
    kprq = "20180614"
    kjje = "18679.25"
    data = {'fpdm': fpdm, 'fphm': fphm, 'kprq': kprq, 'kjje': kjje}
    print(WebDriverPool(dBean=fapiaoImpl, num=1, headless=False).getOneDriver().deal(data))
