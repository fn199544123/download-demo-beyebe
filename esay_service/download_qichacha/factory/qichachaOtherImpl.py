import redis
import requests

from downloadImp import DownloadImp
from Custom_exception import LoginError

class QichachaOtherImpl(DownloadImp):
    def download(self, mission):
        cookies = self.col.find().sort('_id', -1)[0]['cookies']
        url = mission['url']
        res = requests.get(url, cookies=cookies, headers=self.headers, timeout=5, verify=False)
        if res.status_code == 405:
            raise LoginError('未能成功登入账户。')
        assert res.status_code == 200
        html = res.text
        self.r_return.set(url, html)
        print(url)
        print("回调任务成功")

    def mid(self):
        return 2

    def state(self):
        super().state()
