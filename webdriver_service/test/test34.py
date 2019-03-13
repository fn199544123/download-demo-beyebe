import json
import requests

# 接口3，接口4测试DEMO
data = {
    "companyName": "东莞市民兴电缆有限公司",
    "billNums": ["25275763"],
    "afterDate": "20190121"
}

headers = {"Content-Type": "application/json"}

text1 = requests.post("http://39.108.188.34:9089/spider/zhongdeng.go", data=json.dumps(data).encode(),
                      headers=headers).text

print("查询结果")
print(text1)
text2 = requests.post("http://39.108.188.34:8891/BatchPdfCode", data=text1.encode(), headers=headers).text
# obj1 = json.loads(text1)
# obj2 = json.loads(text2)

print("交叉验证结果")
print(text2)
