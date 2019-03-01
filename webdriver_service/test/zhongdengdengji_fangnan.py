# -*- coding: utf-8 -*-

import requests
import json


# url = "http://39.108.188.34:9090/spider/zhongdengdengji.go"
url = "http://localhost:9090/spider/zhongdengdengji.go"

input = {
    "timelimit": "1年",
    "title": "测试归档号",
    "maincontractno": "转让合同编码",
    "maincontractcurrency": "人民币",
    "maincontractsum": "10000",
    "description": "我是可爱的小描述",
    "addDebtorList": [
        {
            # 金融机构
            "debtorType": "金融机构",
            "debtorName": "出让人名称",
            "financeCode": "abc123abc123abc123",
            "businessCode": "abc",
            "lei": "123",
            "responsiblePerson": "江泽民",
            "country": "中国",
            "province": "黑龙江省",
            "city": "哈尔滨市",
            "address": "美丽的松花江",
        }
    ]
}
data = json.dumps(input)
# data="""
# {
#   "timelimit": "59",
#   "title": "123",
#   "maincontractno": "123",
#   "maincontractcurrency": "123",
#   "maincontractsum": "10000",
#   "description": "123",
#   "addDebtorList": [
#     {
#       "debtorType": "123",
#       "debtorName": "123",
#       "financeCode": "abc123abc123abc123",
#       "businessCode": "abc",
#       "lei": "123",
#       "responsiblePerson": "123",
#       "country": "123",
#       "province": "123",
#       "city": "123",
#       "address": "123"
#     }
#     ]
# }
# """
headers = {
'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    "Content-Type": "application/json"}
response = requests.post(url,data=data,headers=headers,timeout=(500,500))
print(response.text)

# testAccount = [{'account': 'ytbl0011', 'keyword': 'ytbl0011aDmin'}]
