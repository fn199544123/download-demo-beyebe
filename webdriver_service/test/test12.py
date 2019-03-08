import requests
import json

data = {
    "bill": {
        'ossPath': "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190222/cc47c589fcea0609b6ca1aadfaac7d6c.pdf"
    }
}
headers = {"Content-Type": "application/json"}
text1 = requests.post("http://39.108.188.34:8893/QrcodeDetectV3", data=json.dumps(data).encode(), headers=headers).text
text2 = requests.post("http://39.108.188.34:9088/spider/fapiaoList.go", data=text1.encode(), headers=headers).text
obj1 = json.loads(text1)
obj2 = json.loads(text2)
print("发票识别结果", obj1)
print("发票验真结果", obj2)
