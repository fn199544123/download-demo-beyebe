from selenium import webdriver
from pymongo import MongoClient
import requests
from requests.cookies import RequestsCookieJar
from gongju import format_headers


def add_cookies(chrome_driver, _cookies: str):
    _format_cookies = _cookies.strip().replace('\n', '').replace(' ', '').split(';')
    dict_cookies = {}
    for key_value in _format_cookies:
        if len(key_value.split('=')) == 2:
            dict_cookies.update({'name': key_value.split('=')[0], 'value': key_value.split('=')[1]})
        else:
            dict_cookies.update({'name': key_value.split('=')[0], 'value': '='.join(key_value.split('=')[1::])})
        chrome_driver.add_cookie(dict_cookies)
    return chrome_driver


def get_cookies(url, identity, password):
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url=url)
    driver.delete_all_cookies()
    cookies = "acw_tc=0ed717a515460692760421572e4747068954a3d02400a77631de635019; QCCSESSID=t3vn28p04vkj8l2r7lm7rlohs4; zg_did=%7B%22did%22%3A%20%22167f8e9380113-005213f68e383-784a5037-ff000-167f8e9380221b%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201546069293064%2C%22updated%22%3A%201546069293064%2C%22info%22%3A%201546069293070%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; UM_distinctid=167f8e938ae2a9-06757ad8d5f22d-784a5037-ff000-167f8e938af117; CNZZDATA1254842228=858686226-1546064855-%7C1546064855; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1546069294; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1546069294; saveFpTip=true"
    # add_cookies(driver,cookies)
    driver.add_cookie({'name':'QCCSESSID','value':'vpojr1hbkloejjm0af2uoe8jl4'})
    driver.refresh()


if __name__ == '__main__':
    get_cookies(url='https://www.qichacha.com/user_login', identity='13267038234', password='111')
