# -*- coding: utf-8 -*-

import requests
import json

url = "http://39.108.188.34:9090/spider/zhongdengdengji.go"
# url = "http://localhost:9090/spider/zhongdengdengji.go"

input = {
    "timelimit": "1年",
    "title": "GD20190305001",
    "maincontractno": "YT20181228001",
    "maincontractcurrency": "人民币",
    "maincontractsum": "100000",
    "description": "Y0181228001测试供应商有限公司与测试项目有限公司就SW00002-20181226-1204，转让应收账款金额100000元T2，测试供应商有限公司已出具应收账款转让通知书，对应的发票号及金额为1111/50000，5555/50000，到期日2018-12-29。付款方万科企业股份有限公司已出具编号为ZB00002-20181226-1204的付款确认及授权书",
    "addDebtorList": [
        {
            # 金融机构
            "debtorType": "企业",
            "debtorName": "测试供应商有限公司",
            "orgCode": "9144030068375453XL",
            "businessCode": "9144030068375453XL",
            "lei": "#*¥#*（&¥#（*&¥（）",
            "responsiblePerson": "测试法人1",
            "country": "中国",
            "province": "黑龙江省",
            "city": "哈尔滨市",
            "address": "北京天安门",
        }

    ]

}

data = json.dumps(input)

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    "Content-Type": "application/json"}
response = requests.post(url, data=data, headers=headers, timeout=(500, 500))
print(response.text)

# testAccount = [{'account': 'ytbl0011', 'keyword': 'ytbl0011aDmin'}]
