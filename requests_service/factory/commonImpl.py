import requests

from logging_utils.log import mylog
from requests_service.downloadImp import DownloadImp


class CommonImpl(DownloadImp):
    def download(self, mission):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
        url = mission['url']
        res = requests.get(url, headers=headers, timeout=5, verify=False)
        assert res.status_code == 200
        html = res.text
        self.hash_.update(url.encode('utf-8'))
        urlmd5 = self.hash_.hexdigest()
        self.r_return.set(urlmd5, html)
        print(urlmd5)
        print("回调任务成功")

    def mid(self):
        return 0

    def state(self):
        super().state()