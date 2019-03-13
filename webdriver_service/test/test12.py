import requests
import json

# 接口1、2测试DEMO
# data = {
#     "bill": {
#         'ossPath': "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190222/bffc69d60400cb4365f5ca2528fd27f2.pdf"
#     },
#     "model":2
# }
headers = {"Content-Type": "application/json"}
# text1 = requests.post("http://39.108.188.34:8893/QrcodeDetectV3", data=json.dumps(data).encode(), headers=headers).text
# print("发票识别结果")
# print(text1)
text1="""
{
  "data": [
    {
      "checkCode": "",
      "invoiceNo": "04475590",
      "invoiceCode": "4400184130",
      "amount": "203833.19",
      "date": "20181200"
    },
    {
      "checkCode": "",
      "invoiceNo": "04475591",
      "invoiceCode": "4400184130",
      "amount": "999999.99",
      "date": "20181206"
    },
    {
      "checkCode": "",
      "invoiceNo": "04475592",
      "invoiceCode": "4400184130",
      "amount": "999999.99",
      "date": "20181206"
    },
    {
      "checkCode": "",
      "invoiceNo": "04475593",
      "invoiceCode": "4400184130",
      "amount": "999999.99",
      "date": "20181206"
    }
  ]
}
"""
text2 = requests.post("http://localhost:9088/spider/fapiaoList.go", data=text1.encode(), headers=headers).text
obj1 = json.loads(text1)
obj2 = json.loads(text2)

print("发票验真结果")
print(text2)
