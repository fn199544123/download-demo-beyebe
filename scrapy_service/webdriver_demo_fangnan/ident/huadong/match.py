# -*- coding:utf-8 -*-
# @author: lixuxing
# @contact: 13542272776@163.com
# @time: 2018/10/25 18:36
import cv2


def match(target):
    img = cv2.imread(target, 0)
    tmp = cv2.imread('tmp2.png', 0)
    _, th0 = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

    _, th1 = cv2.threshold(tmp, 200, 255, cv2.THRESH_BINARY_INV)

    canny1 = cv2.Canny(th1, 30, 70)
    canny0 = cv2.Canny(th0, 30, 70)

    h, w = canny0.shape[:2]

    # 相关系数匹配方法：cv2.TM_CCOEFF
    res = cv2.matchTemplate(th0, th1, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    left_top = max_loc  # 左上角
    right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
    cv2.rectangle(img, left_top, right_bottom, 255, 2)  # 画出矩形位置
    print(left_top, right_bottom)

    res = list(left_top)
    res[0] = res[0] + 27
    res[0] = res[1] + 27

    return res[0]


if __name__ == "__main__":
    target = 'target.jpg'
    print(match(target))
