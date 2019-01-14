import requests
from hashlib import md5
from gongju import format_headers
from pymongo import MongoClient

client = MongoClient('192.168.10.9', 27017)
db = client['hedgehog_spider']
db.authenticate(name='fangnan', password='Fang135')
col = db['qichacha_cookies']
cookies = col.find().sort('_id', -1)[0]['cookies']
header = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Host: www.qichacha.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134
"""
headers = format_headers(header)
res = requests.get(
    'https://www.qichacha.com/company_getinfos?unique=182249d7736fdb68960201022c19647a&companyname=%E6%B7%B1%E5%9C%B3%E5%B8%82%E6%AF%94%E4%B8%80%E6%AF%94%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&tab=susong',
    headers=headers, verify=False, cookies=cookies)
print(res)
print(res.text)
