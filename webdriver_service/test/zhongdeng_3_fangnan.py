# -*- coding: utf-8 -*-

import requests
import json

url = "http://39.108.188.34:9089/spider/zhongdeng.go"
# url = "http://localhost:9090/spider/zhongdengdengji.go"

input = {
    "companyName": "深圳银泰保理有限公司",
    "afterDate":"20190101"
    ""
}

data = json.dumps(input)

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    "Content-Type": "application/json"}
response = requests.post(url, data=data, headers=headers, timeout=(500, 500))
print(response.text)

# testAccount = [{'account': 'ytbl0011', 'keyword': 'ytbl0011aDmin'}]
