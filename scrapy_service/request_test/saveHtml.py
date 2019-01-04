import requests


def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()


def html_test(url, htmlName):
    ua = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    headers = {'User-Agent': ua}
    session = requests.session()
    session.get(url, headers=headers)
    html = session.get(url, headers=headers).text
    save_to_file(htmlName, html)


if __name__ == '__main__':
    url = 'https://www.baidu.com/s?q2=中花岗消防站项目施工'
    html_test(url, 'test.html')
