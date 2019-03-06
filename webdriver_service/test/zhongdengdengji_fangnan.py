# -*- coding: utf-8 -*-

import requests
import json

# url = "http://39.108.188.34:9090/spider/zhongdengdengji.go"
url = "http://localhost:9090/spider/zhongdengdengji.go"

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
            "financeCode": "123456000001111111",
            "businessCode": "",
            "lei": "",
            "responsiblePerson": "测试法人1",
            "country": "中国",
            "province": "黑龙江省",
            "city": "哈尔滨市",
            "address": "北京天安门",
        }

    ]

}
inputString="""
{
  "timelimit": "1年",
  "title": "GD20190306001",
  "maincontractno": "GY20180723134-2019",
  "maincontractcurrency": "人民币",
  "maincontractsum": "490605.3",
  "description": "YT20190228002东莞市民兴电缆有限公司与佛山市南海现代城投资开发有限公司就FS-FSYDH-01Q-施工-0001，转让应收账款金额490605.3元，东莞市民兴电缆有限公司已出具应收账款转让通知书，对应的发票号及金额为25275799/545117，到期日2020-02-26。付款方万科企业股份有限公司已出具编号为ZB00002-20190227-0095的付款确认及授权书",
  "ossPathList": [
    "http://boss.yintaifac.com:8888/obpm/uploads/item/2019/070c9b11-61b4-4d81-a2c6-f9343eddc5bd.jpg"
  ],
  "addDebtorList": [
    {
      "debtorType": "企业",
      "debtorName": "东莞市民兴电缆有限公司",
      "orgCode": "",
      "businessCode": "91441900721158959T",
      "lei": "",
      "responsiblePerson": "吴惠明",
      "industryCode": "制造业",
      "scale": "中型企业",
      "country": "中国",
      "province": "广东省",
      "city": "东莞市",
      "address": "凤岗镇龙平公路宏盈工业园"
    }
  ]
}

"""
# data = json.dumps(input)
data=inputString
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    "Content-Type": "application/json"}
response = requests.post(url, data=data, headers=headers, timeout=(500, 500))
print(response.text)

# testAccount = [{'account': 'ytbl0011', 'keyword': 'ytbl0011aDmin'}]
