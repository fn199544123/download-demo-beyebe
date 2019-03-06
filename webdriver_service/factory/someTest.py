#!/usr/bin/python3
import re

line = "href=\"javascript:filedownload('00','05617033000668301597') are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.search(r'href=\"javascript:filedownload\(\'(.*)\',\'(.*?)\'\)', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")