import requests

from logging_utils.log import mylog


def file_test(url, fileName):
    ua = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    headers = {'User-Agent': ua}
    response = requests.get(url=url, verify=False, headers=headers)
    mylog.info(response.status_code)
    with open(fileName, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    url = 'http://www.sothebys.com/content/dam/stb/lots/N09/N09953/N09953-227_web.jpg'
    file_test(url, 'test.jpg')
