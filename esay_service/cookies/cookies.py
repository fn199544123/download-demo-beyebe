import json
import time
import requests
from requests.cookies import RequestsCookieJar
from pymongo import MongoClient
from gongju import format_headers


class VerificationCodeError(Exception):
    pass


class QichachaVerificationError(Exception):
    pass


class AutomaticAcquisitionCookies:
    """
    获取企查查账号cookies，调用时执行get_verify.
    name为账户，pwd为密码
    """

    def __init__(self):
        self.name = '18923477217'
        self.pwd = 'pk12580'
        client = MongoClient('192.168.10.9', 27017)
        db = client['hedgehog_spider']
        db.authenticate('fangnan', 'Fang135')
        self.col = db['qichacha_cookies']
        self.session = requests.session()

    def get_verify(self):
        gt_header = """    
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
            Accept-Encoding: gzip, deflate, br
            Accept-Language: zh-CN,zh;q=0.9
            Cache-Control: max-age=0
            Connection: keep-alive
            Host: www.qichacha.com
            Upgrade-Insecure-Requests: 1
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
            """
        gt_headers = format_headers(gt_header)
        gt_challenge = self.session.get('https://www.qichacha.com/index_getcap', headers=gt_headers, verify=False)
        assert gt_challenge.status_code == 200
        gt_challenge_Dict = json.loads(gt_challenge.text)
        if gt_challenge_Dict['success'] == 1:
            gt = gt_challenge_Dict['gt']
            challenge = gt_challenge_Dict['challenge']
            if gt and challenge:
                return self.approved(gt, challenge)
            else:
                raise VerificationCodeError('参数gt或challenge为空')
        else:
            return self.get_verify()

    def approved(self, gt, challenge):
        url = 'http://jiyanapi.c2567.com/shibie?gt={}&challenge={}&referer=https://www.qichacha.com/user_login&user=beyebe&pass=pk12580&return=json&model=0&format=utf8'.format(
            gt, challenge)
        resp = requests.get(url)
        assert resp.status_code == 200
        return_parameter = json.loads(resp.text)
        print(resp.text)
        if return_parameter['status'] == 'ok':
            challenge = return_parameter["challenge"]
            validate = return_parameter["validate"]
            return self.return_qichacha(challenge, validate)
        elif return_parameter['status'] == 'no':
            return self.approved(gt, challenge)
        elif return_parameter['status'] == 'stop':
            raise VerificationCodeError('请求打码接口参数异常。')

    def return_qichacha(self, challenge, validate):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
        resp = requests.get('https://www.qichacha.com/user_login', headers=header, verify=False)
        cookies = resp.cookies.get_dict()
        header = """
           Accept: application/json, text/javascript, */*; q=0.01
           Accept-Encoding: gzip, deflate, br
           Accept-Language: zh-CN
           Cache-Control: no-cache
           Connection: Keep-Alive
           Content-Length: 245
           Content-Type: application/x-www-form-urlencoded; charset=UTF-8
           Host: www.qichacha.com
           Origin: https://www.qichacha.com
           Referer: https://www.qichacha.com/user_login
           User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134
           X-Requested-With: XMLHttpRequest
        """
        headers = format_headers(header)
        data = 'phone_prefix=%2B86&nameNormal={}&pwdNormal={}&geetest_challenge={}&geetest_validate={}&geetest_seccode={}%7Cjordan&verify_type=2'.format(
            self.name, self.pwd, challenge, validate, validate)
        resp = self.session.post('https://www.qichacha.com/user_loginaction', data=data, verify=False, headers=headers,
                                 cookies=cookies)
        print(resp)
        print(resp.text)
        assert resp.status_code == 200
        if json.loads(resp.text)['success']:
            cookies = resp.cookies.get_dict()
            dict_tmp = {'website': 'qichacha', 'cookies': cookies, 'insert_time': int(time.time())}
            self.col.insert(dict_tmp)
            print(resp.text)
            print(resp.cookies.get_dict())
        else:
            raise QichachaVerificationError('通过企查查验证失败')


if __name__ == '__main__':
    auto_cookies = AutomaticAcquisitionCookies()
    auto_cookies.get_verify()
