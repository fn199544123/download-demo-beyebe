# -*- coding: utf-8 -*-

import requests
import json

# url = "http://39.108.188.34:9090/spider/zhongdengdengji.go"
url = "http://localhost:9088/spider/fapiaoList.go"

data = """
{"message":"success","state":200,"rate":100,"data":[{"filePath":"/","result":[{"page":1,"state":502,"ossPath":"http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190307/c92fb84ee375c0c0c4f2fd7d5d9b9eb9.png"},{"invoiceCode":"1100162350","invoiceNo":"17930113","date":"20190123","checkCode":"","ossPath":"http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190307/033eb6be393b1fcf986e3c7f6a325497.png","amount":"900900.09","state":201,"page":2},{"page":3,"state":502,"ossPath":"http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190307/f53eed445191e43076143460c9e13edb.png"}],"fileName":"cc47c589fcea0609b6ca1aadfaac7d6c.pdf"}]}
"""

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    "Content-Type": "application/json"}
response = requests.post(url, data=data, headers=headers, timeout=(500, 500))
print(response.text)

# testAccount = [{'account': 'ytbl0011', 'keyword': 'ytbl0011aDmin'}]
