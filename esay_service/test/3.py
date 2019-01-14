import requests
from gongju import format_headers

header = """
Host: www.qichacha.com
Connection: keep-alive
Content-Length: 247
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://www.qichacha.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.qichacha.com/user_login
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: acw_tc=7160b5a715460707077541926e83198ccf7568a05325a5f3621314a639; QCCSESSID=vpojr1hbkloejjm0af2uoe8jl4; zg_did=%7B%22did%22%3A%20%22167f8ff123a327-08bbf69642925d-784a5037-ff000-167f8ff123c4b2%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201546070725186%2C%22updated%22%3A%201546070725186%2C%22info%22%3A%201546070725192%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; UM_distinctid=167f8ff13b6388-04bbaa88854182-784a5037-ff000-167f8ff13b711e; CNZZDATA1254842228=1400657672-1546070255-%7C1546070255; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1546070726; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1546070726; saveFpTip=true
"""
headers = format_headers(header)
challenge = '2e4c0f5daf2070bc68fb318481276895kl'
validate = '545465cef68ecf1855f3df734ebe0245'
data = 'phone_prefix=%2B86&nameNormal=18923477217&pwdNormal=pk12580&geetest_challenge={}&geetest_validate={}&geetest_seccode={}%7Cjordan&verify_type=2'.format(challenge,validate,validate)
resp = requests.post('https://www.qichacha.com/user_loginaction', data=data, verify=False, headers=headers)
print(resp)
print(resp.text)
print(resp.cookies.get_dict())