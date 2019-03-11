# # -*- coding:utf-8 -*-
# # @author: lixuxing
# # @contact: 13542272776@163.com
# # @time: 2018/10/26 8:47
#
#
# from PIL import Image, ImageEnhance
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# import cv2
# import numpy as np
# from io import BytesIO
# import time, requests
# import random as r
#
# URL = 'http://dun.163.com/trial/jigsaw'
#
#
# class CrackSlider():
#     """
#     通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并模仿人类行为破解滑动验证码
#     """
#
#     def __init__(self):
#         super(CrackSlider, self).__init__()
#         # 实际地址
#         self.url = URL
#         self.driver = webdriver.Chrome()
#         self.wait = WebDriverWait(self.driver, 30)
#         self.zoom = 1
#
#     def open(self):
#         self.driver.get(self.url)
#
#     def get_pic(self):
#         """
#         只需下载背景图（target_img）
#         :return:
#         """
#         # target
#         target = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_bg-img')))
#         template = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_jigsaw')))
#         target_link = target.get_attribute('src')
#         # template_link = template.get_attribute('src')
#         target_img = Image.open(BytesIO(requests.get(target_link).content))
#         # template_img = Image.open(BytesIO(requests.get(template_link).content))
#         target_img.insert('target.jpg')
#         # template_img.save('template.png')
#         size_orign = target.size
#         local_img = Image.open('target.jpg')
#         size_loc = local_img.size
#         self.zoom = 320 / int(size_loc[0])
#
#     def get_tracks(self, distance):
#         """
#         计算滑块运动轨迹
#         :param distance:滑块起始位置和终点位置的水平位移
#         :return:
#         """
#         mylog.infodistance)
#         distance += 20
#         v = 0
#         t = 0.2
#         forward_tracks = []
#         current = 0
#         mid = distance * 3 / 5
#         while current < distance:
#             if current < mid:
#                 a = 2
#             else:
#                 a = -3
#             s = v * t + 0.5 * a * (t ** 2)
#             v = v + a * t
#             current += s
#             forward_tracks.append(round(s))
#
#         # 轨迹按照实际情况微调
#         back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1]
#         forward_tracks_2 = [1, 1, 1, 1, 1, 1, 1, 1]
#         return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks, 'forward_tracks_2': forward_tracks_2}
#
#     def match(self, target):
#         """
#         匹配滑块终点位置坐标
#         :param target: 背景图文件途径("target.jpg")
#         :return res[0]:终点位置滑块左上角的横坐标
#         """
#         img = cv2.imread(target)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         tmp = cv2.imread('tmp2.png', 0)
#         _, th0 = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
#         _, th1 = cv2.threshold(tmp, 200, 255, cv2.THRESH_BINARY_INV)
#
#         canny0 = cv2.Canny(th0, 30, 70)
#         canny1 = cv2.Canny(th1, 30, 70)
#
#         h, w = canny0.shape[:2]
#
#         res = cv2.matchTemplate(canny0, canny1, cv2.TM_CCOEFF)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         left_top = max_loc  # 左上角
#         right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
#         cv2.rectangle(img, left_top, right_bottom, 255, 2)  # 画出矩形位置
#         # mylog.infoleft_top, right_bottom)
#         res = list(left_top)
#         res[0] = res[0] + 3  # 按实际情况微调
#         res[1] = res[1] + 27
#         return res[0]
#
#     def crack_slider(self):
#         """
#         模拟鼠标点击和拖动滑块
#         :return:
#         """
#         self.open()
#         target = 'target.jpg'
#         self.get_pic()
#         distance = self.match(target)
#         tracks = self.get_tracks((distance) * self.zoom)  # 对位移的缩放计算
#         mylog.infotracks)
#         slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'yidun_slider')))
#         ActionChains(self.driver).click_and_hold(slider).perform()
#
#         for track in tracks['forward_tracks']:
#             ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()
#
#         time.sleep(r.uniform(0.2, 0.7))
#         for back_tracks in tracks['back_tracks']:
#             ActionChains(self.driver).move_by_offset(xoffset=back_tracks, yoffset=0).perform()
#
#         time.sleep(r.uniform(0.2, 0.7))
#         for forward_tracks in tracks['forward_tracks_2']:
#             ActionChains(self.driver).move_by_offset(xoffset=forward_tracks, yoffset=0).perform()
#
#         ActionChains(self.driver).move_by_offset(xoffset=-3, yoffset=0).perform()
#         ActionChains(self.driver).move_by_offset(xoffset=3, yoffset=0).perform()
#         # time.sleep(0.5)
#         time.sleep(r.uniform(0.2, 0.7))
#         ActionChains(self.driver).release().perform()
#         # try:
#         #     failure = self.wait.until(
#         #         EC.text_to_be_present_in_element((By.CLASS_NAME, 'yidun_tips__text'), '向右拖动滑块填充拼图'))
#         #     mylog.infofailure)
#         # except:
#         #     mylog.info'验证成功')
#         #     return None
#         #
#         # if failure:
#         #     self.crack_slider()
#
#         if __name__ == '__main__':
#             c = CrackSlider()
#
#     while True:
#         c.crack_slider()
#         time.sleep(3)
