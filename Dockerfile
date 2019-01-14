#基于的基础镜像
FROM python:3.6
FROM python:3.6
#代码添加到code文件夹

ADD . /scrapy-demo-beyebe
# 设置code文件夹是工作目录
WORKDIR /scrapy-demo-beyebe
# 安装支持
RUN yum install chrome
RUN pip install -r requirements.txt
CMD ["cd","/scrapy-demo-beyebe"]
CMD ["python3", "/scrapy-demo-beyebe/webdriver_service/start/fapiaoHttpStart.py"]