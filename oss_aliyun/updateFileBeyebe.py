# -*- coding: utf-8 -*-
import datetime
import hashlib
import os
import uuid

import oss2
import pymongo
import requests

# 从内网Mongo获取账号密码
import sys

from logging_utils.log import mylog

MONGODB_HOST = '192.168.10.9'
MONGODB_USER = 'fangnan'
MONGODB_PASSWORD = 'Fang135'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'hedgehog_spider'

client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
db = client[MONGODB_DBNAME]
db.authenticate(MONGODB_USER, MONGODB_PASSWORD)
item = db['aliyun_oss'].find_one({'name': 'beyebe'})

access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', item['access_key_id'])
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', item['access_key_secret'])
bucket_name = os.getenv('OSS_TEST_BUCKET', item['bucket_name'])
endpoint = os.getenv('OSS_TEST_ENDPOINT', item['endpoint'])

URL_BASE = 'http://{bucketName}.oss-cn-shenzhen.aliyuncs.com/'.replace('{bucketName}', bucket_name)
# 确认上面的参数都填写正确了
for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    assert '<' not in param, '请设置参数：' + param

# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)


def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()


def uploadToOss(type, data, fileName, path="beyebe/data/{yyyymmdd}/"):
    global bucket, URL_BASE
    if path is None:
        path = "beyebe/data/{yyyymmdd}/"
    if path[-1] != '/':
        path += '/'
    path = path.replace('{yyyymmdd}', datetime.datetime.now().strftime('%Y%m%d'))
    name = getMd5(data)
    if fileName is None:
        url = path + "_" + name + '.' + type
    else:
        url = path + fileName + "_" + name + '.' + type
    print('正在上传')
    print('name', name)
    print('url', url)

    bucket.put_object(url, data, progress_callback=percentage)
    return URL_BASE + url


def getMd5(file):
    m0 = hashlib.md5()
    m0.update(file)
    return m0.hexdigest()


def fileUpdate(file_dir, isFileName=False, path=None):
    # 图片上传
    f = open(file_dir, 'rb')
    file = f.read()
    f.close()

    if isFileName:
        fileName = file_dir.split('/')[-1].split('.')[0]
        msg = uploadToOss(file_dir.split('.')[-1], file, fileName, path=path)
    else:
        msg = uploadToOss(file_dir.split('.')[-1], file, None, path=path)

    return msg


def mkdirUpdate(file_mkdir_dir, isFileName=False, path=None):
    msgList = []
    for root, dirs, files in os.walk(file_mkdir_dir):
        for fileName in files:
            print("文件路径", file_mkdir_dir + '/' + fileName)
            msgList.append(fileUpdate(file_mkdir_dir + '/' + fileName, isFileName=isFileName, path=path))
    return msgList


if __name__ == '__main__':
    # 单文件上传
    print(fileUpdate('/Users/magic/Library/Mobile Documents/com~apple~CloudDocs/Desktop/docker镜像/fapiao_http_new.tar', path='beyebe/docker', isFileName=True))
    # print(fileUpdate('./test.txt'))
    # 文件夹上传,如果isFileName=True,那么地址会保留文件名,并且不会被文件系统去重逻辑去重
    # print(mkdirUpdate('./banner', isFileName=True))
