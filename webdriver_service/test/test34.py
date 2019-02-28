# 沈阳北方建设股份有限公司
import json

import requests

companyName = "沈阳北方建设股份有限公司"
url = "http://39.108.188.34:9089/spider/zhongdeng.go?companyName={}".format(companyName)
text = requests.get(url).text
objJson = json.loads(text)
print(objJson)