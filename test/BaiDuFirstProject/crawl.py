# -*- coding:utf-8 -*-
# @Time    : 2018/7/26 17:28
# @Author  : Brady
# @File    : crawl.py
# @Software: PyCharm
# @Contact : bradychen1024@gmail.com

import re
import queue
import inspect
import traceback
import configparser
from pprint import pprint
from datetime import datetime
from random import choice
from threading import Thread
from time import sleep, strftime, time
from concurrent.futures import ThreadPoolExecutor

import pymongo
import selenium
from bs4 import BeautifulSoup
from pymongo.errors import ServerSelectionTimeoutError, AutoReconnect
from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

# from extend.downloader import Downloader
from extend.task_distribution import TaskDistribution
from extend.toolkit import SpiderLog, Timer, retry_wrapper, timeout, get_datetime_now, format_headers
from extend.toolkit import TimeoutException, MongoDbClient, filter_all_char, replace_all, client, dbClient

"""
不完全匹配搜索，但拆词后的搜索词出现在搜索结果的标题时，停止翻页并返回结果
拆词策略:
1.如果"工程"或"项目"都出现，取第一次出现位置到前面的所有词进行搜索
2.当出现"工程"或"项目"，取第一次出现位置到前面的所有词进行搜索
3.如果都没出现关键字，则不拆词
"""


class Crawl(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('extend/config.ini')
        self.config.sections()
        self.debug = self.config['setting']['debug']
        self.debug = True if self.debug == 'True' else False

        self.session = HTMLSession()
        # self.download = Downloader()

        # self.keywords = list(
        #     set([k if k else '民间借贷' for k in keyword.replace('\n', '\t').replace(' ', '').split('\t')]))
        # self.keywords = ['开工']
        self.log = SpiderLog()

        self.snapshot_queue = queue.Queue()
        self.results_queue = queue.Queue()

        self.filter_url = self.config['setting']['filter_url'].split('|||')  # 过滤域名
        self.filter_title = self.config['setting']['filter_title'].split('|||')  # 过滤标题名称

        self.task_amount = 0  # 种子队列总量
        self.task_count = 0  # 用来统计队列消耗量

        self.insert_date = ''
        self.project_name = ''

    @staticmethod
    def split_keywords(_project_name: str) -> (str, tuple):
        """
        拆词策略:
        1.如果"工程"或"项目"都出现，取第一次出现位置到前面的所有词进行搜索
        2.当出现"工程"或"项目"，取第一次出现位置到前面的所有词进行搜索
        3.如果都没出现关键字，则不拆词
        :param _project_name:
        :return:
        """
        keyword_engineering = '工程'
        keyword_project = '项目'
        _project_name = replace_all(['(', ')', '（', '）'], _project_name)

        keyword1_match = _project_name.count(keyword_engineering)
        keyword2_match = _project_name.count(keyword_project)
        keyword1_index = _project_name.find(keyword_engineering) + 2 if _project_name.find(
            keyword_engineering) != -1 else 0
        keyword2_index = _project_name.find(keyword_project) + 2 if _project_name.find(keyword_project) != -1 else 0

        if keyword1_match and keyword2_match:
            first_keyword_index = max([keyword1_index, keyword2_index])
            return _project_name[0:first_keyword_index]
        elif keyword1_match:
            return _project_name[0:keyword1_index]
        elif keyword2_match:
            return _project_name[0:keyword2_index]
        else:
            return _project_name

    def get_project_on_mongodb(self):
        """
        从mongodb获取公司名
        :return:
        """
        _mongo = dbClient['task_seed_new']
        while True:
            try:
                result = _mongo.find_one({'$or': [
                    {'spider.baidu_first_project': 0},
                    {'spider.baidu_first_project': {"$exists": False}},

                ]})
                if result is not None:
                    # _project_name = result['seed']['project_message']
                    # _company_name = result['seed']['proposer']

                    self.update_company_status(result, 0)

                    # 如果项目采集没有项目名，说明不是项目采集
                    # if not _project_name:
                    #     _mongo.update({'status': 1, 'company_name': _company_name,
                    #                   'crawl_target': 'baidu_first_project'},
                    #                  {'$set': {'status': 2,
                    #                            'process_time': get_datetime_now()}})
                    #     self.update_company_status(_company_name, 1, 2)
                    return result
                else:
                    print('百度项目2等待新的任务种子中...,休息10秒')
                    sleep(10)
            except Exception as e:
                traceback.print_exc()
                print('出现未知异常,休眠一分钟重试')
                sleep(60)

    def update_company_status(self, result, new_status, errMsg=None):
        # project_name = result['seed']['project_message']
        _mongo = dbClient['task_seed_new']
        result['spider']['baidu_first_project'] = new_status * 1.0
        if errMsg is not None:
            result['errMsg']['baidu_first_project'] = errMsg
        _mongo.save(result)

        # if not self.debug:
        #     mongo = dbClient['task_seed']
        #     try:
        #         result = mongo.update(
        #             {'status': old_status, 'project_name': project_name, 'crawl_target': 'baidu_first_project'},
        #             {'$set': {'status': new_status, 'process_time': get_datetime_now()}})
        #         pass
        #     except AutoReconnect:
        #         sleep(5)
        #         result = mongo.update(
        #             {'status': old_status, 'project_name': project_name, 'crawl_target': 'baidu_first_project'},
        #             {'$set': {'status': new_status, 'process_time': get_datetime_now()}})

    def parse_search_result(self, _project_name):
        if not _project_name:
            return None

        _project_name = self.split_keywords(_project_name)
        headers = format_headers("""
                   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
                   Accept-Encoding: gzip, deflate, br
                   Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
                   Cache-Control: max-age=0
                   Connection: keep-alive
                   Host: www.baidu.com
                   User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36
                   """)
        proxy_url = 'http://121.9.245.183/daili2.txt'
        resp = self.session.get(proxy_url)
        proxy = choice(resp.html.html.split('\r\n'))
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }

        for pn in range(0, 90 + 10, 10):
            url = f'https://www.baidu.com/s?q1={_project_name}&pn={pn}'
            try:
                resp = self.session.get(url, headers=headers, proxies=proxies, timeout=10)
            except Exception:
                proxy_url = 'http://121.9.245.183/daili2.txt'
                resp = self.session.get(proxy_url)

                proxy = choice(resp.html.html.split('\r\n'))

                proxies = {
                    "http": f"http://{proxy}",
                    "https": f"http://{proxy}",
                }
                print('请求超时')

            while True:
                if '百度信誉V标识及信誉档案中的任何内容' in resp.html.html:
                    print('进入百度企业验证页面，休眠1秒...')
                    sleep(1)
                else:
                    break

            if '很抱歉，没有找到' not in resp.html.html:
                all_title = resp.html.find('div#content_left div.result h3 a')
                snapshot_list = resp.html.find("""div#content_left div.result a[data-click="{'rsv_snapshot':'1'}"]""")
                for title, snapshot in zip(all_title, snapshot_list):
                    snapshot_url = snapshot.attrs.get('href')
                    if _project_name in replace_all(['(', ')', '（', '）'], title.text):
                        print('采集到的标题:', title.text)
                        return {'title': title.text, 'snapshot_url': snapshot_url}
            else:
                return None
        else:
            print('没有匹配到数据:', _project_name)
            return None

    def run(self):
        result = self.get_project_on_mongodb()
        try:

            mongo = dbClient['baidu_first_project']
            _project_name = result['seed']['project_message']
            print("种子项目名: " + _project_name)
            crawl_result = self.parse_search_result(_project_name)

            if self.debug:
                return
            if not crawl_result:
                print("未找到匹配的项目")
                self.update_company_status(result, 1, "未找到匹配的项目")
            else:
                crawl_result.update({'insert_date': self.insert_date, 'project_name': _project_name})
                mongo.insert(crawl_result)
                self.update_company_status(result, 1)
        except:
            self.update_company_status(result, -1, traceback.format_exc())


