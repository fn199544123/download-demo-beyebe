FROM centos
WORKDIR /root
RUN curl -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
RUN  echo '[google-chrome]' > /etc/yum.repos.d/google-chrome.repo
RUN  echo 'name=google-chrome' >> /etc/yum.repos.d/google-chrome.repo
RUN  echo 'baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch' >> /etc/yum.repos.d/google-chrome.repo
RUN  echo 'enabled=1' >> /etc/yum.repos.d/google-chrome.repo
RUN  echo 'gpgcheck=1' >> /etc/yum.repos.d/google-chrome.repo
RUN  echo 'gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub' >> /etc/yum.repos.d/google-chrome.repo

RUN yum install -y python36
RUN yum -y install google-chrome-stable --nogpgcheck
RUN yum install -y epel-release

