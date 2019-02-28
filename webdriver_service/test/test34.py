# 沈阳北方建设股份有限公司
import json

import requests

companyName = "沈阳北方建设股份有限公司"
url = "http://39.108.188.34:9089/spider/zhongdeng.go?companyName={}".format(companyName)
text = requests.get(url).text
objJson = json.loads(text)
print(objJson)
print("PDF数量", len(objJson['ansList']))

url = "http://39.108.188.34:8891/BatchPdfCode"
data = {
    "pdfs": objJson['ansList'],
    "billNums": ["01287153", "01238774"],
}

data = json.dumps(data)
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=data, headers=headers)
print(response.text)
