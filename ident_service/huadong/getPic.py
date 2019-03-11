# -*- coding:utf-8 -*-
# @author: lixuxing
# @contact: 13542272776@163.com
# @time: 2018/10/26 9:38
from PIL import Image, ImageEnhance
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import cv2
import numpy as np
from io import BytesIO

import time, requests

# driver = webdriver.Chrome()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
zoom = 1

def open():
    url = 'http://dun.163.com/trial/jigsaw'
    driver.get(url)


def get_pic(i):
    time.sleep(2)
    target = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_bg-img')))
    template = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_jigsaw')))
    target_link = target.get_attribute('src')
    target_img = Image.open(BytesIO(requests.get(target_link).content))
    target_img.insert('target_{}.jpg'.format(i))
    driver.refresh()


if __name__ == "__main__":
    open()
    for i in range(45, 100):
        get_pic(i)
        time.sleep(2)