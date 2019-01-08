import requests

cookies = {'QCCSESSID': 'ck3e09qbhsqn2eh8g6195i4cm1'}
session = requests.session()
html = session.get("https://www.qichacha.com",cookies=cookies).text
print(html)
