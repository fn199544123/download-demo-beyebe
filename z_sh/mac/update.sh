#!/usr/bin/expect
send "<----------------->\r"
send "send mkdir\r"
send "<----------------->\r"
#环境检查
#服务器环境
set IPAddress 39.108.188.34
set password qq190.com
#相关设置
set timeout -1
#本地环境
set scpFilePath /Users/magic/PycharmProjects/scrapy-demo-beyebe
set servicePath /root/scrapy-demo-beyebe
set password Szlocal!!!
#scp -r /Users/magic/PycharmProjects/zywa-spider-xiaociwei root@172.10.3.103:/root/xiaociwei_download
#Jar包传输
#spawn scp -r $scpFilePath root@$IPAddress:$servicePath
#expect "root@$IPAddress's password:"
#send "$password\r"
#expect "forever"

spawn rsync -av --delete --exclude .git --exclude venv $scpFilePath root@$IPAddress:$servicePath
expect "root@$IPAddress's password:"
send "$password\r"
expect "speedup is"
