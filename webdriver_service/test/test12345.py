import requests
import json
import time

headers = {"Content-Type": "application/json"}
# 接口1、2测试DEMO
data12 = {
    "bill": {
        'ossPath': "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190222/bffc69d60400cb4365f5ca2528fd27f2.pdf"
    }
}
# 接口3，接口4测试DEMO
data34 = {
    "companyName": "沈阳北方建设股份有限公司",
    "billNums": ["01287153", "01238774"],
    "afterDate": "19000101"
}

"""
发票OCR识别
"""

timeStart = time.time()
text1 = requests.post("http://39.108.188.34:8893/QrcodeDetectV3", data=json.dumps(data12).encode(),
                      headers=headers).text
print("发票识别结果")
print(text1)
print("用时", time.time() - timeStart)
"""
发票验真
"""
timeStart = time.time()
text2 = requests.post("http://39.108.188.34:9088/spider/fapiaoList.go", data=text1.encode(), headers=headers).text
print("发票验真结果")
print(text2)
print("用时", time.time() - timeStart)

"""
中登网查询
"""
timeStart = time.time()
text3 = requests.post("http://39.108.188.34:9089/spider/zhongdeng.go", data=json.dumps(data34).encode(),
                      headers=headers).text
obj3 = json.loads(text3)
print("用时", )
print("中登网查询结果", text3)
print("用时", time.time() - timeStart)

"""
PDF交叉比对
"""
timeStart = time.time()
text4 = requests.post("http://39.108.188.34:8891/BatchPdfCode", data=text3.encode(), headers=headers).text
obj4 = json.loads(text4)
print("交叉验证结果", obj4)
print("用时", time.time() - timeStart)

"""
中登网登记
"""
timeStart = time.time()
input = {
    "timelimit": "1年",
    "title": "测试归档号",
    "maincontractno": "转让合同编码",
    "maincontractcurrency": "人民币",
    "maincontractsum": "10000",
    "description": "我是可爱的小描述",
    "addDebtorList": [
        {
            # 企业
            "debtorType": "企业",
            "debtorName": "可爱的比一比",
            "orgCode": "abcd",
            "businessCode": "1234",
            "lei": "777",
            "responsiblePerson": "毛泽东",
            "industryCode": "农、林、牧、渔业",
            "scale": "大型企业",
            "country": "中国",
            "province": "广东省",
            "city": "深圳市",
            "address": "可爱的南山区",
        }
    ],
    "ossPathList": [
        {
            "filename": "东莞民兴YT20190228002.jpg",
            "path": "http://boss.yintaifac.com:8888/obpm/uploads/item/2019/070c9b11-61b4-4d81-a2c6-f9343eddc5bd.jpg"
        }
    ]
}
headers = {"Content-Type": "application/json"}
text5 = requests.post("http://39.108.188.34:9090/spider/zhongdengdengji.go", data=json.dumps(input).encode(),
                      headers=headers).text
print("预览测试")
print(json.loads(text5))
print("用时", time.time() - timeStart)

# testAccount = [{'account': 'ytbl0011', 'keyword': 'ytbl0011aDmin'}]
