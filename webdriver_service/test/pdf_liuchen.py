import requests
import json
url = "http://192.168.10.49:8891/BatchPdfCode"
data = {
    "pdfs":[
        {"pdfName":"03297837000397536524_A.pdf","ossPath":"http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190124/_b1290a74337e0ee66b8f4dafeca76bcb.pdf"},
        {"pdfName":"03668300000441007012_A.pdf","ossPath":"http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190124/_dc30239d71c6ace9e4613045721bd603.pdf"},
        {"pdfName":"03668300000441007012_A.pdf","ossPath":"http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190124/_dc30239d71c6ace9e4613045721bd603.pdf"}
    ],
    "billNums":["391048","04391052","46127896341"],
}
data = json.dumps(data)
headers = {"Content-Type": "application/json"}
response = requests.post(url,data=data,headers=headers)
print(response.text)