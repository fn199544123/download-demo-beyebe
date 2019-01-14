import requests
from gongju import format_headers

header = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: acw_tc=77939ca515468288046942551ee28171b2a6d7f06214c807c4bb6070c8; QCCSESSID=ck3e09qbhsqn2eh8g6195i4cm1; UM_distinctid=168264a446e35e-0037c245e54059-b781636-ff000-168264a446f4a5; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1546830628; hasShow=1; _uab_collina=154683062831903366159232; saveFpTip=true; zg_did=%7B%22did%22%3A%20%22168264a492572-03ea6919b2df42-b781636-ff000-168264a492662c%22%7D; CNZZDATA1254842228=2130430023-1546828033-%7C1546838833; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201546841666791%2C%22updated%22%3A%201546843997907%2C%22info%22%3A%201546830629175%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1546843998
Host: www.qichacha.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
"""
headers = format_headers(header)
resp = requests.get('https://www.qichacha.com/', headers=headers, verify=False)
print(resp)
print(resp.text)

