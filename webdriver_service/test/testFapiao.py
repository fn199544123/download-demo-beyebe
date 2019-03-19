import json

import requests

url = "https://zjfpcyweb.bjsat.gov.cn/WebQuery/yzmQuery?fpdm=1100182130&fphm=15024752&r=0.13089881319166152&v=V1.0.07_001&nowtime=1552902966024&area=1100&publickey=A1732BD5C5FDEDA762686831E15958D0&_=1552902933340"
jsonObj=json.loads(requests.get(url, verify=False).text)
print(jsonObj)
