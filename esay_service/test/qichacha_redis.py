import re
import os
import requests
from bs4 import BeautifulSoup
import pymongo
import time
import redis
import datetime

class QiChaChaRedis():
    def __init__(self):
        client = pymongo.MongoClient('mongodb://fangnan:Fang135@192.168.10.9:27017/?authSource=hedgehog_spider')
        mydb = client['hedgehog_spider']
        self.mycol = mydb['ds_qichacha_sitemap']
        self.rpool = redis.ConnectionPool(host="192.168.10.9", port=6379, password='123456', decode_responses=True, db=14)

    def get_data(self):
        resp = requests.get('https://www.qichacha.com/sitemap.xml')
        soup = BeautifulSoup(resp.text, 'lxml')
        for _ in soup.find_all('url'):
            if 'https://www' in _.text:
                loc = _.find('loc').text
                priority = _.find('priority').text
                lastmod = _.find('lastmod').text
                changefreq = _.find('changefreq').text
                cid = re.search('firm_(.*?)\.', _.find('loc').text).group(1)
                _dict = {'loc': loc, 'priority': priority, 'lastmod': lastmod, 'changefreq': changefreq,
                         'cid': cid, 'time': datetime.datetime.now()}
                try:
                    self.mycol.insert_one(_dict)
                    r = redis.Redis(connection_pool=self.rpool)
                    print(r.lpush('qichacha_sitemap', _dict.get('loc')))

                except:
                    continue

while True:
    try:
        QiChaChaRedis().get_data()
        time.sleep(3600)
    except:
        while True:
            if os.system('ping 223.5.5.5') is True:
                break
            else:
                time.sleep(60)