def send_signal():
    def send():
        sleep(0.9)
        return '6.baidu_first_project'

    t = TaskDistribution('172.18.158.144', 8180, 'brady'.encode('utf-8'), send)
    t.start()


if __name__ == '__main__':
    # threads_func = Thread(target=send_signal)
    # threads_func.setDaemon(True)
    # threads_func.start()
    # sleep(5)

    # 测试监控与激活功能
    # while True:
    #     print('百度舆情在采集中')
    #     sleep(1)

    # c = Crawl()
    # c.run('于都县2018年高标准农田建设项目（19-29标段）19标')
    # exit()

    # 多线程
    c = Crawl()
    import time

    while True:
        try:
            c.run()
            time.sleep(1)
        except:
            traceback.print_exc()
    # # c.run('采购玉米')
    # # exit()
    # result = c.get_project_on_mongodb()
    # c.update_company_status(result, 0)
    # project_name = result['seed']['project_message']
    # print('正在采集此项目:', result)
    # c.insert_date = get_datetime_now()
    # c.run(result)
    # print('完成项目：', project_name)
    # try:
    #     c.update_company_status(result, 1)
    # except ServerSelectionTimeoutError:
    #     c.update_company_status(result, -1)

    # """
    # 单次快照链接测试
    # c = Crawl()
    # arg = (('http://cache.baiducontent.com/c?m=9d78d513d9d430a44f9de2697c61c0121c4381132ba6a3020cd78449e3732d435015e0ac56200775a3d20c6016d94c4beb802104371454c18cb8f85dacbf85295f9f573f676f805662d20edeba5124b137e65bfede1bf0ca8725e2afc5d2af4323c144767197808c4d7711dd6e80034097b1ef3c022e10ad9d3572fe296058ec3433bd5089eb251d0195b19d0243996c96230696dc28ad7f58ee04a468537402f05bb17f007b6ff74f50ae182055c1b008ba6d644325b44db2bcc7a1eb3fd69ab56f&p=c06ccc04969d12a05abd9b7c4b&newp=9370c64ad48703fa08e296251553d8254207dc357b9687787dc0c513fe200c01063dbee728261407d3c47f6602ad4856e8fb3d70310726b48f8ee50b8af99d7f73de637625&user=baidu&fm=sc&query=%22%C9%BD%CE%F7%CA%A1%D0%A1%C0%CB%B5%D7%D2%FD%BB%C6%B9%A4%B3%CC%D3%C0%BE%C3%B9%A9%B5%E7%CF%DF%C2%B7%CA%A9%B9%A4%22&qid=e144e00500022648&p1=1', '某公司'))
    # c.parse_snapshot(arg)
