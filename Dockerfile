# 基于的基础镜像
FROM python:3.6.4

# 安装Python支持包支持
ADD . /root/scrapy-demo-beyebe
RUN python36 -m pip install --upgrade pip
RUN python36 -m pip install -r /root/scrapy-demo-beyebe/requirements.txt


CMD ["cd","/root/scrapy-demo-beyebe"]
CMD ["python36", "/root/scrapy-demo-beyebe/webdriver_service/start/fapiaoHttpStart.py"]