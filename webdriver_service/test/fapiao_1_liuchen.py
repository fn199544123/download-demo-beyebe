import requests
import json

url = "http://39.108.188.34:8893/QrcodeDetectV3"
data = {
    "bill": {'ossPath': "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190222/cc47c589fcea0609b6ca1aadfaac7d6c.pdf"},
}
data = json.dumps(data)
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    "Content-Type": "application/json"}
response = requests.post(url, data=data, headers=headers, timeout=(500, 500))
print(response.text)
# 这是两次请求，下面的是单张，上面的是PDF 其中headers和data分别是请求头和post请求体
# data = {
#     "bill": {'ossPath': 'http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/docker/test2_0c7ed229f4fb2a3dacdf8f9f22b7677e.jpg'},
# }
# data = json.dumps(data)
# headers = {"Content-Type": "application/json"}
# response = requests.post(url, data=data, headers=headers)
# print(response.text)
