import requests
import json

# 接口1、2测试DEMO
ossPath = "http://ibossapi.oss-cn-shenzhen.aliyuncs.com/beyebe/其他30张发票2019-03-21 11_9661329e5fcb09c91124e0002ce3ba78.pdf"
# ossPath="http://boss.yintaifac.com:8888/obpm/uploads/item/2019/a1b501db-29c4-4fc3-822b-de0ac87aadfc.pdf"
data = {"bill": {"ossPath": ossPath}}

headers = {"Content-Type": "application/json"}
text1 = requests.post("http://39.108.188.34:8893/QrcodeDetectV3", data=json.dumps(data).encode(), headers=headers).text
print("发票识别结果")
print(text1)
text2 = requests.post("http://39.108.188.34:9088/spider/fapiaoList.go", data=text1.encode(), headers=headers).text
obj1 = json.loads(text1)
obj2 = json.loads(text2)

print("发票验真结果")
print(text2)
