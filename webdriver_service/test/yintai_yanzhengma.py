

import requests

if __name__ == '__main__':
    # 发票-英文验证码 端口9020
    # 调用接口识别验证码
    print('9020')
    file = {'file': open("9020red.png", 'rb'), 'etc': 'red'}
    url = "http://39.108.188.34:9020/middleware/identifyingChinese/upload.go?filename=caipan"
    response = requests.post(url, files=file)
    code = response.text
    print(code)
    # 发票-英文验证码 端口9021
    # 调用接口识别验证码
    print('9021')
    file = {'file': open("9021red.png", 'rb'), 'etc': 'red'}
    url = "http://39.108.188.34:9021/middleware/identifyingEnglish/upload.go?filename=caipan"
    response = requests.post(url, files=file)
    code = response.text
    # 中登网验证码 端口9022
    # 调用接口识别验证码
    print(code)
    print('9022')
    file = {'file': open("9022.jpg", 'rb')}
    url = "http://39.108.188.34:9022/middleware/zd_identifyingEnglish/upload.go?filename=fapiao"
    response = requests.post(url, files=file)
    code = response.text
    print(code)