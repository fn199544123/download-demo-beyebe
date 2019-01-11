"""
这段代码通过浏览器复制可以得到所有请求的headers.
包括但不限于 cookie ua等
By xincheng
使用方法：
打开chrome访问网页，使用调试器进行调试，进入网页点击headers，拉到requestHeaders整体复制
"""
from logging_utils.log import mylog

headersStr = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: QCCSESSID=0a63ehii2t32nhbedgb7pdrqb4; UM_distinctid=167edac442a404-099880917fb379-10326653-1fa400-167edac442b187; zg_did=%7B%22did%22%3A%20%22167edac44ee627-0abc800cd7c28b-10326653-1fa400-167edac44efff4%22%7D; _uab_collina=154588074943244773305084; saveFpTip=true; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1545880750; acw_tc=0ed7179d15458807513665473e19d2c368eaa832cc0e13221897b36be3; CNZZDATA1254842228=851495438-1545875840-%7C1545967646; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1545968446; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201545966953755%2C%22updated%22%3A%201545968446152%2C%22info%22%3A%201545880749304%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22153b25f8e0a1e282a5afdae73d2c817d%22%7D
Host: www.qichacha.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
"""
"""解析请求头"""


def format_headers(string):
    """
    将在Chrome上复制下来的浏览器UA格式化成字典，以\n为切割点
    :param string: 使用三引号的字符串
    :return:
    """
    string = string.strip().replace(' ', '').split('\n')
    dict_ua = {}
    for key_value in string:
        dict_ua.update({key_value.split(':')[0]: key_value.split(':')[1]})
    return dict_ua


if __name__ == '__main__':
    # Test 自动进行模拟请求
    import requests

    headers = format_headers(headersStr)
    rep = requests.get("https://www.qichacha.com/firm_182249d7736fdb68960201022c19647a.html#report", headers=headers)
    html = rep.text
    mylog.info(rep.url)
    with open("web_msg/headerTest.html", "w", encoding='utf-8') as fp:
        fp.write(html)
