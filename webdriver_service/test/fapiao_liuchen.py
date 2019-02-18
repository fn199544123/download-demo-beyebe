import requests
import json
url = "http://192.168.10.49:8892/QrcodeDetectV3"
# data = {
#     "bill":{'ossPath':'http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/docker/test1_832204445033b6ae1e13afabca083b51.pdf'},
# }
# data = json.dumps(data)
# headers = {
# 'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
#     "Content-Type": "application/json"}
# response = requests.post(url,data=data,headers=headers,timeout=(500,500))
# print(response.text)
data = {
    "bill":{'ossPath':'http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/docker/test2_0c7ed229f4fb2a3dacdf8f9f22b7677e.jpg'},
}
data = json.dumps(data)
headers = {"Content-Type": "application/json"}
response = requests.post(url,data=data,headers=headers)
print(response.text)

