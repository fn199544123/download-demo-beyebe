# -*- coding: utf-8 -*-

import requests
import json

url = "http://39.108.188.34:9090/spider/zhongdengdengji.go"
# url = "http://localhost:9090/spider/zhongdengdengji.go"

input = {
  "isUpload":1,
  "timelimit": "1年",
  "title": "GD20190311001",
  "maincontractno": "GY20190307001-2019",
  "maincontractcurrency": "人民币",
  "maincontractsum": "2290942.58",
  "description": "华诚博远建筑工程有限公司与北京万城永辉置业有限公司就BJ-HC(2#)-01Q-施工-0031合同，转让应收账款金额2290942.58元，华诚博远建筑工程有限公司已出具应收账款转让通知书，对应的发票号及金额为69006501/1000000，69006502/107020.6，54848555/1000000，54848556/183921.98，到期日2020-03-04。付款方万科企业股份有限公司已出具编号为ZB00002-20190306-0025的付款确认及授权书",
  "ossPathList": [{"filename":"微信图片_20190307110953.jpg","path":"http://boss.yintaifac.com:8888/obpm/uploads/item/2019/9fc0eff2-3d0b-432c-92b4-ed8859d84fe8.jpg"}],
  "addDebtorList": [{
    "debtorType": "企业",
    "debtorName": "华诚博远建筑工程有限公司",
    "orgCode": "911101077226666481",
    "businessCode": "911101077226666481",
    "lei": "",
    "responsiblePerson": "吴峥",
    "industryCode": "建筑业",
    "scale": "中型企业",
    "country": "中国",
    "province": "北京市",
    "city": "北京市",
    "address": "石景山区八大处高科技园区西井路3号3号楼6364房间"
  }]
}

headers = {"Content-Type": "application/json"}
text1 = requests.post(url, data=json.dumps(input).encode(), headers=headers).text
print("预览测试")
print(json.loads(text1))

# testAccount = [{'account': 'ytbl0011', 'keyword': 'ytbl0011aDmin'}]
