import requests

from downloadImp import DownloadImp


class CommonImpl(DownloadImp):
    def download(self, mission):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
        url = mission['url']
        res = requests.get(url, headers=headers, timeout=5, verify=False)
        assert res.status_code == 200
        html = res.text
        self.r_return.set(url, html)
        print(url)
        print("回调任务成功")

    def mid(self):
        return 0

    def state(self):
        super().state()