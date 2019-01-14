import pipenv
import re
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pprint import pprint
import requests
import json

clint = MongoClient(host='192.168.10.9:27017')
db = clint['hedgehog_spider']
db.authenticate(name='fangnan',password='Fang135')
col = db['ds_qichacha']
data = col.find({},{'_id': 1, 'data': 1, 'url': 1})

myclint = MongoClient(host='localhost:27017')
mydb = myclint['qichacha']
mycol = mydb['test']


def parse(html,url):
    address, introduction, website, email, phone = None, None, None, None, None
    postData = {
        'html': html,
        'sid': 'qichacha_xy',
    }
    response = requests.post('http://121.9.245.173:8001/middleware/htmlparse.go', data=postData)
    response = json.loads(response.text)
    try:
        name = response.get('class_s').get('title')[0].get('text').replace('\n', '').replace('曾用名', '').strip()
        name = re.split(' +',name)
        name, status = [_ for _ in name]
        head = response.get('id_s').get('company-top')[0].get('text').replace('\n','').strip()
        head = re.split(' +',head)
        phone = response.get('class_s').get('fc')[1].get('text')
        print(phone)
        exit()
        # print(head)
        for num,_head in enumerate(head):
            if _head == '地址：':
                address = head[num+1]
            if _head == '简介：':
                introduction = head[num+1]
            if _head == '官网：':
                website = head[num+1]
            if _head == '邮箱：':
                email = head[num+1]
            if _head == '电话：':
                phone = head[num+1]
        nianbao = response.get('class_s').get('company-nav-head')
        for _nianbao in nianbao:
            if '企业年报' in _nianbao.get('text'):
                nianbao ='https://www.qichacha.com/' + _nianbao.get('href')
        print(status)
        # exit()
    except TypeError:
        print(url)

def qichacha_save(i):
    postData = {
        'html': html,
        'sid': 'qichacha_xy',
    }
    response = requests.post('http://e1651.gicp.net:13144/middleware/htmlparse.go', data=postData)
    with open('qichacha{}'.format(i), 'w') as w:
        w.write(response.text)
    response = json.loads(response.text)

i = 0
for _ in data:
    _id = _.get('_id')
    html = _.get('data')
    url = _.get('url')
    createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # qichacha_save(i)
    # i+=1
    parse(html, url)    #调用函数
    exit()


