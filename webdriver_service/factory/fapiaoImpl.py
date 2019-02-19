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
from selenium.common.exceptions import TimeoutException
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
# class fapiaoImpl(WebDriverImp):

class fapiaoImpl(WebDriverRemoteImp):

    def getDriverPort(self):
        return 5440

    def _deal(self, input):
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
                while True:
                    if 'yzm_img' in driver.page_source:
                        print("出现验证码标签")
                        break
                """
                验证码
                """
                try:
                    for i in range(100):
                        if '请输入验证码图片' in driver.page_source:
                            print("成功渲染验证码")
                            break
                    else:
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
                    dictNow = {'errMsg': "超过次数！无法返回信息", 'state': 601}
                    return dictNow
                elif '开票日期有误' in driver.page_source:
                    print("开票日期有误")
                    dictNow = {'errMsg': "开票日期有误！无法返回信息，请输入正确的数据或格式，例如20190101", 'state': 602}
                    return dictNow
                elif '校验码有误!' in driver.page_source:
                    print("校验码有误")
                    dictNow = {'errMsg': "校验码有误！无法返回信息,请输入校验码或查看是否正确", 'state': 602}
                    return dictNow
                elif '一分钟' in driver.page_source:
                    print("访问过于频繁，休息60秒后再试")
                    # popup_ok
                    # driver.find_element_by_id('popup_ok').click()  # 点击搜索按钮
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
                    dictNow.update({'html': driver.page_source,
                                    'imgFile': ossPath,
                                    'errMsg': "success!",
                                    'state': 200})
                    return dictNow
            except:
                print("未知异常,暂停一分钟之后再进行")
                traceback.print_exc()
                time.sleep(60)
                continue

    def duplicate(self, input):
        """
                去重逻辑,发票代码显示在发标的左上方，发票号码在发票的右上方。
        发票代码一般来说一次购票基本一样，很难得会出现不一致的情况，发票号码在本发票代码编号下为唯一。
        发票代码可以理解为目录，发票号码为目录下的明细。

        :param input:
        :return:
        """
        dictDup = {'fpdm': input['fpdm'], 'fphm': input['fphm']}
        item = self.db['auto_' + type(self).__name__].find_one(dictDup)
        if item is not None:
            return dict(item)
        else:
            return False

    """
    获取验证码主方法,直接被deal调用
    """

    def getCodeString(self):

        url_cw = "http://121.9.245.186:9020/middleware/identifyingChinese/upload.go"  # 中文外网
        url_ew = "http://121.9.245.186:9021/middleware/identifyingEnglish/upload.go"  # 英文外网
        # url_c = "http://192.168.10.212:9020/middleware/identifyingChinese/upload.go"  # 中文本地
        # url_e = "http://192.168.10.212:9021/middleware/identifyingEnglish/upload.go"  # 英文本地
        urlList = [url_cw, url_ew]
        ansList = []

        while True:
            # 尝试到成功为止
            for url in urlList:
                try:  # 异常处理
                    filePath = self.get_image()
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
