import requests

from logging_utils.log import mylog

cookies = {'QCCSESSID': 'ck3e09qbhsqn2eh8g6195i4cm1'}
session = requests.session()
html = session.get("https://www.qichacha.com",cookies=cookies).text
mylog.info(html)
