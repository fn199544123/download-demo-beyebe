import traceback
import redis
import requests

from logging_utils.log import mylog
from requests_service.Custom_exception import LoginError
from requests_service.downloadImp import DownloadImp


class QichachaMainImpl(DownloadImp):
    def download(self, mission):
        cookies = self.col.find().sort('_id', -1)[0]['cookies']
        url = mission['url']
        res = requests.get(url, cookies=cookies, headers=self.headers, timeout=5, verify=False)
        assert res.status_code == 200
        html = res.text
        if '玄鸟' in html:
            self.hash_.update(url.encode('utf-8'))
            urlmd5 = self.hash_.hexdigest()
            self.r_return.set(urlmd5, html)
            print(urlmd5)
            print("回调任务成功")
        else:
            traceback.print_exc()
            raise LoginError('未能成功登入账户。')

    def mid(self):
        return 1

    def state(self):
        super().state()
