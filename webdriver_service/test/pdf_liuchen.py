import requests
import json

url = "http://192.168.10.49:8891/BatchPdfCode"
data = {
    "pdfs": [{"regno": "04094405000491249700", "pdfname": "04094405000491249700_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_a6864be826b83dff8e2bb6edd555e4e3.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fc3d94b8410fbaa01b3"},
             {"regno": "04596352000550220797", "pdfname": "04596352000550220797_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_6145d6da2f123df9ac1aa13f9ce08d4b.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fc4d94b8410fbaa01b4"},
             {"regno": "04821362000576254173", "pdfname": "04821362000576254173_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_359ac31221c9a60a95be165d5dcc071d.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fc6d94b8410fbaa01b5"},
             {"regno": "04999690000596844297", "pdfname": "04999690000596844297_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_e62fba9599913a5d930057222548fd18.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fc7d94b8410fbaa01b6"},
             {"regno": "05078971000606061685", "pdfname": "05078971000606061685_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_9338fab0d6f2ffd462a4156dc7ba2b8a.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fc9d94b8410fbaa01b7"},
             {"regno": "05200075000620392412", "pdfname": "05200075000620392412_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_07057792fac3e84bb276bef39fda93c2.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fcad94b8410fbaa01b8"},
             {"regno": "05279527000629566636", "pdfname": "05279527000629566636_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_11a57d75992f140ecb4b6f71a75ee9d5.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fcbd94b8410fbaa01b9"},
             {"regno": "05279674000629585124", "pdfname": "05279674000629585124_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_0294e96e6e4ead373ad6f8ba52ed91d2.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fcdd94b8410fbaa01ba"},
             {"regno": "05279674000629917073", "pdfname": "05279674000629917073_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_e29188c30910024c7e02c7567fa1a887.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fced94b8410fbaa01bb"},
             {"regno": "05279674000629966797", "pdfname": "05279674000629966797_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_426ee4f671c96173b7695048be361a5c.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fd0d94b8410fbaa01bc"},
             {"regno": "05279674000636614985", "pdfname": "05279674000636614985_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_1f71b5bff5388e90b90a46b8b170f135.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fd1d94b8410fbaa01bd"},
             {"regno": "05279674000640147161", "pdfname": "05279674000640147161_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_c1c2217fe1829a52b20789ddd70f18a9.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fd2d94b8410fbaa01be"},
             {"regno": "05355495000638304897", "pdfname": "05355495000638304897_A.pdf", "companypdfname": "沈阳北方建设股份有限公司",
              "ossPath": "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190227/_35c57e51dc73813eafe6570d6b4fb478.pdf",
              "insertTime": "2019-02-27", "_id": "5c762fd4d94b8410fbaa01bf"}],
    "billNums": ["01287153", "01238774"],
}
data = json.dumps(data)
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=data, headers=headers)
print(response.text)
