import base64
import json

import execjs
import requests
import time


def getImgByBase64(base64Str):
    img = base64.b64decode(base64Str)
    file = open('test.jpg', 'wb')
    file.write(img)
    file.close()


if __name__ == '__main__':
    # 第一步，获取验证码
    fpdm = "1100182130"
    fphm = "15024752"
    kprq = "20180614"
    kjje = "18679.25"
    timeStamp = str(int(time.time()))
    url1 = "https://zjfpcyweb.bjsat.gov.cn/WebQuery/yzmQuery?callback=jQuery110205429715339927312_{timeStamp}&fpdm=1100182130&fphm=15024752&r=0.04577118100268329&v=V1.0.07_001&nowtime={timeStamp}&area=1100&_={timeStamp}".replace(
        "{timeStamp}", timeStamp).format(fphm, fpdm)
    session = requests.Session()
    session.get("https://inv-veri.chinatax.gov.cn/index.html", verify=False)
    # session.cert = "ssl/taxca.p7b"
    headers = {
        "Referer": "https://inv-veri.chinatax.gov.cn/index.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    request1Str = session.get(url1, verify=False).text
    callbackStr = "jQuery110205429715339927312_{timeStamp}(".replace("{timeStamp}", timeStamp)
    request1Str = request1Str.replace(callbackStr, "")[:-1]
    jsonObj1 = json.loads(request1Str)
    print("保存图片")
    getImgByBase64(jsonObj1['key1'])
    dateTime = jsonObj1['key2']
    index = jsonObj1['key3']
    # 第二步，找到应该使用的表单提交网站
    pass
    # 第三步 进行表单请求
    yzm = input("请输入验证码,颜色为{}".format(jsonObj1['key4']))
    timeStamp = str(int(time.time()))
    url3 = "https://zjfpcyweb.bjsat.gov.cn/WebQuery/vatQuery?" \
           "callback={callback}&" \
           "key1={fpdm}&" \
           "key2={fphm}&" \
           "key3={kprq}&" \
           "key4={kjje}&" \
           "fplx=01&" \
           "yzm={yzm}&" \
           "yzmSj={dateTime}&" \
           "index={index}&" \
           "area=1100&" \
           "_={timeStamp}".replace("{timeStamp}", timeStamp) \
        .replace("{fpdm}", fpdm) \
        .replace("{fphm}", fphm) \
        .replace("{kjje}", kjje) \
        .replace("{kprq}", kprq) \
        .replace("{index}", index) \
        .replace("{yzm}", yzm) \
        .replace("{dateTime}", dateTime)
    print("请求地址", url3)
    print(session.get(url3, verify=False).text)
    # 第四步 反混淆得到结果
