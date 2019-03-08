# 接口3，接口4测试DEMO
import json
import requests

data = {
    "companyName": "沈阳北方建设股份有限公司",
    "billNums": ["01287153", "01238774"],
    "afterDate": "19000101"
}

headers = {"Content-Type": "application/json"}

text1 = requests.post("http://39.108.188.34:9089/spider/zhongdeng.go", headers=headers).text
text2 = requests.post("http://39.108.188.34:8891/BatchPdfCode", data=text1, headers=headers).text
obj1 = json.loads(text1)
obj2 = json.loads(text2)
print("PDF数量", len(obj1['pdfs']))
print("交叉验证结果", obj2)
