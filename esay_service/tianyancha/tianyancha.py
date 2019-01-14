# -*- coding: UTF-8 -*-
import pipenv
import re
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pprint import pprint
import requests
import json
from threading import Thread

clint = MongoClient(host='192.168.10.9:27017')
db = clint['hedgehog_spider']
db.authenticate(name='fangnan',password='Fang135')


myclint = MongoClient(host='localhost:27017')
mydb = myclint['qichacha']
mycol = mydb['test']

class JieXi():
    def __init__(self):
        self.url = 'http://192.168.10.101:8001/middleware/htmlparse.go'
        self.html = """
<!DOCTYPE html><html><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1"><title>小米科技有限责任公司_工商信息_信用报告_财务报表_电话地址查询-天眼查</title><meta http-equiv="pragma" content="no-cache"><meta http-equiv="cache-control" content="no-cache"><meta http-equiv="expires" content="0"><meta name="format-detection" content="telephone=no"><meta http-equiv="cache-control" content="no-transform"/><meta http-equiv="cache-control" content="no-siteapp"/><meta name="MobileOptimized" content="width"/><meta name="HandheldFriendly" content="true"/><meta name="description" itemprop="description" content="天眼查为您提供小米科技有限责任公司工商信息查询、注册信息查询、企业信用报告、财务报表查询、电话地址查询、招聘信息等企业信息查询服务,了解小米科技有限责任公司股东法人、经营状况、商业关系等详细信息,就到天眼查官网！"><meta name="keywords" content="小米科技有限责任公司工商信息查询,小米科技有限责任公司信用报告查询,小米科技有限责任公司财务报表查询"><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
        charset="UTF-8"><!-- applicable-device begin --><meta name="applicable-device" content="mobile"><link rel="canonical" href="https://www.tianyancha.com/company/23402373"><!-- applicable-device end --><!--qq config--><meta itemprop="name" content="小米科技有限责任公司_工商信息_信用报告_财务报表_电话地址查询-天眼查"><meta itemprop="image" content="https://static.tianyancha.com/wap/images/18blue/weixinlogo.png"><meta name="fragment" content="!"/><meta name="tyc-wx-type" content="company"/><meta name="tyc-wx-name" content="小米科技有限责任公司"/><meta name="tyc-device" content="mobile"/><!--baidu config--><script src="//msite.baidu.com/sdk/c.js?appid=1559462363285617"></script><base href="/"><script>
    String.prototype.trim = function () {
      return this.replace(/(^\s*)|(\s*$)/g, "");
    };
    window.serverDomain = 'https://m.tianyancha.com';
    window.antirobotServer = 'https://antirobot.tianyancha.com';
    window.serverSuffix = '.tianyancha.com';
    window.appServerDomain = 'https://app.tianyancha.com';
    window.cookieServerSuffix = '.tianyancha.com';
    window.disServerDomain = 'https://dis.tianyancha.com';
  </script><base href="/"><script src="//static.tianyancha.com/js-cdn/oss/4.15.1/aliyun-oss-sdk.min.js"></script><link rel="stylesheet" href="https://static.tianyancha.com/fonts-styles/css/14/14dfa282/font.css"><script type="text/javascript" src="https://static.tianyancha.com/m-require-js/public/js/require-0b59cae482.config.js"></script><script data-main="route/company"
          src="https://static.tianyancha.com/wap-require-js/public/js/lib/require.js"></script><link rel="stylesheet" href="https://static.tianyancha.com/wap/css/bootstrap.css"><!-- build:css(./) resources/styles/app.css --><!-- inject:css --><link rel="stylesheet" href="https://static.tianyancha.com/m-require-js/public/styles/main-e43b8a1e39.css"><!-- endinject --><!-- endbuild --><style type="text/css">
    [ng\:cloak], [ng-cloak], [data-ng-cloak], [x-ng-cloak], .ng-cloak, .x-ng-cloak, .ng-hide {
      display: none !important;
    }

    ng\:form {
      display: block;
    }

    .ng-animate-start {
      clip: rect(0, auto, auto, 0);
      -ms-zoom: 1.0001;
    }

    .ng-animate-active {
      clip: rect(-1px, auto, auto, 0);
      -ms-zoom: 1;
    }
  </style>


  <script>
    (function () {
      var method;
      var noop = function () {
      };
      var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'
      ];
      var length = methods.length;
      var console = (window.console = window.console || {});

      while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
          console[method] = noop;
        }
      }
      CacheStoarge = function CacheStoarge() {
        var _bb = [];
        return {
          _tt: function (bbV, bbE, bbX) {
            bbX ? _bb.push(bbX) : _bb[bbV].push(bbE);
          },
          _ff: function (ii) {
            //console.log(_bb);
            return _bb[ii];
          }
        };
      };
      DOMImplementaiton = CacheStoarge();
    }());

  </script></head><body class="font-14dfa282"><div id="banner_mobile"></div><div><div class='wapHeader' style=""><div class=" search_recontain row over-hide ml10 mr10 pl0 pr0"><a href="https://m.tianyancha.com" class="float-left vertival-middle mt5" style="width: 27%;"><img style="width: 96px;max-height: 30px;"
           src="https://static.tianyancha.com/wap-require-js/themes/18blue/images/index_logo_web2.png" alt=""></a><div class="input-group search_group float-right vertival-middle" style="width: 68%;"><form onsubmit="return header.mobileStopSubmit(event);" autocomplete="off"><input type="search" id="live-search"
               class="search_input form-control search_form new-c1 input pl5 f14"
               style="border-bottom-left-radius: 2px; border-top-left-radius: 2px" search-type="company"
               value=""
               placeholder="请输入公司、人名、商标" required></form><img alt="" onclick="header.clearKey(event,'#live-search');"
           src="https://static.tianyancha.com/wap/images/close.png" class="clear"
           width="20px" alt=""/><div class="input-group-addon" onclick="header.mobileSearch(event);"><i class="tic tic-lg tic-search"></i></div></div></div></div></div><div><div class="company-mobile-container416"><div class="updateInfoError hide"><div class="close" onclick="closeUpdateError()"><i class="tic tic-close"></i></div><div class="pttw">我们将持续追踪该企业，并及时自动完成信息更新</div></div><!--头部信息--><div id="wap_header_top"><div class="page-header417"><div class="over-hide"><div class="f18 new-c3 float-left" style="width: 59%;">小米科技有限责任公司</div><div class="float-right text-right hi-hide" style="width: 41%;"><div class="app-intro" onclick="mobileReport(23402373);" ng-hide="zjhClient">免费获取信用报告</div></div></div><div class="c9 pt15 f14"><span class="mr18"><i class="tic tic-star-o"></i><span class="new-c1">评分</span>98</span><a class=" change1018 hi-hide"
           href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&param2=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&channelCode=WAP26"><span
            class="mr9 near_company_btn">附近公司</span></a><a class=" change1018 hi-hide"
           href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&param2=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&channelCode=WAP26"><span
            class="go_to_app_btn">前往APP查看</span></a></div></div><div class="page-header-subContent over-hide company-mobile-subcontent" style="height:40px"><div class="pt10 pb10 hi-hide"><span class="icon-phone417"></span><a class=" change1018 hi-hide"
           href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&param2=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&channelCode=WAP27"><span class="title-right417" style="width: auto">60606666-<img style="    height: 20px;
                display: inline-block;
                margin-top: -4px;
                margin-left: -1px;" src="https://static.tianyancha.com/wap-require-js/themes/18blue/images/Slice3.png"></span><span class="go_to_app_btn hi-hide hi-hide">前往APP查看</span></a><span class="float-right new-c2" onclick="baseInfoTogal(this)">联系信息<i
            class="tic mr2 f14 tic-angle-down"></i></span></div><div class="new-border-top pt10 pb10"><span class="icon-email417 "></span><span class="title-right417">****@xiaomi.com</span></div><div class="new-border-top pt10 pb10"><span class="icon-cp417"></span><a class="title-right417 overflow-width"
           target="_blank" rel="nofollow"
           href="http://www.xiaomi.com"
        >www.xiaomi.com</a></div><div class="new-border-top pt10 pb10"><span class="icon-dt417"></span><span class="title-right417">北京市海淀区清河中街68号华润五彩城购物中心二期13层</span></div></div><a class="change1018" href="https://m.tianyancha.com/risk/riskInfo/23402373"><div class="page-header-subContent mobile-risk-content clearfix hi-hide"><table class="float-left mt15"><tbody><tr><td rowspan="2"><div class="mobile-risk-logo"></div></td><td><span class="mobile-risk-count-content">自身风险：<span
                  class="risk-count">2691条</span></span></td></tr><tr><td><span class="mobile-risk-count-content">周边风险：<span
                  class="risk-count">26条</span></span></td></tr></tbody></table><div class="float-right mobile-risk-info-content pt9 text-center"><div class="mobile-risk-btn pt3 pb3 pl6 pr6">查看风险</div></div></div></a></div><!--end头部信息--><!--人员提前--><div id="personner_wapper" class="mobile-bottom-cut"><div class="personner-container"><div class="holder-container"><div class="holder-title"><span>股东</span></div><div class="holder-box-container"><div class="position-rel"><div id="holder-width" class='f0' style="width:472px;"><a
              href="/human/2263357360-c23402373"
              class="holder-box mr4"><div class="line1"><div class="portrait c-white text-center f16"
                     style="background-color:#5dcff3;"><span class='holder-letter'>雷</span></div><div class="personner-name pl4"><div class="overflow-width mb2 pl2">雷军</div><span class='f10 big-holder pl2 pr2 ' style="">大股东</span></div></div><div class="line2 sec-c3"><div>持股比例<span style="color:#fb5253;">77.80%</span></div><div class="mt2">共有141家公司</div></div></a><a
              href="/human/2303132325-c23402373"
              class="holder-box mr4"><div class="line1"><div class="portrait c-white text-center f16"
                     style=""><img style="vertical-align: top;width:30px;height:30px;" src="https://img.tianyancha.com/logo/human2/8921b6d29f5d04ada17434ef0bc7e6e3.png@!z_200x200  "
                       onerror="this.src='https://static.tianyancha.com/wap-require-js/themes/18blue/images/person-img-error.png'"/></div><div class="personner-name pl4"><div class="pl2 more-overflow2">黎万强</div></div></div><div class="line2 sec-c3"><div>持股比例<span style="color:#fb5253;">10.12%</span></div><div class="mt2">共有118家公司</div></div></a><a
              href="/human/2048698570-c23402373"
              class="holder-box mr4"><div class="line1"><div class="portrait c-white text-center f16"
                     style=""><img style="vertical-align: top;width:30px;height:30px;" src="https://img.tianyancha.com/logo/human/2/ef7e265d932df414897d685bfca8ba4c.png@!z_200x200  "
                       onerror="this.src='https://static.tianyancha.com/wap-require-js/themes/18blue/images/person-img-error.png'"/></div><div class="personner-name pl4"><div class="pl2 more-overflow2">洪锋</div></div></div><div class="line2 sec-c3"><div>持股比例<span style="color:#fb5253;">10.07%</span></div><div class="mt2">共有40家公司</div></div></a><a
              href="/human/1811254503-c23402373"
              class="holder-box mr4"><div class="line1"><div class="portrait c-white text-center f16"
                     style=""><img style="vertical-align: top;width:30px;height:30px;" src="https://img.tianyancha.com/logo/human/2/78439a0b3684579c27fc595cc92d0d5f.png@!z_200x200  "
                       onerror="this.src='https://static.tianyancha.com/wap-require-js/themes/18blue/images/person-img-error.png'"/></div><div class="personner-name pl4"><div class="pl2 more-overflow2">刘德</div></div></div><div class="line2 sec-c3"><div>持股比例<span style="color:#fb5253;">2.01%</span></div><div class="mt2">共有68家公司</div></div></a></div></div></div></div><div class="staff-container mt4"><div class="staff-title"><span>董监高</span></div><div class="staff-box-container"><div class="position-rel"><div id="staff-width" class='f0' style="width:590px;"><a
              href="/human/2344180375-c23402373"
              class="staff-box mr4"><div class="line1"><div class="portrait text-center f16"
                     style="color:white;"><img style="vertical-align: top;width:30px;height:30px;" src="https://img.tianyancha.com/logo/human/2/35ce589dde92c51dcc810e254e44713f.png@!z_200x200  "
                       onerror="this.src='https://static.tianyancha.com/wap-require-js/themes/18blue/images/person-img-error.png'"/></div><div class="personner-name pl4"><div class="overflow-width pl2" style=" ">林斌</div><div class="overflow-width f12 mt2 c-s-gray pl2" style="">董事</div></div></div><div class="line2 sec-c3"><div class="mt8">共有13家公司</div></div></a><a
              href="/human/2263357360-c23402373"
              class="staff-box mr4"><div class="line1"><div class="portrait text-center f16"
                     style="background-color:#c69781;color:white;"><span class="holder-letter">雷</span></div><div class="personner-name pl4"><div class="overflow-width pl2" style=" ">雷军</div><div class="overflow-width f12 mt2 c-s-gray pl2" style="">董事长，经理</div></div></div><div class="line2 sec-c3"><div class="mt8">共有141家公司</div></div></a><a
              href="/human/1816392796-c23402373"
              class="staff-box mr4"><div class="line1"><div class="portrait text-center f16"
                     style="color:white;"><img style="vertical-align: top;width:30px;height:30px;" src="https://img.tianyancha.com/logo/human/2/866fb5987ccdc194312c77e059a33e1f.png@!z_200x200  "
                       onerror="this.src='https://static.tianyancha.com/wap-require-js/themes/18blue/images/person-img-error.png'"/></div><div class="personner-name pl4"><div class="overflow-width pl2" style=" ">刘芹</div><div class="overflow-width f12 mt2 c-s-gray pl2" style="">董事</div></div></div><div class="line2 sec-c3"><div class="mt8">共有62家公司</div></div></a><a
              href="/human/2303132325-c23402373"
              class="staff-box mr4"><div class="line1"><div class="portrait text-center f16"
                     style="color:white;"><img style="vertical-align: top;width:30px;height:30px;" src="https://img.tianyancha.com/logo/human2/8921b6d29f5d04ada17434ef0bc7e6e3.png@!z_200x200  "
                       onerror="this.src='https://static.tianyancha.com/wap-require-js/themes/18blue/images/person-img-error.png'"/></div><div class="personner-name pl4"><div class="overflow-width pl2" style=" ">黎万强</div><div class="overflow-width f12 mt2 c-s-gray pl2" style="">监事</div></div></div><div class="line2 sec-c3"><div class="mt8">共有118家公司</div></div></a><a
              href="/human/2172832730-c23402373"
              class="staff-box mr4"><div class="line1"><div class="portrait text-center f16"
                     style="background-color:#5dcff3;color:white;"><span class="holder-letter">许</span></div><div class="personner-name pl4"><div class="overflow-width pl2" style=" ">许达来</div><div class="overflow-width f12 mt2 c-s-gray pl2" style="">董事</div></div></div><div class="line2 sec-c3"><div class="mt8">共有19家公司</div></div></a></div></div></div></div></div></div><!--人员提前End--><div class="mobile-bottom-cut pl8 pr8 pt8 clearfix hi-hide" id="tagInfo_wapper"><a class="common-preview" href="https://m.tianyancha.com/brand/bc800159002"><span class="preview-title"><span>品牌</span></span><span class="preview-container overflow-width"><span class="preview-tag pr20">MIJIA米家</span><span>融资轮次:<span
              class="preview-red pr20">—</span></span><span>融资:<span
              class="preview-red pr20">6</span></span><span>竞品:<span
              class="preview-red ">50</span></span></span><span class="previe-angle "><i class="tic tic-angle-right"></i></span></a><a class="common-preview"
       href="https://m.tianyancha.com/organize/b48be2888"><span class="preview-title"><span>机构</span></span><span class="preview-container overflow-width"><span class="preview-tag pr20">小米科技</span><span>管理基金:<span
              class="preview-red pr20">17</span></span><span>投资事件:<span
              class="preview-red ">221</span></span></span><span class="previe-angle"><i class="tic tic-angle-right"></i></span></a></div><div class='new-border-bottom' style="height: 40px;"><div class=" b-c-white mobile-nav-directive"
     style="z-index: 1030; overflow: hidden; padding-bottom: 0; opacity: .96; padding-top: 0px; padding-left: 0px; padding-right: 0px;"><div class="position-rel" style="left: 0px;"><div class="nav-directive" style=" height:40px; width:2664px;font-size: 0px;"><span id="btn_nav-main-baseInfo"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-baseInfo')"

      >基本信息</span><span id="btn_nav-main-graphInfo"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-graphInfo')"

      >企业关系</span><span id="btn_nav-main-equityStructure"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-equityStructure')"

      >股权结构</span><span id="btn_nav-main-staffCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-staffCount')"

      >主要人员</span><span id="btn_nav-main-holderCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-holderCount')"

      >股东信息</span><span id="btn_nav-main-inverstCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-inverstCount')"

      >对外投资</span><span id="btn_nav-main-changeCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-changeCount')"

      >变更记录</span><span id="btn_nav-main-reportCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-reportCount')"

      >企业年报</span><span id="btn_nav-main-branchCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-branchCount')"

      >分支机构</span><span id="btn_nav-main-lawsuitCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-lawsuitCount')"

      >法律诉讼</span><span id="btn_nav-main-courtCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-courtCount')"

      >法院公告</span><span id="btn_nav-main-dishonest"
            class="mulit-nav-items-mobile c6"

      >失信人信息</span><span id="btn_nav-main-zhixing"
            class="mulit-nav-items-mobile c6"
            onclick="goToPage('nav-main-zhixing')"

      >被执行人</span><span id="btn_nav-main-abnormalCount"
            class="mulit-nav-items-mobile c6"
            onclick="goToPage('nav-main-abnormalCount')"

      >经营异常</span><span id="btn_nav-main-punishment"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-punishment')"

      >行政处罚</span><span id="btn_nav-main-illegalCount"
            class="mulit-nav-items-mobile c6"
            onclick="goToPage('nav-main-illegalCount')"

      >严重违法</span><span id="btn_nav-main-equityCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-equityCount')"

      >股权出质</span><span id="btn_nav-main-mortgageCount"
            class="mulit-nav-items-mobile c6"
            onclick="goToPage('nav-main-mortgageCount')"

      >动产抵押</span><span id="btn_nav-main-ownTaxCount"
            class="mulit-nav-items-mobile c6"
            onclick="goToPage('nav-main-ownTaxCount')"

      >欠税公告</span><span id="btn_nav-main-companyRongzi"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-companyRongzi')"

      >融资历史</span><span id="btn_nav-main-companyTeammember"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-companyTeammember')"

      >核心团队</span><span id="btn_nav-main-companyProduct"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-companyProduct')"

      >企业业务</span><span id="btn_nav-main-jigouTzanli"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-jigouTzanli')"

      >投资事件</span><span id="btn_nav-main-companyJingpin"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-companyJingpin')"

      >竞品信息</span><span id="btn_nav-main-recruitCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-recruitCount')"

      >招聘信息</span><span id="btn_nav-main-taxCreditCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-taxCreditCount')"

      >税务评级</span><span id="btn_nav-main-checkCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-checkCount')"

      >抽查检查</span><span id="btn_nav-main-bidCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-bidCount')"

      >招投标</span><span id="btn_nav-main-productinfo"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-productinfo')"

      >产品信息</span><span id="btn_nav-main-bondCount"
            class="mulit-nav-items-mobile c6"
            onclick="goToPage('nav-main-bondCount')"

      >债券信息</span><span id="btn_nav-main-goudiCount"
            class="mulit-nav-items-mobile c6"
            onclick="goToPage('nav-main-goudiCount')"

      >购地信息</span><span id="btn_nav-main-tmCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-tmCount')"

      >商标信息</span><span id="btn_nav-main-patentCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-patentCount')"

      >专利信息</span><span id="btn_nav-main-cpoyRCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-cpoyRCount')"

      >著作权</span><span id="btn_nav-main-icpCount"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-icpCount')"

      >网站备案</span><span id="btn_nav-main-past"
            class="mulit-nav-items-mobile "
            onclick="goToPage('nav-main-past')"

      >历史信息</span></div></div></div></div><!-- 1基本信息 --><div class="header-container"><div id="nav-main-baseInfo" class="itemTitle">基本信息</div></div><div><!--entityType  ==1   公司 ，2香港，3社会组织，4律所 5事业单位 6基金会--><div class="content-container pb10"><div class="item-line"><span class="left-text">法定代表人：</span><span class="overflow-width" style="max-width: 200px;    vertical-align: middle;"
    ><a
        title="雷军"
        href="/human/2263357360-c23402373"
        class=" f18 "
      >雷军</a></span><a class="app-intro"
       href="/human/2263357360-c23402373"
    >他有141家企业</a></div><div class="item-line"><span
      class="left-text">经营状态：</span><span>在业</span></div><div class="item-line"><span
      class="left-text">注册时间：</span><span><text class="tyc-num" >6383-32-32</text></span></div><div class="item-line"><span
      class="left-text">注册资本：</span><span><text class="tyc-num" >817333万比土币</text></span></div><div class="item-line"><span class="left-text">行业：</span><span>科技推广和应用服务业</span></div><div class="item-line"><span
      class="left-text">企业类型：</span><span>有限责任公司(自然人投资或控股)</span></div><div class="item-line"><span
      class="left-text">工商注册号：</span><span>110108012660422</span></div><div class="item-line"><span
      class="left-text">组织结构代码：</span><span>551385082</span></div><div class="item-line"><span
      class="left-text">统一信用代码：</span><span>91110108551385082Q</span></div><div class="item-line"><span
      class="left-text">纳税人识别号：</span><span>91110108551385082Q</span></div><div class="item-line"><span class="left-text">经营期限：</span><span>2010-03-03至2030-03-02</span></div><div class="item-line"><span
      class="left-text">核准日期：</span><span><text class="tyc-num" >6381-35-63</text></span></div><div class="item-line"><span
      class="left-text">登记机关：</span><span>海淀分局</span></div><div class="item-line"><span
      class="left-text">注册地址：</span><span>北京市海淀区清河中街68号华润五彩城购物中心二期13层</span></div><div class="item-line" style="line-height: 30px;"><span class="left-text">经营范围：</span><span style="word-break: break-all;" content-folder content="company.businessScope" num="60"><span ng-init="showDetail = false;" class="js-shrink-container"><span ng-if="!showDetail" ng-bind-html="perContent|splitNum"
        class="js-full-container hidden"><html><head></head><body><div><text class="tyc-num">&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x8D27;&#x7269;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x6280;&#x672F;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x4EE3;&#x7406;&#x5E03;&#x51FA;&#x53E3;&#xFF1B;&#x9500;&#x552E;&#x5E74;&#x8BAF;&#x8BBE;&#x6765;&#x3001;&#x53A8;&#x623F;&#x7528;&#x53EA;&#x3001;&#x536B;&#x793A;&#x7528;&#x53EA;&#xFF08;&#x542B;&#x661F;&#x6BD4;&#x62A4;&#x7406;&#x7528;&#x53EA;&#xFF09;&#x3001;&#x65E5;&#x7528;&#x6742;&#x8D27;&#x3001;&#x5316;&#x5986;&#x53EA;&#x3001;&#x53CA;&#x7597;&#x5668;&#x68B0;I&#x77F3;&#x3001;II&#x77F3;&#x3001;&#x907F;&#x5B55;&#x5668;&#x65AD;&#x3001;&#x73A9;&#x65AD;&#x3001;&#x6025;&#x80B2;&#x7528;&#x53EA;&#x3001;&#x6587;&#x5316;&#x7528;&#x53EA;&#x3001;&#x670D;&#x5C06;&#x978B;&#x5E3D;&#x3001;&#x949F;&#x4E89;&#x773C;&#x955C;&#x3001;&#x9488;&#x7EBA;&#x7EC7;&#x53EA;&#x3001;&#x81F4;&#x7528;&#x7535;&#x5668;&#x3001;&#x81F4;&#x65AD;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#x3001;&#x8BC1;&#x3001;&#x8349;&#x5916;&#x89C2;&#x8D4F;&#x690D;&#x7269;&#x3001;&#x4E0D;&#x518D;&#x5206;&#x5C06;&#x7684;&#x5305;&#x5C06;&#x8BE5;&#x5B50;&#x3001;&#x7FA4;&#x76F8;&#x5668;&#x6750;&#x3001;&#x4E09;&#x827A;&#x53EA;&#x3001;&#x53F2;&#x53EA;&#x3001;&#x6837;&#x5168;&#x673A;&#x3001;&#x8F6F;&#x4EF6;&#x5916;&#x8F85;&#x52A9;&#x8BBE;&#x6765;&#x3001;&#x73E0;&#x542C;&#x5404;&#x9970;&#x3001;&#x54CD;&#x7528;&#x867D;&#x4EA7;&#x53EA;&#x3001;&#x5BA0;&#x7269;&#x54CD;&#x53EA;&#x3001;&#x7535;&#x5B50;&#x4EA7;&#x53EA;&#x3001;&#x6469;&#x6258;&#x8F66;&#x3001;&#x7535;&#x8D44;&#x8F66;&#x3001;&#x81EA;&#x884C;&#x8F66;&#x5916;&#x96F6;&#x90E8;&#x4EF6;&#x3001;&#x667A;&#x52A8;&#x5361;&#x3001;&#x4E94;&#x91D1;&#x4EA4;&#x7535;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#x3001;&#x5EFA;&#x7B51;&#x6750;&#x653F;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#xFF1B;&#x6562;&#x4FEE;&#x4EEA;&#x5668;&#x4EEA;&#x4E89;&#xFF1B;&#x6562;&#x4FEE;&#x627E;&#x5F8B;&#x8BBE;&#x6765;&#xFF1B;&#x627F;&#x627E;&#x6309;&#x89C8;&#x6309;&#x5E72;&#x7C7B;&#x8D44;&#xFF1B;&#x751F;&#x544A;&#x670D;&#x52A1;&#xFF1B;&#x7B79;&#x6765;&#x3001;&#x7B56;&#x5212;&#x3001;&#x7EC4;&#x7EC7;&#x5927;&#x578B;&#x5E86;&#x5178;&#xFF1B;&#x8BBE;&#x6837;&#x3001;&#x5236;&#x7ECF;&#x3001;&#x4EE3;&#x7406;&#x3001;&#x5374;&#x89C4;&#x5E7F;&#x529B;&#xFF1B;&#x6444;&#x5F71;&#x6269;&#x5370;&#x670D;&#x52A1;&#xFF1B;&#x6587;&#x827A;&#x6F14;&#x51FA;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x6025;&#x80B2;&#x8D5B;&#x4E8B;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x6309;&#x89C8;&#x751F;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x535A;&#x89C8;&#x751F;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#xFF1B;&#x6BCD;&#x673A;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x6BCD;&#x673A;&#x793A;&#x4EA7;&#x3001;&#x6BCD;&#x673A;&#x670D;&#x52A1;&#xFF08;&#x9650;&#x5C81;&#x6DC0;&#x533A;&#x6C38;&#x6377;&#x5317;&#x4F1A;6&#x5148;&#x5357;&#x5C42;&#x786E;&#x8D39;&#xFF09;&#xFF1B;&#x547D;&#x4E8B;&#x4E92;&#x5979;&#x7F51;&#x6587;&#x5316;&#x7C7B;&#x8D44;&#xFF1B;&#x51FA;&#x7248;&#x7269;&#x96F6;&#x552E;&#xFF1B;&#x51FA;&#x7248;&#x7269;&#x6279;&#x5374;&#xFF1B;&#x9500;&#x552E;&#x7B2C;&#x4F5C;&#x77F3;&#x53CA;&#x7597;&#x5668;&#x68B0;&#xFF1B;&#x9500;&#x552E;&#x54CD;&#x53EA;&#xFF1B;&#x96F6;&#x552E;&#x836F;&#x53EA;&#xFF1B;&#x5E7F;&#x64AD;&#x7535;&#x89C6;&#x6B64;&#x76EE;&#x5236;&#x7ECF;&#x3002;&#xFF08;&#x4F01;&#x4E1A;&#x8BF7;&#x6CD5;&#x81EA;&#x53F8;&#x9009;&#x62E9;&#x786E;&#x8D39;&#x9879;&#x76EE;&#xFF0C;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;&#x547D;&#x4E8B;&#x4E92;&#x5979;&#x7F51;&#x6587;&#x5316;&#x7C7B;&#x8D44;&#x3001;&#x51FA;&#x7248;&#x7269;&#x6279;&#x5374;&#x3001;&#x51FA;&#x7248;&#x7269;&#x96F6;&#x552E;&#x3001;&#x9500;&#x552E;&#x54CD;&#x53EA;&#x3001;&#x5E7F;&#x64AD;&#x7535;&#x89C6;&#x6B64;&#x76EE;&#x5236;&#x7ECF;&#x3001;&#x96F6;&#x552E;&#x836F;&#x53EA;&#x3001;&#x9500;&#x552E;&#x7B2C;&#x4F5C;&#x77F3;&#x53CA;&#x7597;&#x5668;&#x68B0;&#x4EE5;&#x5916;&#x8BF7;&#x6CD5;&#x4E2A;&#x786E;&#x6279;&#x51C6;&#x7684;&#x9879;&#x76EE;&#xFF0C;&#x786E;&#x76F8;&#x6B66;&#x90E8;&#x95E8;&#x6279;&#x51C6;&#x98DF;&#x8BF7;&#x6279;&#x51C6;&#x7684;&#x5185;&#x5BB9;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;&#x4E0D;&#x5BDF;&#x547D;&#x4E8B;&#x672C;&#x597D;&#x4EA7;&#x4E1A;&#x5427;&#x7B56;&#x7981;&#x4F3C;&#x548C;&#x9650;&#x5236;&#x77F3;&#x9879;&#x76EE;&#x7684;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#x3002;&#xFF09;</text></div></body></html></span><span ng-if="showDetail" ng-bind-html="content|splitNum"
        class="js-split-container "><html><head></head><body><div><text class="tyc-num">&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x8D27;&#x7269;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x6280;&#x672F;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x4EE3;&#x7406;&#x5E03;&#x51FA;&#x53E3;&#xFF1B;&#x9500;&#x552E;&#x5E74;&#x8BAF;&#x8BBE;&#x6765;&#x3001;&#x53A8;&#x623F;&#x7528;&#x53EA;&#x3001;&#x536B;&#x793A;...</text></div></body></html></span><a ng-show="needFolder" ng-click="showDetail = btnOnClick(showDetail)" style="cursor: pointer;"
     class="" onclick="folder.toggle(this)">详细</a></span></span></div></div></div><div class="hi-hide"><div id="nav-main-graphInfo" class="header-container"><div class="itemTitle">企业关系</div></div><a class=" change1018"
       href="https://m.tianyancha.com/graphMobile?id=23402373&name=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8"><img style="width:100%;" src="http://static.tianyancha.com/web-require-js/public/images/graph_mobile_img.png"></a></div><div class="hi-hide"><div id="nav-main-equityStructure" class="header-container"><div class="itemTitle">股权结构</div></div><a class="change1018"
       href="https://m.tianyancha.com/equityMobile?id=23402373&name=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8"><img style="width:100%;" src="http://static.tianyancha.com/web-require-js/public/images/equity_mobile_img.png"></a></div><!-- end基本信息 --><!--理事会--><!--理事会end--><!--监事会--><!--监事会end--><!-- graph --><!-- endgraph --><!--2主要人员--><div><div id="nav-main-staffCount" class="header-container"><div class="itemTitle">主要人员</div></div><div class="over-hide" id="_container_staff"><div class=""><div class="content-container"><div class="pt10 pb10 new-border-bottom"><a
        href="/human/2344180375-c23402373"
        class="in-block vertival-middle overflow-width">林斌</a><a ng-hide="zjhClient" class="app-intro"
         href="/human/2344180375-c23402373"
      >他有13家公司</a><span class="float-right"><span>董事</span></span></div><div class="pt10 pb10 new-border-bottom"><a
        href="/human/2263357360-c23402373"
        class="in-block vertival-middle overflow-width">雷军</a><a ng-hide="zjhClient" class="app-intro"
         href="/human/2263357360-c23402373"
      >他有141家公司</a><span class="float-right"><span>董事长，</span><span>经理</span></span></div><div class="pt10 pb10 new-border-bottom"><a
        href="/human/1816392796-c23402373"
        class="in-block vertival-middle overflow-width">刘芹</a><a ng-hide="zjhClient" class="app-intro"
         href="/human/1816392796-c23402373"
      >他有62家公司</a><span class="float-right"><span>董事</span></span></div><div class="pt10 pb10 new-border-bottom"><a
        href="/human/2303132325-c23402373"
        class="in-block vertival-middle overflow-width">黎万强</a><a ng-hide="zjhClient" class="app-intro"
         href="/human/2303132325-c23402373"
      >他有118家公司</a><span class="float-right"><span>监事</span></span></div><div class="pt10 pb10 "><a
        href="/human/2172832730-c23402373"
        class="in-block vertival-middle overflow-width">许达来</a><a ng-hide="zjhClient" class="app-intro"
         href="/human/2172832730-c23402373"
      >他有19家公司</a><span class="float-right"><span>董事</span></span></div></div></div></div></div><!--end主要人员--><!--3股东信息--><div><div id="nav-main-holderCount" class="header-container"><div class="itemTitle in-block vertival-middle">股东信息</div><span class="app-intro float-right vertival-middle hi-hide" onclick="mobileReport(23402373);"
            style="margin-top: -3px;">实缴出资和出资比例</span></div><div class="" id="_container_holder"><div class=""><div class="content-container"><div class="pb15 pt15 new-border-bottom"><div><a
          href="/human/2263357360-c23402373"
          class="in-block vertival-middle overflow-width">雷军</a><a class="app-intro"
           href="/human/2263357360-c23402373"
        >他有141家公司</a></div><div class="mt10"><span class="left-text">认缴出资：</span><span><span>143934.0478万元</span></span></div><div class="mt10 hi-hide"><span class="left-text">出资比例：</span><span class="new-info "><a
            href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&param2=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&channelCode=WAP23"
            class="f13 " tyc-event-click tyc-event-ch="company.wap.detail.holder"><img
              src="https://static.tianyancha.com/wap-require-js/public/images/company-value-mask-new.png" width="64px"
              alt="">下载APP查看</a></span></div></div><div class="pb15 pt15 new-border-bottom"><div><a
          href="/human/2303132325-c23402373"
          class="in-block vertival-middle overflow-width">黎万强</a><a class="app-intro"
           href="/human/2303132325-c23402373"
        >他有118家公司</a></div><div class="mt10"><span class="left-text">认缴出资：</span><span><span>18724.3569万元</span></span></div><div class="mt10 hi-hide"><span class="left-text">出资比例：</span><span class="new-info "><a
            href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&param2=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&channelCode=WAP23"
            class="f13 " tyc-event-click tyc-event-ch="company.wap.detail.holder"><img
              src="https://static.tianyancha.com/wap-require-js/public/images/company-value-mask-new.png" width="64px"
              alt="">下载APP查看</a></span></div></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">2个</span>股东信息</a></div></div></div></div><!--end股东信息--><!--4对外投资--><div><div id="nav-main-inverstCount" class="header-container"><div class="itemTitle in-block vertival-middle">对外投资</div><span class="app-intro float-right vertival-middle hi-hide" ng-hide="zjhClient"
            onclick="mobileReport(23402373);"
            style="margin-top: -3px;">实缴出资和出资比例</span></div><div id="_container_invest"><div class=""><div class="content-container"><div class="pt15 pb15 new-border-bottom"><a href="/company/3077374563"
         style="word-break: break-all;"
         class="block"><span class="text-click-color">重庆小米商业保理有限公司</span></a><div class="item-line"><span
          class="left-text">法定代表人：</span><span>洪锋</span><a class="app-intro"
           href="/human/2048698570-c3077374563"
        >他有36家公司</a></div><div class="item-line"><span
          class="left-text">注册资本：</span><span>10000万人民币</span></div><div class="item-line"><span
          class="left-text">投资数额：</span><span>10000万元人民币</span></div><div class="item-line hi-hide"><span class="left-text">投资比例：</span><a
          href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&param2=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&channelCode=WAP24"
          class="f13" tyc-event-click tyc-event-ch="company.wap.detail.invest"><img src="https://static.tianyancha.com/wap-require-js/public/images/company-value-mask-new.png" width="64px"
               alt="">下载APP查看</a></div></div><div class="pt15 pb15 new-border-bottom"><a href="/company/2352467007"
         style="word-break: break-all;"
         class="block"><span class="text-click-color">西藏小米科技有限责任公司</span></a><div class="item-line"><span
          class="left-text">法定代表人：</span><span>雷军</span><a class="app-intro"
           href="/human/2263357360-c2352467007"
        >他有142家公司</a></div><div class="item-line"><span
          class="left-text">注册资本：</span><span>100万人民币</span></div><div class="item-line"><span
          class="left-text">投资数额：</span><span>100万元人民币</span></div><div class="item-line hi-hide"><span class="left-text">投资比例：</span><a
          href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&param2=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&channelCode=WAP24"
          class="f13" tyc-event-click tyc-event-ch="company.wap.detail.invest"><img src="https://static.tianyancha.com/wap-require-js/public/images/company-value-mask-new.png" width="64px"
               alt="">下载APP查看</a></div></div></div><!--<div class="company_mobile_pager new-border-top pt15 pb15 ml15 mr15" ng-if="ceil(investList.total/20)>1">--><!--<uib-pagination previous-text="<" next-text=">" items-per-page="20" ng-change="getInverstInfo(inverstInfoCurrentPage,20);" total-items="investList.total" ng-model="inverstInfoCurrentPage" max-size="5" class="pagination-sm" boundary-links="false" rotate="false" style="float:left"></uib-pagination>--><!--<div class="total"><span>共</span>{{ceil(investList.total/20);}}<span>页</span></div>--><!--</div>--><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">12个</span>对外投资</a></div></div></div></div><!--end对外投资--><!--5变更信息--><div><div class="header-container"><div id="nav-main-changeCount" class="itemTitle">变更信息</div></div><div id="_container_changeinfo"><div class="limit-2-download hi-show"><div class="content-container"><div class="pt15 pb15 new-border-bottom"><div><div
          ng-bind-html="($index+1+(mobileChangeIndex*5))>9?($index+1+(mobileChangeIndex*5)):'0'+($index+1+(mobileChangeIndex*5))"          class="f14 new-border c9 p3 in-block vertical-top mr10">01</div><div class="in-block vertical-top"><div class="mb8"><span class="left-text">时间：</span><span>2018-05-09</span></div><div><span class="left-text">项目：</span><span>经营范围</span></div></div></div><div class="over-hide mt10"><div class="left-content float-left new-border" style="width: 49%;"><div class="changeSubTitle">变更前</div><div class="changeSubText"><span ng-init="showDetail = false;" class="js-shrink-container"><span ng-if="!showDetail" ng-bind-html="perContent|splitNum"
        class="js-full-container hidden"><html><head></head><body><div><text class="tyc-num">&#x6BCD;&#x673A;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x6BCD;&#x673A;&#x793A;&#x4EA7;&#x3001;&#x6BCD;&#x673A;&#x670D;&#x52A1;&#xFF08;&#x9650;&#x5C81;&#x6DC0;&#x533A;&#x6C38;&#x6377;&#x5317;&#x4F1A;6&#x5148;&#x5357;&#x5C42;&#x786E;&#x8D39;&#xFF09;&#xFF1B;&#x547D;&#x4E8B;&#x4E92;&#x5979;&#x7F51;&#x6587;&#x5316;&#x7C7B;&#x8D44;&#xFF1B;&#x51FA;&#x7248;&#x7269;&#x96F6;&#x552E;&#xFF1B;&#x51FA;&#x7248;&#x7269;&#x6279;&#x5374;&#xFF1B;&#x9500;&#x552E;&#x7B2C;&#x4F5C;&#x77F3;&#x53CA;&#x7597;&#x5668;&#x68B0;&#xFF1B;&#x9500;&#x552E;&#x54CD;&#x53EA;&#xFF1B;&#x96F6;&#x552E;&#x836F;&#x53EA;&#x3002;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x8D27;&#x7269;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x6280;&#x672F;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x4EE3;&#x7406;&#x5E03;&#x51FA;&#x53E3;&#xFF1B;&#x9500;&#x552E;&#x5E74;&#x8BAF;&#x8BBE;&#x6765;&#x3001;&#x53A8;&#x623F;&#x7528;&#x53EA;&#x3001;&#x536B;&#x793A;&#x7528;&#x53EA;&#xFF08;&#x542B;&#x661F;&#x6BD4;&#x62A4;&#x7406;&#x7528;&#x53EA;&#xFF09;&#x3001;&#x65E5;&#x7528;&#x6742;&#x8D27;&#x3001;&#x5316;&#x5986;&#x53EA;&#x3001;&#x53CA;&#x7597;&#x5668;&#x68B0;I&#x77F3;&#x3001;II&#x77F3;&#x3001;&#x907F;&#x5B55;&#x5668;&#x65AD;&#x3001;&#x73A9;&#x65AD;&#x3001;&#x6025;&#x80B2;&#x7528;&#x53EA;&#x3001;&#x6587;&#x5316;&#x7528;&#x53EA;&#x3001;&#x670D;&#x5C06;&#x978B;&#x5E3D;&#x3001;&#x949F;&#x4E89;&#x773C;&#x955C;&#x3001;&#x9488;&#x7EBA;&#x7EC7;&#x53EA;&#x3001;&#x81F4;&#x7528;&#x7535;&#x5668;&#x3001;&#x81F4;&#x65AD;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#x3001;&#x8BC1;&#x3001;&#x8349;&#x5916;&#x89C2;&#x8D4F;&#x690D;&#x7269;&#x3001;&#x4E0D;&#x518D;&#x5206;&#x5C06;&#x7684;&#x5305;&#x5C06;&#x8BE5;&#x5B50;&#x3001;&#x7FA4;&#x76F8;&#x5668;&#x6750;&#x3001;&#x4E09;&#x827A;&#x53EA;&#x3001;&#x53F2;&#x53EA;&#x3001;&#x6837;&#x5168;&#x673A;&#x3001;&#x8F6F;&#x4EF6;&#x5916;&#x8F85;&#x52A9;&#x8BBE;&#x6765;&#x3001;&#x73E0;&#x542C;&#x5404;&#x9970;&#x3001;&#x54CD;&#x7528;&#x867D;&#x4EA7;&#x53EA;&#x3001;&#x5BA0;&#x7269;&#x54CD;&#x53EA;&#x3001;&#x7535;&#x5B50;&#x4EA7;&#x53EA;&#x3001;&#x6469;&#x6258;&#x8F66;&#x3001;&#x7535;&#x8D44;&#x8F66;&#x3001;&#x81EA;&#x884C;&#x8F66;&#x5916;&#x96F6;&#x90E8;&#x4EF6;&#x3001;&#x667A;&#x52A8;&#x5361;&#x3001;&#x4E94;&#x91D1;&#x4EA4;&#x7535;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#x3001;&#x5EFA;&#x7B51;&#x6750;&#x653F;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#xFF1B;&#x6562;&#x4FEE;&#x4EEA;&#x5668;&#x4EEA;&#x4E89;&#xFF1B;&#x6562;&#x4FEE;&#x627E;&#x5F8B;&#x8BBE;&#x6765;&#xFF1B;&#x627F;&#x627E;&#x6309;&#x89C8;&#x6309;&#x5E72;&#x7C7B;&#x8D44;&#xFF1B;&#x751F;&#x544A;&#x670D;&#x52A1;&#xFF1B;&#x7B79;&#x6765;&#x3001;&#x7B56;&#x5212;&#x3001;&#x7EC4;&#x7EC7;&#x5927;&#x578B;&#x5E86;&#x5178;&#xFF1B;&#x8BBE;&#x6837;&#x3001;&#x5236;&#x7ECF;&#x3001;&#x4EE3;&#x7406;&#x3001;&#x5374;&#x89C4;&#x5E7F;&#x529B;&#xFF1B;&#x6444;&#x5F71;&#x6269;&#x5370;&#x670D;&#x52A1;&#xFF1B;&#x6587;&#x827A;&#x6F14;&#x51FA;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x6025;&#x80B2;&#x8D5B;&#x4E8B;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x6309;&#x89C8;&#x751F;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x535A;&#x89C8;&#x751F;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3002;&#x4F01;&#x4E1A;&#x8BF7;&#x6CD5;&#x81EA;&#x53F8;&#x9009;&#x62E9;&#x786E;&#x8D39;&#x9879;&#x76EE;&#xFF0C;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;&#x547D;&#x4E8B;&#x4E92;&#x5979;&#x7F51;&#x6587;&#x5316;&#x7C7B;&#x8D44;&#x3001;&#x51FA;&#x7248;&#x7269;&#x6279;&#x5374;&#x3001;&#x51FA;&#x7248;&#x7269;&#x96F6;&#x552E;&#x3001;&#x9500;&#x552E;&#x54CD;&#x53EA;&#x3001;&#x96F6;&#x552E;&#x836F;&#x53EA;&#x3001;&#x9500;&#x552E;&#x7B2C;&#x4F5C;&#x77F3;&#x53CA;&#x7597;&#x5668;&#x68B0;&#x4EE5;&#x5916;&#x8BF7;&#x6CD5;&#x4E2A;&#x786E;&#x6279;&#x51C6;&#x7684;&#x9879;&#x76EE;&#xFF0C;&#x786E;&#x76F8;&#x6B66;&#x90E8;&#x95E8;&#x6279;&#x51C6;&#x98DF;&#x8BF7;&#x6279;&#x51C6;&#x7684;&#x5185;&#x5BB9;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;&#x4E0D;&#x5BDF;&#x547D;&#x4E8B;&#x672C;&#x597D;&#x4EA7;&#x4E1A;&#x5427;&#x7B56;&#x7981;&#x4F3C;&#x548C;&#x9650;&#x5236;&#x77F3;&#x9879;&#x76EE;&#x7684;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#x3002;</text></div></body></html></span><span ng-if="showDetail" ng-bind-html="content|splitNum"
        class="js-split-container "><html><head></head><body><div><text class="tyc-num">&#x6BCD;&#x673A;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x6BCD;&#x673A;&#x793A;&#x4EA7;&#x3001;&#x6BCD;&#x673A;&#x670D;&#x52A1;&#xFF08;&#x9650;&#x5C81;&#x6DC0;&#x533A;&#x6C38;&#x6377;&#x5317;&#x4F1A;6&#x5148;&#x5357;&#x5C42;&#x786E;&#x8D39;&#xFF09;&#xFF1B;&#x547D;...</text></div></body></html></span><a ng-show="needFolder" ng-click="showDetail = btnOnClick(showDetail)" style="cursor: pointer;"
     class="" onclick="folder.toggle(this)">详细</a></span></div></div><div class="right-content float-right new-border" style="width: 49%;"><div class="changeSubTitle">变更后</div><div class="changeSubText"><span ng-init="showDetail = false;" class="js-shrink-container"><span ng-if="!showDetail" ng-bind-html="perContent|splitNum"
        class="js-full-container hidden"><html><head></head><body><div><text class="tyc-num">&#x6BCD;&#x673A;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x6BCD;&#x673A;&#x793A;&#x4EA7;&#x3001;&#x6BCD;&#x673A;&#x670D;&#x52A1;&#xFF08;&#x9650;&#x5C81;&#x6DC0;&#x533A;&#x6C38;&#x6377;&#x5317;&#x4F1A;6&#x5148;&#x5357;&#x5C42;&#x786E;&#x8D39;&#xFF09;&#xFF1B;&#x547D;&#x4E8B;&#x4E92;&#x5979;&#x7F51;&#x6587;&#x5316;&#x7C7B;&#x8D44;&#xFF1B;&#x51FA;&#x7248;&#x7269;&#x96F6;&#x552E;&#xFF1B;&#x51FA;&#x7248;&#x7269;&#x6279;&#x5374;&#xFF1B;&#x9500;&#x552E;&#x7B2C;&#x4F5C;&#x77F3;&#x53CA;&#x7597;&#x5668;&#x68B0;&#xFF1B;&#x9500;&#x552E;&#x54CD;&#x53EA;&#xFF1B;&#x96F6;&#x552E;&#x836F;&#x53EA;<em><font color="#EF7599">&#xFF1B;&#x5E7F;&#x64AD;&#x7535;&#x89C6;&#x6B64;&#x76EE;&#x5236;&#x7ECF;</font></em>&#x3002;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x8D27;&#x7269;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x6280;&#x672F;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x4EE3;&#x7406;&#x5E03;&#x51FA;&#x53E3;&#xFF1B;&#x9500;&#x552E;&#x5E74;&#x8BAF;&#x8BBE;&#x6765;&#x3001;&#x53A8;&#x623F;&#x7528;&#x53EA;&#x3001;&#x536B;&#x793A;&#x7528;&#x53EA;&#xFF08;&#x542B;&#x661F;&#x6BD4;&#x62A4;&#x7406;&#x7528;&#x53EA;&#xFF09;&#x3001;&#x65E5;&#x7528;&#x6742;&#x8D27;&#x3001;&#x5316;&#x5986;&#x53EA;&#x3001;&#x53CA;&#x7597;&#x5668;&#x68B0;I&#x77F3;&#x3001;II&#x77F3;&#x3001;&#x907F;&#x5B55;&#x5668;&#x65AD;&#x3001;&#x73A9;&#x65AD;&#x3001;&#x6025;&#x80B2;&#x7528;&#x53EA;&#x3001;&#x6587;&#x5316;&#x7528;&#x53EA;&#x3001;&#x670D;&#x5C06;&#x978B;&#x5E3D;&#x3001;&#x949F;&#x4E89;&#x773C;&#x955C;&#x3001;&#x9488;&#x7EBA;&#x7EC7;&#x53EA;&#x3001;&#x81F4;&#x7528;&#x7535;&#x5668;&#x3001;&#x81F4;&#x65AD;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#x3001;&#x8BC1;&#x3001;&#x8349;&#x5916;&#x89C2;&#x8D4F;&#x690D;&#x7269;&#x3001;&#x4E0D;&#x518D;&#x5206;&#x5C06;&#x7684;&#x5305;&#x5C06;&#x8BE5;&#x5B50;&#x3001;&#x7FA4;&#x76F8;&#x5668;&#x6750;&#x3001;&#x4E09;&#x827A;&#x53EA;&#x3001;&#x53F2;&#x53EA;&#x3001;&#x6837;&#x5168;&#x673A;&#x3001;&#x8F6F;&#x4EF6;&#x5916;&#x8F85;&#x52A9;&#x8BBE;&#x6765;&#x3001;&#x73E0;&#x542C;&#x5404;&#x9970;&#x3001;&#x54CD;&#x7528;&#x867D;&#x4EA7;&#x53EA;&#x3001;&#x5BA0;&#x7269;&#x54CD;&#x53EA;&#x3001;&#x7535;&#x5B50;&#x4EA7;&#x53EA;&#x3001;&#x6469;&#x6258;&#x8F66;&#x3001;&#x7535;&#x8D44;&#x8F66;&#x3001;&#x81EA;&#x884C;&#x8F66;&#x5916;&#x96F6;&#x90E8;&#x4EF6;&#x3001;&#x667A;&#x52A8;&#x5361;&#x3001;&#x4E94;&#x91D1;&#x4EA4;&#x7535;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#x3001;&#x5EFA;&#x7B51;&#x6750;&#x653F;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#xFF1B;&#x6562;&#x4FEE;&#x4EEA;&#x5668;&#x4EEA;&#x4E89;&#xFF1B;&#x6562;&#x4FEE;&#x627E;&#x5F8B;&#x8BBE;&#x6765;&#xFF1B;&#x627F;&#x627E;&#x6309;&#x89C8;&#x6309;&#x5E72;&#x7C7B;&#x8D44;&#xFF1B;&#x751F;&#x544A;&#x670D;&#x52A1;&#xFF1B;&#x7B79;&#x6765;&#x3001;&#x7B56;&#x5212;&#x3001;&#x7EC4;&#x7EC7;&#x5927;&#x578B;&#x5E86;&#x5178;&#xFF1B;&#x8BBE;&#x6837;&#x3001;&#x5236;&#x7ECF;&#x3001;&#x4EE3;&#x7406;&#x3001;&#x5374;&#x89C4;&#x5E7F;&#x529B;&#xFF1B;&#x6444;&#x5F71;&#x6269;&#x5370;&#x670D;&#x52A1;&#xFF1B;&#x6587;&#x827A;&#x6F14;&#x51FA;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x6025;&#x80B2;&#x8D5B;&#x4E8B;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x6309;&#x89C8;&#x751F;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x535A;&#x89C8;&#x751F;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3002;&#x4F01;&#x4E1A;&#x8BF7;&#x6CD5;&#x81EA;&#x53F8;&#x9009;&#x62E9;&#x786E;&#x8D39;&#x9879;&#x76EE;&#xFF0C;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;&#x547D;&#x4E8B;&#x4E92;&#x5979;&#x7F51;&#x6587;&#x5316;&#x7C7B;&#x8D44;&#x3001;&#x51FA;&#x7248;&#x7269;&#x6279;&#x5374;&#x3001;&#x51FA;&#x7248;&#x7269;&#x96F6;&#x552E;&#x3001;&#x9500;&#x552E;&#x54CD;&#x53EA;<em><font color="#EF7599">&#x3001;&#x5E7F;&#x64AD;&#x7535;&#x89C6;&#x6B64;&#x76EE;&#x5236;&#x7ECF;</font></em>&#x3001;&#x96F6;&#x552E;&#x836F;&#x53EA;&#x3001;&#x9500;&#x552E;&#x7B2C;&#x4F5C;&#x77F3;&#x53CA;&#x7597;&#x5668;&#x68B0;&#x4EE5;&#x5916;&#x8BF7;&#x6CD5;&#x4E2A;&#x786E;&#x6279;&#x51C6;&#x7684;&#x9879;&#x76EE;&#xFF0C;&#x786E;&#x76F8;&#x6B66;&#x90E8;&#x95E8;&#x6279;&#x51C6;&#x98DF;&#x8BF7;&#x6279;&#x51C6;&#x7684;&#x5185;&#x5BB9;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;&#x4E0D;&#x5BDF;&#x547D;&#x4E8B;&#x672C;&#x597D;&#x4EA7;&#x4E1A;&#x5427;&#x7B56;&#x7981;&#x4F3C;&#x548C;&#x9650;&#x5236;&#x77F3;&#x9879;&#x76EE;&#x7684;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#x3002;</text></div></body></html></span><span ng-if="showDetail" ng-bind-html="content|splitNum"
        class="js-split-container "><html><head></head><body><div><text class="tyc-num">&#x6BCD;&#x673A;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x6BCD;&#x673A;&#x793A;&#x4EA7;&#x3001;&#x6BCD;&#x673A;&#x670D;&#x52A1;&#xFF08;&#x9650;&#x5C81;&#x6DC0;&#x533A;&#x6C38;&#x6377;&#x5317;&#x4F1A;6&#x5148;&#x5357;&#x5C42;&#x786E;&#x8D39;&#xFF09;&#xFF1B;&#x547D;...</text></div></body></html></span><a ng-show="needFolder" ng-click="showDetail = btnOnClick(showDetail)" style="cursor: pointer;"
     class="" onclick="folder.toggle(this)">详细</a></span></div></div></div></div><div class="pt15 pb15 "><div><div
          ng-bind-html="($index+1+(mobileChangeIndex*5))>9?($index+1+(mobileChangeIndex*5)):'0'+($index+1+(mobileChangeIndex*5))"          class="f14 new-border c9 p3 in-block vertical-top mr10">02</div><div class="in-block vertical-top"><div class="mb8"><span class="left-text">时间：</span><span>2018-04-04</span></div><div><span class="left-text">项目：</span><span>经营范围</span></div></div></div><div class="over-hide mt10"><div class="left-content float-left new-border" style="width: 49%;"><div class="changeSubTitle">变更前</div><div class="changeSubText"><span ng-init="showDetail = false;" class="js-shrink-container"><span ng-if="!showDetail" ng-bind-html="perContent|splitNum"
        class="js-full-container hidden"><html><head></head><body><div><text class="tyc-num">&#x6BCD;&#x673A;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x6BCD;&#x673A;&#x793A;&#x4EA7;&#x3001;&#x6BCD;&#x673A;&#x670D;&#x52A1;<em><font style="color:#0E0E0E;text-decoration:line-through;text-decoration-color:#ff2b23;">&#xFF1B;</font></em>&#xFF08;&#x9650;&#x5C81;&#x6DC0;&#x533A;&#x6C38;&#x6377;&#x5317;&#x4F1A;6&#x5148;&#x5357;&#x5C42;&#x786E;&#x8D39;&#xFF09;&#x547D;&#x4E8B;&#x4E92;&#x5979;&#x7F51;&#x6587;&#x5316;&#x7C7B;&#x8D44;&#x3002;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x8D27;&#x7269;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x6280;&#x672F;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x4EE3;&#x7406;&#x5E03;&#x51FA;&#x53E3;&#xFF1B;&#x9500;&#x552E;&#x5E74;&#x8BAF;&#x8BBE;&#x6765;&#xFF1B;&#x6562;&#x4FEE;&#x4EEA;&#x5668;&#x4EEA;&#x4E89;&#xFF1B;&#x6562;&#x4FEE;&#x627E;&#x5F8B;&#x8BBE;&#x6765;&#xFF1B;&#x627F;&#x627E;&#x6309;&#x89C8;&#x6309;&#x5E72;&#x7C7B;&#x8D44;&#xFF1B;&#x751F;&#x544A;&#x670D;&#x52A1;&#xFF1B;&#x7B79;&#x6765;&#x3001;&#x7B56;&#x5212;&#x3001;&#x7EC4;&#x7EC7;&#x5927;&#x578B;&#x5E86;&#x5178;&#xFF1B;&#x8BBE;&#x6837;&#x3001;&#x5236;&#x7ECF;&#x3001;&#x4EE3;&#x7406;&#x3001;&#x5374;&#x89C4;&#x5E7F;&#x529B;&#x3002;&#x4F01;&#x4E1A;&#x8BF7;&#x6CD5;&#x81EA;&#x53F8;&#x9009;&#x62E9;&#x786E;&#x8D39;&#x9879;&#x76EE;&#xFF0C;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;&#x8BF7;&#x6CD5;&#x4E2A;&#x786E;&#x6279;&#x51C6;&#x7684;&#x9879;&#x76EE;&#xFF0C;&#x786E;&#x76F8;&#x6B66;&#x90E8;&#x95E8;&#x6279;&#x51C6;&#x98DF;&#x8BF7;&#x6279;&#x51C6;&#x7684;&#x5185;&#x5BB9;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;&#x4E0D;&#x5BDF;&#x547D;&#x4E8B;&#x672C;&#x597D;&#x4EA7;&#x4E1A;&#x5427;&#x7B56;&#x7981;&#x4F3C;&#x548C;&#x9650;&#x5236;&#x77F3;&#x9879;&#x76EE;&#x7684;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#x3002;</text></div></body></html></span><span ng-if="showDetail" ng-bind-html="content|splitNum"
        class="js-split-container "><html><head></head><body><div><text class="tyc-num">&#x6BCD;&#x673A;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x6BCD;&#x673A;&#x793A;&#x4EA7;&#x3001;&#x6BCD;&#x673A;&#x670D;&#x52A1;<em></em></text></div></body></html></span><a ng-show="needFolder" ng-click="showDetail = btnOnClick(showDetail)" style="cursor: pointer;"
     class="" onclick="folder.toggle(this)">详细</a></span></div></div><div class="right-content float-right new-border" style="width: 49%;"><div class="changeSubTitle">变更后</div><div class="changeSubText"><span ng-init="showDetail = false;" class="js-shrink-container"><span ng-if="!showDetail" ng-bind-html="perContent|splitNum"
        class="js-full-container hidden"><html><head></head><body><div><text class="tyc-num">&#x6BCD;&#x673A;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x6BCD;&#x673A;&#x793A;&#x4EA7;&#x3001;&#x6BCD;&#x673A;&#x670D;&#x52A1;&#xFF08;&#x9650;&#x5C81;&#x6DC0;&#x533A;&#x6C38;&#x6377;&#x5317;&#x4F1A;6&#x5148;&#x5357;&#x5C42;&#x786E;&#x8D39;&#xFF09;<em><font color="#EF7599">&#xFF1B;</font></em>&#x547D;&#x4E8B;&#x4E92;&#x5979;&#x7F51;&#x6587;&#x5316;&#x7C7B;&#x8D44;<em><font color="#EF7599">&#xFF1B;&#x51FA;&#x7248;&#x7269;&#x96F6;&#x552E;&#xFF1B;&#x51FA;&#x7248;&#x7269;&#x6279;&#x5374;&#xFF1B;&#x9500;&#x552E;&#x7B2C;&#x4F5C;&#x77F3;&#x53CA;&#x7597;&#x5668;&#x68B0;&#xFF1B;&#x9500;&#x552E;&#x54CD;&#x53EA;&#xFF1B;&#x96F6;&#x552E;&#x836F;&#x53EA;</font></em>&#x3002;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x8D27;&#x7269;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x6280;&#x672F;&#x5E03;&#x51FA;&#x53E3;&#x3001;&#x4EE3;&#x7406;&#x5E03;&#x51FA;&#x53E3;&#xFF1B;&#x9500;&#x552E;&#x5E74;&#x8BAF;&#x8BBE;&#x6765;<em><font color="#EF7599">&#x3001;&#x53A8;&#x623F;&#x7528;&#x53EA;&#x3001;&#x536B;&#x793A;&#x7528;&#x53EA;&#xFF08;&#x542B;&#x661F;&#x6BD4;&#x62A4;&#x7406;&#x7528;&#x53EA;&#xFF09;&#x3001;&#x65E5;&#x7528;&#x6742;&#x8D27;&#x3001;&#x5316;&#x5986;&#x53EA;&#x3001;&#x53CA;&#x7597;&#x5668;&#x68B0;I&#x77F3;&#x3001;II&#x77F3;&#x3001;&#x907F;&#x5B55;&#x5668;&#x65AD;&#x3001;&#x73A9;&#x65AD;&#x3001;&#x6025;&#x80B2;&#x7528;&#x53EA;&#x3001;&#x6587;&#x5316;&#x7528;&#x53EA;&#x3001;&#x670D;&#x5C06;&#x978B;&#x5E3D;&#x3001;&#x949F;&#x4E89;&#x773C;&#x955C;&#x3001;&#x9488;&#x7EBA;&#x7EC7;&#x53EA;&#x3001;&#x81F4;&#x7528;&#x7535;&#x5668;&#x3001;&#x81F4;&#x65AD;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#x3001;&#x8BC1;&#x3001;&#x8349;&#x5916;&#x89C2;&#x8D4F;&#x690D;&#x7269;&#x3001;&#x4E0D;&#x518D;&#x5206;&#x5C06;&#x7684;&#x5305;&#x5C06;&#x8BE5;&#x5B50;&#x3001;&#x7FA4;&#x76F8;&#x5668;&#x6750;&#x3001;&#x4E09;&#x827A;&#x53EA;&#x3001;&#x53F2;&#x53EA;&#x3001;&#x6837;&#x5168;&#x673A;&#x3001;&#x8F6F;&#x4EF6;&#x5916;&#x8F85;&#x52A9;&#x8BBE;&#x6765;&#x3001;&#x73E0;&#x542C;&#x5404;&#x9970;&#x3001;&#x54CD;&#x7528;&#x867D;&#x4EA7;&#x53EA;&#x3001;&#x5BA0;&#x7269;&#x54CD;&#x53EA;&#x3001;&#x7535;&#x5B50;&#x4EA7;&#x53EA;&#x3001;&#x6469;&#x6258;&#x8F66;&#x3001;&#x7535;&#x8D44;&#x8F66;&#x3001;&#x81EA;&#x884C;&#x8F66;&#x5916;&#x96F6;&#x90E8;&#x4EF6;&#x3001;&#x667A;&#x52A8;&#x5361;&#x3001;&#x4E94;&#x91D1;&#x4EA4;&#x7535;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;&#x3001;&#x5EFA;&#x7B51;&#x6750;&#x653F;&#xFF08;&#x4E0D;&#x547D;&#x4E8B;&#x5FC5;&#x6025;&#x5E97;&#x94FA;&#x786E;&#x8D39;&#xFF09;</font></em>&#xFF1B;&#x6562;&#x4FEE;&#x4EEA;&#x5668;&#x4EEA;&#x4E89;&#xFF1B;&#x6562;&#x4FEE;&#x627E;&#x5F8B;&#x8BBE;&#x6765;&#xFF1B;&#x627F;&#x627E;&#x6309;&#x89C8;&#x6309;&#x5E72;&#x7C7B;&#x8D44;&#xFF1B;&#x751F;&#x544A;&#x670D;&#x52A1;&#xFF1B;&#x7B79;&#x6765;&#x3001;&#x7B56;&#x5212;&#x3001;&#x7EC4;&#x7EC7;&#x5927;&#x578B;&#x5E86;&#x5178;&#xFF1B;&#x8BBE;&#x6837;&#x3001;&#x5236;&#x7ECF;&#x3001;&#x4EE3;&#x7406;&#x3001;&#x5374;&#x89C4;&#x5E7F;&#x529B;<em><font color="#EF7599">&#xFF1B;&#x6444;&#x5F71;&#x6269;&#x5370;&#x670D;&#x52A1;&#xFF1B;&#x6587;&#x827A;&#x6F14;&#x51FA;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x6025;&#x80B2;&#x8D5B;&#x4E8B;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x6309;&#x89C8;&#x751F;&#x7968;&#x52A1;&#x4EE3;&#x7406;&#x3001;&#x535A;&#x89C8;&#x751F;&#x7968;&#x52A1;&#x4EE3;&#x7406;</font></em>&#x3002;&#x4F01;&#x4E1A;&#x8BF7;&#x6CD5;&#x81EA;&#x53F8;&#x9009;&#x62E9;&#x786E;&#x8D39;&#x9879;&#x76EE;&#xFF0C;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;<em><font color="#EF7599">&#x547D;&#x4E8B;&#x4E92;&#x5979;&#x7F51;&#x6587;&#x5316;&#x7C7B;&#x8D44;&#x3001;&#x51FA;&#x7248;&#x7269;&#x6279;&#x5374;&#x3001;&#x51FA;&#x7248;&#x7269;&#x96F6;&#x552E;&#x3001;&#x9500;&#x552E;&#x54CD;&#x53EA;&#x3001;&#x96F6;&#x552E;&#x836F;&#x53EA;&#x3001;&#x9500;&#x552E;&#x7B2C;&#x4F5C;&#x77F3;&#x53CA;&#x7597;&#x5668;&#x68B0;&#x4EE5;&#x5916;</font></em>&#x8BF7;&#x6CD5;&#x4E2A;&#x786E;&#x6279;&#x51C6;&#x7684;&#x9879;&#x76EE;&#xFF0C;&#x786E;&#x76F8;&#x6B66;&#x90E8;&#x95E8;&#x6279;&#x51C6;&#x98DF;&#x8BF7;&#x6279;&#x51C6;&#x7684;&#x5185;&#x5BB9;&#x4E3B;&#x6309;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#xFF1B;&#x4E0D;&#x5BDF;&#x547D;&#x4E8B;&#x672C;&#x597D;&#x4EA7;&#x4E1A;&#x5427;&#x7B56;&#x7981;&#x4F3C;&#x548C;&#x9650;&#x5236;&#x77F3;&#x9879;&#x76EE;&#x7684;&#x786E;&#x8D39;&#x7C7B;&#x8D44;&#x3002;</text></div></body></html></span><span ng-if="showDetail" ng-bind-html="content|splitNum"
        class="js-split-container "><html><head></head><body><div><text class="tyc-num">&#x6BCD;&#x673A;&#x6280;&#x672F;&#x4E3B;&#x5374;&#xFF1B;&#x6BCD;&#x673A;&#x793A;&#x4EA7;&#x3001;&#x6BCD;&#x673A;&#x670D;&#x52A1;&#xFF08;&#x9650;&#x5C81;&#x6DC0;&#x533A;&#x6C38;&#x6377;&#x5317;&#x4F1A;6&#x5148;&#x5357;&#x5C42;&#x786E;&#x8D39;&#xFF09;<e...< div=""></e...<></text></div></body></html></span><a ng-show="needFolder" ng-click="showDetail = btnOnClick(showDetail)" style="cursor: pointer;"
     class="" onclick="folder.toggle(this)">详细</a></span></div></div></div></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">23条</span>变更信息</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="25" change-type="changeinfo"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(4,this)"

      >4</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(5,this)"

      >5</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>5<span>页</span></div></div></div></div></div><!--end变更信息--><!--6企业年报--><div><div id="nav-main-reportCount" class="header-container"><div class="itemTitle">企业年报</div></div><div class="over-hide"><div class="limit-2-download hi-show"><div class="content-container"><div><a target="_blank"
         href="/reportContent/23402373/2017"

         class="pt15 pb15 block new-border-bottom"><span>2017年度报告</span><span class="float-right new-c1"><i class="tic tic-angle-right"></i></span></a></div><div><a target="_blank"
         href="/reportContent/23402373/2016"

         class="pt15 pb15 block "><span>2016年度报告</span><span class="float-right new-c1"><i class="tic tic-angle-right"></i></span></a></div></div></div></div></div><!--end企业年报--><!--7分支机构--><div><div id="nav-main-branchCount" class="header-container"><div class="itemTitle">分支机构</div></div><div id="_container_branch"><div class="limit-2-download hi-show"><div class="content-container"><div class="pt15 pb15 new-border-bottom"><a href="https://m.tianyancha.com/company/250301586"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司厦门分公司</span></a></div><div class="pt15 pb15 new-border-bottom"><a href="https://m.tianyancha.com/company/758060794"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司天津南开分公司</span></a></div><div class="pt15 pb15 new-border-bottom"><a href="https://m.tianyancha.com/company/759368745"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司沈阳分公司</span></a></div><div class="pt15 pb15 new-border-bottom"><a href="https://m.tianyancha.com/company/776643061"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司重庆分公司</span></a></div><div class="pt15 pb15 new-border-bottom"><a href="https://m.tianyancha.com/company/1588963427"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司上海分公司</span></a></div><div class="pt15 pb15 new-border-bottom"><a href="https://m.tianyancha.com/company/1649215379"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司武汉分公司</span></a></div><div class="pt15 pb15 new-border-bottom"><a href="https://m.tianyancha.com/company/2309670530"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司成都分公司</span></a></div><div class="pt15 pb15 new-border-bottom"><a href="https://m.tianyancha.com/company/2325133301"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司郑州分公司</span></a></div><div class="pt15 pb15 new-border-bottom"><a href="https://m.tianyancha.com/company/2334497566"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司济南分公司</span></a></div><div class="pt15 pb15 "><a href="https://m.tianyancha.com/company/2335560760"
         style="word-break: break-all;"
         class="query_name"><span>小米科技有限责任公司仙桃分公司</span></a></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">17个</span>分支机构</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="19" change-type="branch"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>2<span>页</span></div></div></div></div></div><!--end分支机构--><!--entityType  ==1公司 ，2香港，3社会组织，4律所 5事业单位 6基金会--><!--8融资历史--><div ng-if="items2.companyRongzi.show&&dataItemCount.companyRongzi>0"><div id="nav-main-companyRongzi" class="header-container"><div class="itemTitle">融资历史</div></div><div id="_container_rongzi"><div class="limit-2-download hi-show"><div class="content-container"><div class="pt15 pb15 new-border-bottom"><div><span class="left-text">融资时间：</span><span>2018-07-09</span></div><div class="item-line"><span class="left-text">融资金额：</span><span>370.53亿港元</span></div><div class="item-line"><span class="left-text">融资阶段：</span><span>IPO上市</span></div><div class="item-line"><span class="left-text">投资方：</span><span><a 
            class="pr10 text-dark-color"
            target="_blank">公开发行</a></span></div></div><div class="pt15 pb15 "><div><span class="left-text">融资时间：</span><span>2014-12-29</span></div><div class="item-line"><span class="left-text">融资金额：</span><span>11亿美元</span></div><div class="item-line"><span class="left-text">融资阶段：</span><span>E轮</span></div><div class="item-line"><span class="left-text">投资方：</span><span><a href="https://m.tianyancha.com/organize/b489b2923"
            class="pr10 c9 point"
            target="_blank">DST Global</a></span><span><a href="https://m.tianyancha.com/organize/bbd852257"
            class="pr10 c9 point"
            target="_blank">厚朴投资</a></span><span><a href="https://m.tianyancha.com/organize/bd6512963"
            class="pr10 c9 point"
            target="_blank">云锋基金</a></span><span><a href="https://m.tianyancha.com/organize/b2bbf879"
            class="pr10 c9 point"
            target="_blank">全明星投资All-Stars Investment</a></span><span><a href="https://m.tianyancha.com/organize/bc8461547"
            class="pr10 c9 point"
            target="_blank">GIC新加坡政府投资公司</a></span></div></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">4条</span>融资历史</a></div></div></div></div><!--end融资历史--><!--9核心团队--><div ng-if="items2.companyTeammember.show&&dataItemCount.companyTeammember>0"><div id="nav-main-companyTeammember" class="header-container"><div class="itemTitle">核心团队</div></div><div id="_container_teamMember"><div class="limit-2-download hi-show"><div class="content-container"><div class="pt15 pb15 new-border-bottom"><div><div class="in-block vertival-middle teamMemberImg"><img style="width: 60px;"
               src="https://img.tianyancha.com/logo/company/ac142ff22e49a622ea75dcb6604375b5.png@!z_200x200"
               onerror="this.src='https://static.tianyancha.com/logo/teamMember/def_photo.png'" alt=""></div><div class="in-block vertival-middle pl20"><div>雷军</div><div class="left-text">创始人&CEO</div></div></div><div style="line-height: 30px;"><span style="word-break: break-all;" content-folder content="team.desc" num="60"><span ng-init="showDetail = false;" class="js-shrink-container"><span ng-if="!showDetail" ng-bind-html="perContent|splitNum"
        class="js-full-container hidden"><html><head></head><body><div>&#x96F7;&#x519B;&#xFF0C;&#x5929;&#x4F7F;&#x6295;&#x8D44;&#x4EBA;&#x96F7;&#x519B;&#x521B;&#x59CB;&#x4EBA;&#x3002;&#x96F7;&#x519B;&#x5148;&#x751F;&#x662F;&#x4E2D;&#x56FD;IT&#x754C;&#x77E5;&#x540D;&#x7684;&#x4F01;&#x4E1A;&#x5BB6;&#x548C;&#x5929;&#x4F7F;&#x6295;&#x8D44;&#x4EBA;&#xFF0C;&#x603B;&#x7ED3;&#x51FA;&#x4E86;&#x201C;&#x4E92;&#x8054;&#x7F51;&#x601D;&#x60F3;&#x4E03;&#x5B57;&#x8BC0;&#x201D;&#x3001;&#x201C;&#x98DE;&#x732A;&#x7406;&#x8BBA;&#x201D;&#x3001;&#x201C;&#x987A;&#x52BF;&#x800C;&#x4E3A;&#x201D;&#x7B49;&#x4E00;&#x7CFB;&#x5217;&#x77E5;&#x540D;&#x89C2;&#x70B9;&#x3002;&#x96F7;&#x519B;&#x5148;&#x751F;&#x4E8E;2010 &#x5E74;&#x521B;&#x529E;&#x5C0F;&#x7C73;&#x79D1;&#x6280;&#xFF0C;&#x73B0;&#x4EFB;&#x5C0F;&#x7C73;&#x79D1;&#x6280;&#x8463;&#x4E8B;&#x957F;&#x517C;CEO&#xFF0C;&#x540C;&#x65F6;&#x517C;&#x4EFB;&#x91D1;&#x5C71;&#x3001;YY&#x3001;&#x730E;&#x8C79;&#x7B49;&#x4E09;&#x5BB6;&#x4E0A;&#x5E02;&#x516C;&#x53F8;&#x8463;&#x4E8B;&#x957F;&#x3002;&#x96F7;&#x519B;&#x5148;&#x751F;&#x7684;&#x804C;&#x4E1A;&#x751F;&#x6DAF;&#x59CB;&#x4E8E;&#x91D1;&#x5C71;&#xFF0C;&#x4ED6;&#x662F;&#x91D1;&#x5C71;&#x8F6F;&#x4EF6;&#x7684;&#x8054;&#x5408;&#x521B;&#x59CB;&#x4EBA;&#x53CA;&#x73B0;&#x4EFB;&#x8463;&#x4E8B;&#x957F;&#xFF0C;&#x4E8E;2007&#x5E74;&#x5E26;&#x9886;&#x91D1;&#x5C71;&#x8F6F;&#x4EF6;&#x6210;&#x529F;&#x4E0A;&#x5E02;&#x3002;&#x4ED6;&#x540C;&#x65F6;&#x4E5F;&#x662F;&#x5353;&#x8D8A;&#x7F51;&#x521B;&#x59CB;&#x4EBA;&#xFF0C;&#x5E76;&#x4E8E;2004&#x5E74;&#x6210;&#x529F;&#x5C06;&#x5176;&#x51FA;&#x552E;&#x7ED9;&#x4E9A;&#x9A6C;&#x900A;&#x3002;&#x4F5C;&#x4E3A;&#x5929;&#x4F7F;&#x6295;&#x8D44;&#x4EBA;&#xFF0C;&#x96F7;&#x519B;&#x5148;&#x751F;&#x4E50;&#x4E8E;&#x4E3A;&#x521B;&#x4E1A;&#x4F01;&#x4E1A;&#x7684;&#x521B;&#x7ACB;&#x53CA;&#x6210;&#x957F;&#x63D0;&#x4F9B;&#x5E2E;&#x52A9;&#x3002;&#x5F97;&#x76CA;&#x4E8E;&#x96F7;&#x519B;&#x5148;&#x751F;&#x7684;&#x534F;&#x52A9;&#xFF0C;&#x6295;&#x8D44;&#x7684;&#x4F01;&#x4E1A;&#x4E2D;&#xFF0C;&#x591A;&#x73A9;(YY)&#x5DF2;&#x7ECF;&#x6210;&#x529F;&#x767B;&#x9646;&#x7EB3;&#x65AF;&#x8FBE;&#x514B;&#xFF0C;&#x51E1;&#x5BA2;&#x8BDA;&#x54C1;&#x3001;UCweb&#x3001;&#x957F;&#x57CE;&#x4F1A;&#x7B49;&#x5728;&#x5404;&#x81EA;&#x9886;&#x57DF;&#x5747;&#x6709;&#x4F18;&#x5F02;&#x8868;&#x73B0;&#x3002;&#x66FE;&#x5F53;&#x9009;&#x300A;&#x798F;&#x5E03;&#x65AF;&#x300B;&#xFF08;&#x4E9A;&#x6D32;&#x7248;&#xFF09;2014&#x5E74;&#x5EA6;&#x5546;&#x4E1A;&#x4EBA;&#x7269;&#x3002;</div></body></html></span><span ng-if="showDetail" ng-bind-html="content|splitNum"
        class="js-split-container "><html><head></head><body><div>&#x96F7;&#x519B;&#xFF0C;&#x5929;&#x4F7F;&#x6295;&#x8D44;&#x4EBA;&#x96F7;&#x519B;&#x521B;&#x59CB;&#x4EBA;&#x3002;&#x96F7;&#x519B;&#x5148;&#x751F;&#x662F;&#x4E2D;&#x56FD;IT&#x754C;&#x77E5;&#x540D;&#x7684;&#x4F01;&#x4E1A;&#x5BB6;&#x548C;&#x5929;&#x4F7F;&#x6295;&#x8D44;&#x4EBA;&#xFF0C;&#x603B;&#x7ED3;&#x51FA;&#x4E86;&#x201C;&#x4E92;&#x8054;&#x7F51;&#x601D;&#x60F3;&#x4E03;&#x5B57;&#x8BC0;&#x201D;&#x3001;&#x201C;&#x98DE;&#x732A;&#x7406;&#x8BBA;...</div></body></html></span><a ng-show="needFolder" ng-click="showDetail = btnOnClick(showDetail)" style="cursor: pointer;"
     class="" onclick="folder.toggle(this)">详细</a></span></span></div></div><div class="pt15 pb15 new-border-bottom"><div><div class="in-block vertival-middle teamMemberImg"><img style="width: 60px;"
               src="https://img.tianyancha.com/logo/company/506be2b8e5ef9a383722a594d8adc84a.jpg@!z_200x200"
               onerror="this.src='https://static.tianyancha.com/logo/teamMember/def_photo.png'" alt=""></div><div class="in-block vertival-middle pl20"><div>林斌</div><div class="left-text">联合创始人&总裁</div></div></div><div style="line-height: 30px;"><span style="word-break: break-all;" content-folder content="team.desc" num="60"><span ng-init="showDetail = false;" class="js-shrink-container"><span ng-if="!showDetail" ng-bind-html="perContent|splitNum"
        class="js-full-container hidden"><html><head></head><body><div>&#x6797;&#x658C;&#xFF0C;&#x5C0F;&#x7C73;&#x79D1;&#x6280;&#x8054;&#x5408;&#x521B;&#x59CB;&#x4EBA;&amp;&#x603B;&#x88C1;&#x3002;&#x524D;&#x8C37;&#x6B4C;&#x4E2D;&#x56FD;&#x5DE5;&#x7A0B;&#x7814;&#x7A76;&#x9662;&#x526F;&#x9662;&#x957F;&#xFF0C;Google&#x5168;&#x7403;&#x5DE5;&#x7A0B;&#x603B;&#x76D1;&#x3002;&#x65E9;&#x524D;&#x53C2;&#x4E0E;&#x521B;&#x5EFA;&#x5FAE;&#x8F6F;&#x4E9A;&#x6D32;&#x5DE5;&#x7A0B;&#x9662;&#x5E76;&#x51FA;&#x4EFB;&#x5DE5;&#x7A0B;&#x603B;&#x76D1;&#x3002;</div></body></html></span><span ng-if="showDetail" ng-bind-html="content|splitNum"
        class="js-split-container "><html><head></head><body><div>&#x6797;&#x658C;&#xFF0C;&#x5C0F;&#x7C73;&#x79D1;&#x6280;&#x8054;&#x5408;&#x521B;&#x59CB;&#x4EBA;&amp;&#x603B;&#x88C1;&#x3002;&#x524D;&#x8C37;&#x6B4C;&#x4E2D;&#x56FD;&#x5DE5;&#x7A0B;&#x7814;&#x7A76;&#x9662;&#x526F;&#x9662;&#x957F;&#xFF0C;Google&#x5168;&#x7403;&#x5DE5;&#x7A0B;&#x603B;&#x76D1;&#x3002;&#x65E9;&#x524D;&#x53C2;&#x4E0E;&#x521B;&#x5EFA;&#x5FAE;&#x8F6F;&#x4E9A;&#x6D32;&#x5DE5;&#x7A0B;&#x9662;&#x5E76;...</div></body></html></span><a ng-show="needFolder" ng-click="showDetail = btnOnClick(showDetail)" style="cursor: pointer;"
     class="" onclick="folder.toggle(this)">详细</a></span></span></div></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">15位</span>核心团队</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="17" change-type="teamMember"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(4,this)"

      >4</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>4<span>页</span></div></div></div></div></div><!--end核心团队--><!--10企业业务--><div ng-if="items2.companyProduct.show&&dataItemCount.companyProduct>0"><div id="nav-main-companyProduct" class="header-container"><div class="itemTitle">企业业务<!--<span>（{{dataItemCount.companyProduct}}）</span>--></div></div><div id="_container_firmProduct"><div class="limit-2-download hi-show"><div class="content-container"><div class=""><div class="mobile-img-box vertival-middle"><img class="w100"
             src="https://img.tianyancha.com/logo/product/75bbea0a24efeee7686c805535b3b371.png@!f_200x200"
             alt="" onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="new-c3 pr10">MIJIA米家</span></div><div class="mobile-box-middle"><span class="">类型 ：</span><span class="new-c3">硬件</span></div><div class="mobile-box-bottom"><span class="">描述 ：</span><span class="new-c3">智能硬件生产制造商</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertival-middle"><img class="w100"
             src="https://img.tianyancha.com/logo/product/30b1c692e0395e849ebf3e6d1dd60046.png@!f_200x200"
             alt="" onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="new-c3 pr10">小米直播</span></div><div class="mobile-box-middle"><span class="">类型 ：</span><span class="new-c3">文娱传媒</span></div><div class="mobile-box-bottom"><span class="">描述 ：</span><span class="new-c3">在线视频直播平台</span></div></div><hr class="mboile-hide-hr"/></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">9个</span>企业业务</a></div></div></div></div><!--end企业业务--><!--11投资事件--><div ng-if="items2.jigouTzanli.show&&dataItemCount.jigouTzanli>0"><div id="nav-main-jigouTzanli" class="header-container"><div class="itemTitle">投资事件<!-- <span>（{{dataItemCount.jigouTzanli}}）</span>--></div></div><div id="_container_touzi"><div class="limit-2-download hi-show"><div class="content-container"><div ng-repeat="te in Tzanli" class=""><div class="mobile-img-box vertival-middle"><img class="w100"
             src="https://img.tianyancha.com/logo/product/1af03054a9251b4baf876e491efd31b1.png@!f_200x200"
             alt="" onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="new-c3 pr10 f16">慧算账</span><span
            class="yellowbox in-block vertival-bottom">C轮</span></div><div class="mobile-box-middle"><span class="">投资时间 ：</span><span
            class="new-c3">2018-09-26</span></div><div class="mobile-box-middle"><span class="">投资金额 ：</span><span class="new-c3">未披露</span></div><div class="mobile-box-middle"><span class="">行业 ：</span><span class="new-c3 ">企业服务</span></div><div class="mobile-box-bottom"><span class="">参投公司 ：</span><a href="https://m.tianyancha.com/organize/b052b24841"
            class="text-click-color point "
            target="_blank">高成资本</a><a href="https://m.tianyancha.com/organize/b48be2888"
            class="text-click-color point "
            target="_blank">小米科技</a></div></div><hr class="mobile-hr"/></div><div ng-repeat="te in Tzanli" class=""><div class="mobile-img-box vertival-middle"><img class="w100"
             src="https://img.tianyancha.com/logo/product/db4637a092ea133bede0e6815b6c3fb2.png@!f_200x200"
             alt="" onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="new-c3 pr10 f16">新趋势地产</span><span
            class="yellowbox in-block vertival-bottom">A轮</span></div><div class="mobile-box-middle"><span class="">投资时间 ：</span><span
            class="new-c3">2018-08-29</span></div><div class="mobile-box-middle"><span class="">投资金额 ：</span><span class="new-c3">未披露</span></div><div class="mobile-box-middle"><span class="">行业 ：</span><span class="new-c3 ">房产家居</span></div><div class="mobile-box-bottom"><span class="">参投公司 ：</span><a href="https://m.tianyancha.com/organize/b48be2888"
            class="text-click-color point "
            target="_blank">小米科技</a><a href="https://m.tianyancha.com/organize/bceb13031"
            class="text-click-color point "
            target="_blank">IDG资本</a></div></div><hr class="mboile-hide-hr"/></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">219个</span>投资事件</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="221" change-type="touzi"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(4,this)"

      >4</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(5,this)"

      >5</a></li><li class="pagination-page " style=""><a
        onclick="companyPageChange(6,this)"

      >...</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>23<span>页</span></div></div></div></div></div><!--end投资事件--><!--12竞品信息--><div ng-if="items2.companyJingpin.show&&dataItemCount.companyJingpin>0"><div id="nav-main-companyJingpin" class="header-container"><div class="itemTitle">竞品信息</div></div><div id="_container_jingpin"><div class="limit-2-download hi-show"><div class="content-container"><div ng-repeat="jp in jingpin.page.rows" class=""><div class="mobile-img-box vertival-middle"><img alt="恒控科技" class="w100"
             src="https://img.tianyancha.com/logo/product/b7b386edf077b4d397e249c092073cfe.png@!f_200x200"
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="new-c3 pr10 f16">恒控科技</span></div><div class="mobile-box-middle"><span class="">业务 ：</span><span class="new-c3">智能家居产品研发商</span></div><div class="mobile-box-middle"><span class="">成立日期 ：</span><span
            class="new-c3 ">2018-07-12</span></div><div class="mobile-box-bottom"><span class="">关联公司 ：</span><a
            class="text-click-color" href="/company/3214105012"
            target="_blank">浙江恒控物联科技有限公司</a></div></div><hr class="mobile-hr"/></div><div ng-repeat="jp in jingpin.page.rows" class=""><div class="mobile-img-box vertival-middle"><img alt="子弹短信" class="w100"
             src="https://img.tianyancha.com/logo/product/9c1b05f115d4ae2f4f40bbcf259ee4ea.png@!f_200x200"
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="new-c3 pr10 f16">子弹短信</span><span class="yellowbox in-block vertival-bottom">B轮</span></div><div class="mobile-box-middle"><span class="">业务 ：</span><span class="new-c3">高效社交软件开发服务商</span></div><div class="mobile-box-middle"><span class="">成立日期 ：</span><span
            class="new-c3 ">2018-05-02</span></div><div class="mobile-box-bottom"><span class="">关联公司 ：</span><a
            class="text-click-color" href="/company/3188590355"
            target="_blank">北京快如科技有限公司</a></div></div><hr class="mboile-hide-hr"/></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">381个</span>竞品信息</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="383" change-type="jingpin"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(4,this)"

      >4</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(5,this)"

      >5</a></li><li class="pagination-page " style=""><a
        onclick="companyPageChange(6,this)"

      >...</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>39<span>页</span></div></div></div></div></div><!--end竞品信息--><!--13法律诉讼--><div><div id="nav-main-lawsuitCount" class="header-container"><div class="itemTitle">法律诉讼</div></div><div id="_container_lawsuit"><div class="limit-2-download hi-show"><div class="content-container"><div class="pt15 pb15 new-border-bottom"><div><a href="https://m.tianyancha.com/lawsuit/634022bebd6a11e8a8b47cd30ae00894">中国电信股份有限公司信丰分公司阳明中路营业厅一审民事裁定书
</a></div><div class="item-line"><span
          class="left-text">案件类型：</span><span>民事案件</span></div><div class="item-line"><span class="left-text">发布日期：</span><span>2018-08-27</span></div></div><div class="pt15 pb15 new-border-bottom"><div><a href="https://m.tianyancha.com/lawsuit/9ddf8012bd6811e8a8b47cd30ae00894">小米科技有限责公司与付伟侵害商标权纠纷二审民事判决书
</a></div><div class="item-line"><span
          class="left-text">案件类型：</span><span>民事案件</span></div><div class="item-line"><span class="left-text">发布日期：</span><span>2018-08-20</span></div></div><div class="pt15 pb15 new-border-bottom"><div><a href="https://m.tianyancha.com/lawsuit/d5703e08bd6b11e8a8b47cd30ae00894">刘成相与北京市工商行政管理局等其他一审行政判决书
</a></div><div class="item-line"><span
          class="left-text">案件类型：</span><span>行政案件</span></div><div class="item-line"><span class="left-text">发布日期：</span><span>2018-08-13</span></div></div><div class="pt15 pb15 new-border-bottom"><div><a href="https://m.tianyancha.com/lawsuit/d7561096a02a11e8a8b47cd30ae00894">小米科技有限责任公司与江苏苏宁易购电子商务有限公司、深圳信昌国际数码科技有限责任公司侵害商标权纠纷二审民事裁定书</a></div><div class="item-line"><span
          class="left-text">案件类型：</span><span>民事案件</span></div><div class="item-line"><span class="left-text">发布日期：</span><span>2018-08-13</span></div></div><div class="pt15 pb15 "><div><a href="https://m.tianyancha.com/lawsuit/bbf81ccbbd6b11e8a8b47cd30ae00894">小米科技有限公司与安岳县鑫五洋通信设备有限公司侵害商标权纠纷一审民事裁定书
</a></div><div class="item-line"><span
          class="left-text">案件类型：</span><span>民事案件</span></div><div class="item-line"><span class="left-text">发布日期：</span><span>2018-08-13</span></div></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">2671条</span>法律诉讼</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="2673" change-type="lawsuit"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(4,this)"

      >4</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(5,this)"

      >5</a></li><li class="pagination-page " style=""><a
        onclick="companyPageChange(6,this)"

      >...</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>268<span>页</span></div></div></div></div></div><!--end法律诉讼--><!--14法院公告--><div><div id="nav-main-courtCount" class="header-container"><div class="itemTitle">法院公告</div></div><div id="_container_court"><div class="limit-2-download hi-show"><div class="content-container"><div><script type="text/html">{"id":4899243,"announce_id":6979054,"bltnno":"1018092701199","bltnstate":null,"bltntype":null,"bltntypename":"裁判文书","caseno":null,"content":"北京晟煌科技有限公司：本院受理原告小米科技有限责任公司诉被告北京晟煌科技有限公司侵害商标权纠纷一案，已审理终结。现依法向你公告送达（2018）京0101民初6278号民事判决书。自公告之日起60日内来本院领取民事判决书，逾期则视为送达。如不服本判决，可在公告期满后15日内，向本院递交上诉状及副本，上诉于北京知识产权法院。逾期本判决即发生法律效力。特此公告。北京市东城区人民法院","courtflag":null,"courtcode":"北京市东城区人民法院","customno":null,"dealgrade":null,"dealgradename":null,"judge":null,"judgephone":"非公示项","mobilephone":"非公示项","party1":"小米科技有限责任公司","party2":"北京晟煌科技有限公司","companyList":[{"id":"3017414172","name":"北京晟煌科技有限公司","type":1},{"id":"23402373","name":"小米科技有限责任公司","type":1}],"party1Str":"\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F23402373' target='_blank'\u003E小米科技有限责任公司\u003C\u002Fa\u003E","party2Str":"\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F3017414172' target='_blank'\u003E北京晟煌科技有限公司\u003C\u002Fa\u003E","province":"北京","publishdate":"2018-10-09","publishpage":"G08","reason":null,"showtxtdate":null,"tmpsaversn":null,"uuid":"8a78c7995c082614ac80fa13a7ad9e7f"}</script><a
        class="pt15 pb15 position-rel sec-c1 block new-border-bottom"
        href="https://m.tianyancha.com/court/23402373/8a78c7995c082614ac80fa13a7ad9e7f"><!--onclick="openPopup(this,'court')">--><div><span class="left-text">刊登日期：</span><span class="sec-c1">2018-10-09</span></div><div class="item-line"><span
            class="left-text">公告类型：</span><span class="sec-c1">裁判文书</span></div><div class="item-line"><span class="left-text">公告人：</span><span class="sec-c1">小米科技有限责任公司</span></div><div class="new-c1 position-abs" style="right: 10px;top: 40%;"><i class="tic tic-angle-right"></i></div></a></div><div><script type="text/html">{"id":4897148,"announce_id":6956881,"bltnno":"3318091900150","bltnstate":null,"bltntype":null,"bltntypename":"裁判文书","caseno":null,"content":"兖州市三合平价手机超市：本院受理小米科技有限责任公司诉兖州市三合平价手机超市侵害商标权纠纷一案，现已审理终结。现依法向你公告送达（2018）鲁08民初14号民事判决书。自公告之日起60日内来本院领取民事判决书，逾期则视为送达。如不服本判决，可在公告期满后15日内向本院递交上诉状及副本，上诉于山东省高级人民法院。逾期本判决即发生法律效力。","courtflag":null,"courtcode":"山东省济宁市中级人民法院","customno":null,"dealgrade":null,"dealgradename":null,"judge":null,"judgephone":"非公示项","mobilephone":"非公示项","party1":"小米科技有限责任公司","party2":"兖州市三合平价手机超市","companyList":[{"id":"23402373","name":"小米科技有限责任公司","type":1}],"party1Str":"\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F23402373' target='_blank'\u003E小米科技有限责任公司\u003C\u002Fa\u003E","party2Str":"兖州市三合平价手机超市","province":"山东","publishdate":"2018-09-27","publishpage":"G66","reason":null,"showtxtdate":null,"tmpsaversn":null,"uuid":"2c702aa5a5d569620fb5d40dc6a5e3ec"}</script><a
        class="pt15 pb15 position-rel sec-c1 block "
        href="https://m.tianyancha.com/court/23402373/2c702aa5a5d569620fb5d40dc6a5e3ec"><!--onclick="openPopup(this,'court')">--><div><span class="left-text">刊登日期：</span><span class="sec-c1">2018-09-27</span></div><div class="item-line"><span
            class="left-text">公告类型：</span><span class="sec-c1">裁判文书</span></div><div class="item-line"><span class="left-text">公告人：</span><span class="sec-c1">小米科技有限责任公司</span></div><div class="new-c1 position-abs" style="right: 10px;top: 40%;"><i class="tic tic-angle-right"></i></div></a></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">300个</span>法院公告</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="302" change-type="court"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(4,this)"

      >4</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(5,this)"

      >5</a></li><li class="pagination-page " style=""><a
        onclick="companyPageChange(6,this)"

      >...</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>61<span>页</span></div></div></div></div></div><!--end法院公告--><!--15失信人--><!--end失信人--><!--16被执行人--><!--end被执行人--><!--17经营异常--><!--end经营异常--><!--18行政处罚--><div><div id="nav-main-punishment" class="header-container"><div class="itemTitle">行政处罚<!--<span>（{{dataItemCount.punishment}}）</span>--></div></div><div id="_container_punish"><div class="limit-2-download hi-show"><div class="content-container"><div><script type="text/html">{"content":"责令当事人停止销售被依法判定为不合格商品的行为，并决定处罚如下：1、罚款278862元；2、没收违法所得7914元。","punishNumber":"京工商朝处字〔2018〕第1322号","name":"小米科技有限责任公司","base":"bj","decisionDate":"2018-06-21","type":"经营者（销售者）在商品（产品）中掺杂、掺假，以假充真，以次充好，或者以不合格商品（产品）冒充合格商品（产品）的","departmentName":"北京市工商行政管理局朝阳分局"}</script><div onclick='openPopup(this,"punishPopup")'><div class="new-c2 mobile-box"><div class="mobile-box-top">公示日期 ：<span
              class="new-c3"> </span></div><div class="mobile-box-middle">决定机关 ：<span
              class="new-c3">北京市工商行政管理局朝阳分局</span></div><div class="mobile-box-bottom">决定书文号 ：<span
              class="new-c3">京工商朝处字〔2018〕第1322号</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mobile-hr"/></div></div><div><script type="text/html">{"content":"责令停止发布违法广告、公开更正。","punishNumber":"京工商海处字〔2017〕第1585号","name":"小米科技有限责任公司","base":"bj","decisionDate":"2017-11-07","type":"广告使用国家级、最高级、最佳等用语","departmentName":"北京市工商行政管理局海淀分局"}</script><div onclick='openPopup(this,"punishPopup")'><div class="new-c2 mobile-box"><div class="mobile-box-top">公示日期 ：<span
              class="new-c3"> </span></div><div class="mobile-box-middle">决定机关 ：<span
              class="new-c3">北京市工商行政管理局海淀分局</span></div><div class="mobile-box-bottom">决定书文号 ：<span
              class="new-c3">京工商海处字〔2017〕第1585号</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mboile-hide-hr"/></div></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">7条</span>行政处罚</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="9" change-type="punish"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>2<span>页</span></div></div></div></div></div><!--end行政处罚--><!--19严重违法--><!--end严重违法--><!--20股权出质--><div><div id="nav-main-equityCount" class="header-container"><div class="itemTitle">股权出质<!--<span>（{{dataItemCount.equityCount}}）</span>--></div></div><div id="_container_equity"><div class="limit-2-download hi-show"><div class="content-container"><div><script type="text/html">{"equityAmount":"18623.099 万元","pledgorStr":"\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fhuman\u002F2048698570-c23402373' target='_blank'\u003E洪锋\u003C\u002Fa\u003E","regDate":1528646400000,"state":"设立","certifNumber":"非公示项","regNumber":"91110108551385082Q_0","pledgee":"小米通讯技术有限公司","companyList":[{"id":"26052156","name":"小米通讯技术有限公司"}],"pledgeeList":[{"id":"26052156","name":"小米通讯技术有限公司"}],"pledgorList":[{"name":"洪锋"}],"base":"bj","pledgor":"洪锋","certifNumberR":"非公示项","pledgeeStr":"\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F26052156' target='_blank'\u003E小米通讯技术有限公司\u003C\u002Fa\u003E"}</script><div onclick='openPopup(this,"equity")'><div class="new-c2 mobile-box"><div class="mobile-box-top">登记编号 ：<span class="new-c3">91110108551385082Q_0</span></div><div class="mobile-box-middle">出质人 ：<span class="new-c3">洪锋</span></div><div class="mobile-box-bottom">质权人 ：<span
              class="new-c3">小米通讯技术有限公司</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mobile-hr"/></div></div><div><script type="text/html">{"equityAmount":"143934.0478 万元","pledgorStr":"\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fhuman\u002F2263357360-c23402373' target='_blank'\u003E雷军\u003C\u002Fa\u003E","regDate":1461081600000,"state":"设立","certifNumber":"非公示项","regNumber":"91110108551385082Q_0","pledgee":"小米通讯技术有限公司","companyList":[{"id":"26052156","name":"小米通讯技术有限公司"}],"pledgeeList":[{"id":"26052156","name":"小米通讯技术有限公司"}],"pledgorList":[{"name":"雷军"}],"base":"bj","pledgor":"雷军","certifNumberR":"非公示项","pledgeeStr":"\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F26052156' target='_blank'\u003E小米通讯技术有限公司\u003C\u002Fa\u003E"}</script><div onclick='openPopup(this,"equity")'><div class="new-c2 mobile-box"><div class="mobile-box-top">登记编号 ：<span class="new-c3">91110108551385082Q_0</span></div><div class="mobile-box-middle">出质人 ：<span class="new-c3">雷军</span></div><div class="mobile-box-bottom">质权人 ：<span
              class="new-c3">小米通讯技术有限公司</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mboile-hide-hr"/></div></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">13条</span>股权出质</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="15" change-type="equity"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>3<span>页</span></div></div></div></div></div><!--end股权出质--><!--21动产抵押--><!--end动产抵押--><!--22欠税公告--><!--end欠税公告--><!--23招投标--><div><div id="nav-main-bidCount" class="header-container"><div class="itemTitle">招投标<!--<span>（{{dataItemCount.bidCount}}）</span>--></div></div><div id="_container_bid"><div class="limit-2-download hi-show"><div class="content-container"><div class="new-c2"><div class="mobile-box-top f16"><a href="https://m.tianyancha.com/bid/5cd9184b935511e7837d6c92bf3b6045"
                                         class=" text-click-color point">陆丰市中医医院发电机组配套设备和视频网络平台建设采购项目（LFCG2016-56）的最低价法成交公告</a></div><div class="mobile-box-middle">采购人 ：<span class="new-c3">陆丰市中医医院</span></div><div class="mobile-box-bottom">发布时间 ：<span
          class="new-c3">2016-09-23</span></div><hr class="mobile-hr"/></div><div class="new-c2"><div class="mobile-box-top f16"><a href="https://m.tianyancha.com/bid/02f9dab0936311e7837d6c92bf3b6045"
                                         class=" text-click-color point">辽宁工程技术大学营销学院实验室设备采购项目中标公告</a></div><div class="mobile-box-middle">采购人 ：<span class="new-c3">无详细信息</span></div><div class="mobile-box-bottom">发布时间 ：<span
          class="new-c3">2016-09-19</span></div><hr class="mboile-hide-hr"/></div></div></div></div></div><!--end招投标--><!--24债券信息--><!--end债券信息--><!--25购地信息--><!--end购地信息--><!--26招聘信息--><div><div id="nav-main-recruitCount" class="header-container"><div class="itemTitle">招聘信息<!-- <span>（{{dataItemCount.recruitCount}}）</span>--></div></div><div id="_container_recruit"><div class="limit-2-download hi-show"></div></div></div><!--end招聘信息--><!--27税务评级--><div><div id="nav-main-taxCreditCount" class="header-container"><div class="itemTitle">税务评级<!--<span>（{{dataItemCount.taxCreditCount}}）</span>--></div></div><div id="_container_taxcredit"><div class="limit-2-download hi-show"><div class="content-container"><div class="new-c2"><div class="mobile-box-top">年份 ：<span class="new-c3">2016</span></div><div class="mobile-box-middle">纳税人识别号 ：<span class="new-c3">110108551385082</span></div><div class="mobile-box-middle">评价单位 ：<span
          class="new-c3">国家税务总局</span></div><div class="mobile-box-middle">纳税信用评级 ：<span class="new-c3">A</span></div><div class="mobile-box-bottom">类型 ：<span class="new-c3">国税</span></div><hr class="mobile-hr"/></div><div class="new-c2"><div class="mobile-box-top">年份 ：<span class="new-c3">2015</span></div><div class="mobile-box-middle">纳税人识别号 ：<span class="new-c3">110108551385082</span></div><div class="mobile-box-middle">评价单位 ：<span
          class="new-c3">国家税务总局</span></div><div class="mobile-box-middle">纳税信用评级 ：<span class="new-c3">A</span></div><div class="mobile-box-bottom">类型 ：<span class="new-c3">国税</span></div><hr class="mboile-hide-hr"/></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">1条</span>税务评级</a></div></div></div></div><!--end税务评级--><!--28抽查检查--><div><div id="nav-main-checkCount" class="header-container"><div class="itemTitle">抽查检查<!--<span>（{{dataItemCount.checkCount}}）</span>--></div></div><div id="_container_check"><div class="limit-2-download hi-show"><div class="content-container"><div ng-repeat="check in companyCheckInfo.items" class="new-c2"><div class="mobile-box-top">检查实施机关 ：<span class="new-c3">市发展改革委</span></div><div class="mobile-box-middle">时间 ：<span class="new-c3">2016-07-15</span></div><div class="mobile-box-middle">结果 ：<span class="new-c3">未按规定公示年报</span></div><div class="mobile-box-bottom"><span class="yellowbox">检查</span></div><hr class="mobile-hr"/></div><div ng-repeat="check in companyCheckInfo.items" class="new-c2"><div class="mobile-box-top">检查实施机关 ：<span class="new-c3">海淀分局</span></div><div class="mobile-box-middle">时间 ：<span class="new-c3">2015-06-25</span></div><div class="mobile-box-middle">结果 ：<span class="new-c3">正常</span></div><div class="mobile-box-bottom"><span class="yellowbox">抽查</span></div><hr class="mboile-hide-hr"/></div></div></div></div></div><!--end抽查检查--><!--29产品信息--><div><div id="nav-main-productinfo" class="header-container"><div class="itemTitle">产品信息<!--<span>（{{dataItemCount.productinfo}}）</span>--></div></div><div id="_container_product"><div class="limit-2-download hi-show"><div class="content-container"><div><script type="text/html">{"classes":"其它","icon":"https:\u002F\u002Fimg.tianyancha.com\u002Fappbk\u002Ficon\u002F9e4bb2a50a246e657122e3afb2dd0ac6.png@!watermark01","name":"米家-精品商城 智能生活","filterName":"米家","uuid":"1f11ab9b525c345a70095ce56dc2ebfc","type":"应用","brief":"米家App是你家里的智能硬件管理平台，通过米家App，你可以完成手机与智能硬件之间便捷快速的交互，并实现智能设备之间的互联互通。\n通过米家App，你还可以获得智能家庭的酷玩资讯，完成高品质智能硬件的轻松选购。\n你与智能生活，只差一个米家App的距离。\n\nl 联动操控，轻松易用\n可快速掌握的设备添加与操作，实现智能设备间互联互通\nl 个性定制，随你喜好\n按照自己的使用习惯，设置个性化的智能场景\nl 设备分享，乐趣传递\n分享设备给家人朋友，共同感受科技乐趣\nl 有品商城，精品优选\n层层甄选的科技范与性价比，给你品质生活\n\n【联系我们】\n每一次进步都离不开用户的关注和支持，非常期待你的各种点赞和吐槽。想了解米家的更多信息，欢迎关注：\n官方微博：@米家App"}</script><!--<div onclick='openPopup(this,"product")'>--><a class="block" href="https://m.tianyancha.com/product/1f11ab9b525c345a70095ce56dc2ebfc"><div class="mobile-img-box vertival-middle"><img class="w100" src="https://img.tianyancha.com/appbk/icon/9e4bb2a50a246e657122e3afb2dd0ac6.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'" alt="米家-精品商城 智能生活"/></div><div class="new-c2 mobile-img-middle"><div class="mobile-box-top"><span class="new-c3">米家-精品商城 智能生活</span></div><div class="mobile-box-middle"><span class="">类型 ：</span><span
              class="new-c3">应用</span></div></div><div class="mobile-img-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mobile-hr"/></a></div><div><script type="text/html">{"classes":"其它","icon":"https:\u002F\u002Fimg.tianyancha.com\u002Fappbk\u002Ficon\u002F0712ceef311076123fa95db576653a3c.png@!watermark01","name":"小米运动","filterName":"小米运动","uuid":"8d0a0cdab14cbe5a384239bfbb0e3108","type":"应用","brief":"小米运动为你提供精准的运动记录，丰富的健身训练视频，详细的睡眠及运动分析。激励你爱上运动，享受积极健康的生活方式，迎接更加美好的自己。\n\n\n• 连接多种智能设备\n支持小米手环、米动手表青春版、小米体脂秤、小米体重秤、AMAZFIT运动手表、米动智芯等智能设备；\n\n• 精准记录每次运动\n支持跑步、骑行、健走和丰富的减脂、塑型等健身训练内容；\n每次运动都能获得专业的运动姿态和心率分析，让运动更加科学有效；\n\n• 贴心的睡眠管家\n深入分析影响睡眠质量的各种因素，并给出改善建议；\n\n• 全面评测身体状态\n通过小米体脂秤检测10项身体成分数据，让减肥更科学，同时也更早发现影响身体健康的风险；\n\n• 丰富的贴身提醒\n无声闹钟振动唤醒自己，无需打扰枕边人；\n来电、短信、微信、QQ、邮件等各种贴身提醒，不错过每一个重要信息；\n久坐提醒时刻关注你的健康，远离长期久坐给身体带来的伤害；\n\n• 发现更多乐趣\n米动圈分享我的每一次运动，还可以上首页推荐哦；\n报名线上活动随时随地大家一起动；\n精选商城让资深装备控为你选装备。\n\n温馨提示： \n- 本应用支持 Apple 「健康」 应用，授权后可以将你的步数、睡眠、心率等健康数据同步到 「健康」应用\n- 持续运行 GPS 在后台可能会降低你的电池续航时间"}</script><!--<div onclick='openPopup(this,"product")'>--><a class="block" href="https://m.tianyancha.com/product/8d0a0cdab14cbe5a384239bfbb0e3108"><div class="mobile-img-box vertival-middle"><img class="w100" src="https://img.tianyancha.com/appbk/icon/0712ceef311076123fa95db576653a3c.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'" alt="小米运动"/></div><div class="new-c2 mobile-img-middle"><div class="mobile-box-top"><span class="new-c3">小米运动</span></div><div class="mobile-box-middle"><span class="">类型 ：</span><span
              class="new-c3">应用</span></div></div><div class="mobile-img-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mboile-hide-hr"/></a></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">7条</span>产品信息</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="9" change-type="product"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>2<span>页</span></div></div></div></div></div><!--end产品信息--><!--30资质证书--><!--end资质证书--><!--31商标信息--><div><div id="nav-main-tmCount" class="header-container"><div class="itemTitle">商标信息<!--<span>（{{dataItemCount.tmCount}}）</span>--></div></div><div id="_container_tmInfo"><div class="limit-2-download hi-show"><div class="content-container"><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/8a69a4d8538ad1399b6573e573c26972.jpg" alt=""
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-09-12</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3"> </span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">33487510</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">8-手动机械</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">商标注册申请---申请收文</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/375f1a291d1bb9def73734ea27e1f19d.jpg" alt="POCO"
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-09-06</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3">POCO</span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">33350786</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">8-手动机械</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">商标注册申请---申请收文</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/1e0ca784704da0b9a31a73bf9c59ca25.jpg" alt="MIUI"
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-07-31</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3">MIUI</span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">32589107</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">1-化工原料试剂</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">申请收文</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/194c3f3b9193e455b4a9a5831781b360.jpg" alt=""
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-07-27</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3"> </span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">32542034</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">6-金属材料器具</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">申请收文</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/76489f3c5281ea332c6851793c8ada1c.jpg" alt="米兔"
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-07-26</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3">米兔</span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">32496368</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">1-化工原料试剂</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">申请收文</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/0177e06fa79baaca3cc8a09398bb6155.jpg" alt="INSTANTSHOT"
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-07-23</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3">INSTANTSHOT</span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">32420729</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">42-科研服务</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">申请收文</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/0d23859dc584a379bbf96537414e385b.jpg" alt=""
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-07-20</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3"> </span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">32375419</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">7-机械设备</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">申请收文</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/64a8b603f9f6329e2fa35a3950ab51d1.jpg" alt="米粒"
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-07-17</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3">米粒</span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">32291776</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">7-机械设备</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">申请收文</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/e67330d514bfb4af7a9edf6e02c4833d.jpg" alt="米家"
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-07-16</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3">米家</span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">32286209</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">7-机械设备</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">申请收文</span></div></div><hr class="mobile-hr"/></div><div class=""><div class="mobile-img-box vertical-top"><img class="w100" src="https://tm-image.tianyancha.com/tm/668fe5370d82679f65d31a5e0f71218f.jpg" alt="米家"
             onerror="this.src='https://static.tianyancha.com/logo/teamMember/ye_def.png'"/></div><div class="new-c2 mobile-img-detail"><div class="mobile-box-top"><span class="">申请日期 ：</span><span
            class="new-c3">2018-07-16</span></div><div class="mobile-box-middle"><span class="">商标名称 ：</span><span
            class="new-c3">米家</span></div><div class="mobile-box-middle"><span class="">注册号 ：</span><span
            class="new-c3">32268598</span></div><div class="mobile-box-middle"><span class="">类别 ：</span><span
            class="new-c3">5-医药制品</span></div><div class="mobile-box-bottom"><span class="">状态 ：</span><span
            class="new-c3">申请收文</span></div></div><hr class="mboile-hide-hr"/></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">3394条</span>商标信息</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="3396" change-type="tmInfo"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(4,this)"

      >4</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(5,this)"

      >5</a></li><li class="pagination-page " style=""><a
        onclick="companyPageChange(6,this)"

      >...</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>680<span>页</span></div></div></div></div></div><!--end商标信息--><!--32专利信息--><div><div id="nav-main-patentCount" class="header-container"><div class="itemTitle">专利信息<!--（<span>{{dataItemCount.patentCount}}</span>）--></div></div><div id="_container_patent"><div class="limit-2-download hi-show"><div class="content-container"><div><script type="text/html">{"mainCatNum":"[ \"H04B5\u002F02\"]","createTime":"1538275862000","pubnumber":"CN104901725B","searchType":"402","appnumber":"CN201510257008","id":"47896485","_type":"62","title":"信号传输设备、定位器、信号传输系统及信号传输方法","patentName":"信号传输设备、定位器、信号传输系统及信号传输方法","connList":["\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F2310007614' target='_blank'\u003E西安海导信息技术有限公司\u003C\u002Fa\u003E","\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F23402373' target='_blank'\u003E小米科技有限责任公司\u003C\u002Fa\u003E"],"applicationTime":"20150519","applicantname":"[ \"西安海导信息技术有限公司\",\"小米科技有限责任公司\"]","patentType":"发明专利","pubDate":"20180921","applicationPublishNum":"CN104901725B","agency":"北京三高永信知识产权代理有限责任公司 11138","uni":"f8d3548c13edf3d15ef56e63b0a16c6b","inventor":"柯元旦","agent":"张所明","applicationPublishTime":"2018-09-21","patentNum":"CN201510257008","allCatNum":"H04B5\u002F02;H04W4\u002F80;H04W4\u002F02;H04W52\u002F02","abstracts":"本公开关于一种信号传输设备、定位器、信号传输系统及信号传输方法，属于监控技术领域。所述信号传输设备包括：低功耗蓝牙组件、功率放大器、射频开关和天线；低功耗蓝牙组件的输出端分别与功率放大器的输入端和射频开关的第一端口电性相连；功率放大器的输出端与射频开关的第一端口电性相连；射频开关的第二端口与天线电性相连；在射频开关处于第一状态时，低功耗蓝牙组件、功率放大器和天线处于工作状态；在射频开关处于第二状态时，低功耗蓝牙组件和天线处于工作状态。本公开可解决通过GSM组件传输位置信号需要消耗大量的电量的问题，可达到节省电量的效果。","address":"710075 陕西省西安市高新区丈八五路高科尚都摩卡4幢1单元18层11810室","uuid":"1e7cfe2502900a6a000aff3bfd0929c1","eventTime":"1537459200000","applicantName":"西安海导信息技术有限公司;小米科技有限责任公司"}</script><!--<div onclick='openPopup(this,"patent")'>--><a class="block" href="https://m.tianyancha.com/patent/1e7cfe2502900a6a000aff3bfd0929c1"><div class="new-c2 mobile-box"><div class="mobile-box-top"><span class="">申请公布日 ：</span><span
              class="new-c3">2018-09-21</span></div><div class="mobile-box-middle"><span class="">专利名称 ：</span><span class="new-c3">信号传输设备、定位器、信号传输系统及信号传输方法</span></div><div class="mobile-box-middle"><span class="">申请号 ：</span><span
              class="new-c3">CN201510257008</span></div><div class="mobile-box-bottom"><span class="">申请公布号 ：</span><span
              class="new-c3">CN104901725B</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mobile-hr"/></a></div><div><script type="text/html">{"mainCatNum":"[ \"G01C21\u002F00\"]","createTime":"1538280947000","pubnumber":"CN105222773B","searchType":"402","appnumber":"CN201510634512","id":"48096642","_type":"62","title":"导航方法及装置","patentName":"导航方法及装置","connList":["\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F23402373' target='_blank'\u003E小米科技有限责任公司\u003C\u002Fa\u003E"],"applicationTime":"20150929","applicantname":"[ \"小米科技有限责任公司\"]","patentType":"发明专利","pubDate":"20180921","applicationPublishNum":"CN105222773B","agency":"北京三高永信知识产权代理有限责任公司 11138","uni":"0c99691eabfdb33fd5cda4203fc6d8ec","inventor":"刘国明","agent":"徐立","applicationPublishTime":"2018-09-21","patentNum":"CN201510634512","allCatNum":"G01C21\u002F00","abstracts":"本公开是关于一种导航方法及装置，属于导航技术领域。所述方法包括：接收目标设备发送的起点信息和终点信息；基于所述起点信息和所述终点信息，获取从起点到达终点的目标路径导航视频；向所述目标设备发送所述目标路径导航视频。本公开通过实时播放目标路径导航视频，使用户可以实时判断目标路径与实际路线是否偏离，提高了导航的准确度。","address":"100085 北京市海淀区清河中街68号华润五彩城购物中心二期13层","uuid":"1e64ad71fed35fa60700014e49d53487","eventTime":"1537459200000","applicantName":"小米科技有限责任公司"}</script><!--<div onclick='openPopup(this,"patent")'>--><a class="block" href="https://m.tianyancha.com/patent/1e64ad71fed35fa60700014e49d53487"><div class="new-c2 mobile-box"><div class="mobile-box-top"><span class="">申请公布日 ：</span><span
              class="new-c3">2018-09-21</span></div><div class="mobile-box-middle"><span class="">专利名称 ：</span><span class="new-c3">导航方法及装置</span></div><div class="mobile-box-middle"><span class="">申请号 ：</span><span
              class="new-c3">CN201510634512</span></div><div class="mobile-box-bottom"><span class="">申请公布号 ：</span><span
              class="new-c3">CN105222773B</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mboile-hide-hr"/></a></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">4998条</span>专利信息</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="5000" change-type="patent"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(4,this)"

      >4</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(5,this)"

      >5</a></li><li class="pagination-page " style=""><a
        onclick="companyPageChange(6,this)"

      >...</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>1000<span>页</span></div></div></div></div></div><!--end专利信息--><!--33著作权--><div><div id="nav-main-cpoyRCount" class="header-container"><div class="itemTitle">著作权<!--（<span>{{dataItemCount.cpoyRCount}}</span>）--></div></div><div id="_container_copyright"><div class="limit-2-download hi-show"><div class="content-container"><div><script type="text/html">{"authorNationality":"小米科技有限责任公司:中国","simplename":"","searchType":"403","uni":"e70c785e11ae49fcd2e50f07da095059","version":"V1.0","id":"1343593","_type":"63","regtime":"1479139200000","publishtime":"1466352000000","connList":["\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F23402373' target='_blank'\u003E小米科技有限责任公司\u003C\u002Fa\u003E"],"regnum":"2016SR330529","catnum":"30100-0000","eventTime":"1479139200000","fullname":"小米移动网上营业厅软件（Android版）"}</script><div onclick='openPopup(this,"copyRight")'><div class="new-c2 mobile-box"><div class="mobile-box-top"><span class="">登记日期 ：</span><span
              class="new-c3">2016-11-15</span></div><div class="mobile-box-middle"><span class="">软件全称 ：</span><span
              class="new-c3">小米移动网上营业厅软件（Android版）</span></div><div class="mobile-box-middle"><span class="">软件简称 ：</span><span
              class="new-c3">未公示</span></div><div class="mobile-box-middle"><span class="">登记号 ：</span><span
              class="new-c3">2016SR330529</span></div><div class="mobile-box-middle"><span class="">分类号 ：</span><span
              class="new-c3">30100-0000</span></div><div class="mobile-box-bottom"><span class="">版本号：</span><span
              class="new-c3">V1.0</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mobile-hr"/></div></div><div><script type="text/html">{"authorNationality":"小米科技有限责任公司:中国","simplename":"","searchType":"403","uni":"58e521cd4bbc87565b5dd3a3541b3210","version":"V1.0","id":"1335089","_type":"63","regtime":"1478534400000","publishtime":"1466352000000","connList":["\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F23402373' target='_blank'\u003E小米科技有限责任公司\u003C\u002Fa\u003E"],"regnum":"2016SR322156","catnum":"30100-0000","eventTime":"1478534400000","fullname":"小米移动网上营业厅软件（iOS版）"}</script><div onclick='openPopup(this,"copyRight")'><div class="new-c2 mobile-box"><div class="mobile-box-top"><span class="">登记日期 ：</span><span
              class="new-c3">2016-11-08</span></div><div class="mobile-box-middle"><span class="">软件全称 ：</span><span
              class="new-c3">小米移动网上营业厅软件（iOS版）</span></div><div class="mobile-box-middle"><span class="">软件简称 ：</span><span
              class="new-c3">未公示</span></div><div class="mobile-box-middle"><span class="">登记号 ：</span><span
              class="new-c3">2016SR322156</span></div><div class="mobile-box-middle"><span class="">分类号 ：</span><span
              class="new-c3">30100-0000</span></div><div class="mobile-box-bottom"><span class="">版本号：</span><span
              class="new-c3">V1.0</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mobile-hr"/></div></div><div><script type="text/html">{"authorNationality":"小米科技有限责任公司:中国","simplename":"","searchType":"403","uni":"d86171162439c89c0ae21b31c1e1aeb0","version":"V1.0","id":"308532","_type":"63","regtime":"1435161600000","publishtime":"1371657600000","connList":["\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F23402373' target='_blank'\u003E小米科技有限责任公司\u003C\u002Fa\u003E"],"regnum":"2015SR115578","catnum":"30100-0000","eventTime":"1435161600000","fullname":"小米商城软件"}</script><div onclick='openPopup(this,"copyRight")'><div class="new-c2 mobile-box"><div class="mobile-box-top"><span class="">登记日期 ：</span><span
              class="new-c3">2015-06-25</span></div><div class="mobile-box-middle"><span class="">软件全称 ：</span><span
              class="new-c3">小米商城软件</span></div><div class="mobile-box-middle"><span class="">软件简称 ：</span><span
              class="new-c3">未公示</span></div><div class="mobile-box-middle"><span class="">登记号 ：</span><span
              class="new-c3">2015SR115578</span></div><div class="mobile-box-middle"><span class="">分类号 ：</span><span
              class="new-c3">30100-0000</span></div><div class="mobile-box-bottom"><span class="">版本号：</span><span
              class="new-c3">V1.0</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mobile-hr"/></div></div><div><script type="text/html">{"authorNationality":"小米科技有限责任公司:中国","simplename":"","searchType":"403","uni":"7b96f7aca33a7da4feb1c7d9607ec970","version":"V1.0","id":"811747","_type":"63","regtime":"1388073600000","publishtime":"1383148800000","connList":["\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F23402373' target='_blank'\u003E小米科技有限责任公司\u003C\u002Fa\u003E"],"regnum":"2013SR159136","catnum":"30104-6100","eventTime":"1388073600000","fullname":"小米小说软件（for Android版）"}</script><div onclick='openPopup(this,"copyRight")'><div class="new-c2 mobile-box"><div class="mobile-box-top"><span class="">登记日期 ：</span><span
              class="new-c3">2013-12-27</span></div><div class="mobile-box-middle"><span class="">软件全称 ：</span><span
              class="new-c3">小米小说软件（for Android版）</span></div><div class="mobile-box-middle"><span class="">软件简称 ：</span><span
              class="new-c3">未公示</span></div><div class="mobile-box-middle"><span class="">登记号 ：</span><span
              class="new-c3">2013SR159136</span></div><div class="mobile-box-middle"><span class="">分类号 ：</span><span
              class="new-c3">30104-6100</span></div><div class="mobile-box-bottom"><span class="">版本号：</span><span
              class="new-c3">V1.0</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mobile-hr"/></div></div><div><script type="text/html">{"authorNationality":"小米科技有限责任公司:中国","simplename":"","searchType":"403","uni":"77676d6ab19a95c6da5df1304392f63b","version":"V1.0","id":"853446","_type":"63","regtime":"1383148800000","publishtime":"1358524800000","connList":["\u003Ca href='https:\u002F\u002Fwww.tianyancha.com\u002Fcompany\u002F23402373' target='_blank'\u003E小米科技有限责任公司\u003C\u002Fa\u003E"],"regnum":"2013SR116591","catnum":"30100-0000","eventTime":"1383148800000","fullname":"小米手机助手软件"}</script><div onclick='openPopup(this,"copyRight")'><div class="new-c2 mobile-box"><div class="mobile-box-top"><span class="">登记日期 ：</span><span
              class="new-c3">2013-10-31</span></div><div class="mobile-box-middle"><span class="">软件全称 ：</span><span
              class="new-c3">小米手机助手软件</span></div><div class="mobile-box-middle"><span class="">软件简称 ：</span><span
              class="new-c3">未公示</span></div><div class="mobile-box-middle"><span class="">登记号 ：</span><span
              class="new-c3">2013SR116591</span></div><div class="mobile-box-middle"><span class="">分类号 ：</span><span
              class="new-c3">30100-0000</span></div><div class="mobile-box-bottom"><span class="">版本号：</span><span
              class="new-c3">V1.0</span></div></div><div class="mobile-modal-btn"><i class="tic tic-angle-right" aria-hidden="true"></i></div><hr class="mboile-hide-hr"/></div></div></div><div class="ml15 mr15 pt12 pb12 text-center  hi-hide"><a class="text-center download-company-type change1018"
     href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&channelCode=WAP09">下载APP，查看剩余<span class="unit">12条</span>著作权</a></div><div class="company_mobile_pager clearfix new-border-top pt15 pb15 ml15 mr15"><ul class="pagination-sm pagination" boundary-links="false" rotate="false" style="float: left;"
      page-total="14" change-type="copyright"><li class="pagination-prev  disabled" style=""><a

      >&lt;</a></li><li class="pagination-page  active " style=""><a

      >1</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(2,this)"

      >2</a></li><li class="pagination-page   " style=""><a
        onclick="companyPageChange(3,this)"

      >3</a></li><li class="pagination-next  "><a
        onclick="companyPageChange(2,this)"

      >&gt;</a></li></ul><div class="total"><span>共</span>3<span>页</span></div></div></div></div></div><!--end著作权--><!--34网站备案--><div><div id="nav-main-icpCount" class="header-container"><div class="itemTitle">网站备案<!--（<span>{{icpInfo.length?icpInfo.length:'0'}}</span>）--></div></div><div id="_container_icp"><div class="limit-2-download hi-show"><div class="content-container"><div ng-repeat="icp in icpInfo |limitTo:5:icpIndex*5" class=""><!--<div class="new-c2 mobile-box">--><div class="mobile-box-top">审核日期 ：<span class="new-c3">2017-12-18</span></div><div class="mobile-box-middle">网站名称 ：<span class="new-c3">小米推送</span></div><div class="mobile-box-middle">网站首页 ：<a class="overflow-width text-click-color in-block vertival-middle website-over"
           href="http://www.mipush.com"
           target="_blank">www.mipush.com</a></div><div class="mobile-box-middle">域名 ：<span class="new-c3">mipush.com</span></div><div class="mobile-box-middle">备案号 ：<span class="new-c3">京ICP备10046444号</span></div><div class="mobile-box-middle">单位性质 ：<span class="new-c3">企业</span></div><div class="mobile-box-bottom">状态 ：<span class="new-c3">正常</span></div><hr class="mobile-hr"/></div><div ng-repeat="icp in icpInfo |limitTo:5:icpIndex*5" class=""><!--<div class="new-c2 mobile-box">--><div class="mobile-box-top">审核日期 ：<span class="new-c3">2017-12-18</span></div><div class="mobile-box-middle">网站名称 ：<span class="new-c3">脸图</span></div><div class="mobile-box-middle">网站首页 ：<a class="overflow-width text-click-color in-block vertival-middle website-over"
           href="http://www.facephoto.com"
           target="_blank">www.facephoto.com</a></div><div class="mobile-box-middle">域名 ：<span class="new-c3">facephoto.com</span></div><div class="mobile-box-middle">备案号 ：<span class="new-c3">京ICP备10046444号</span></div><div class="mobile-box-middle">单位性质 ：<span class="new-c3">企业</span></div><div class="mobile-box-bottom">状态 ：<span class="new-c3">正常</span></div><hr class="mobile-hr"/></div><!--<div class="company_mobile_pager clearfix new-border-top pt15 pb15" ng-if="ceil(icpTotal/company.icpListpage)>1">--><!--<uib-pagination previous-text="<" next-text=">" items-per-page="5" ng-change="icpChange(icpCurrentPage);" total-items="icpTotal" ng-model="icpCurrentPage" max-size="5" class="pagination-sm" boundary-links="false" rotate="false" style="float:left"></uib-pagination>--><!--<div class="total" ><span>共</span>{{ceil(icpTotal/5);}}<span>页</span></div>--><!--</div>--></div></div></div></div><!--end网站备案--><!--历史信息--><div class="hi-hide"><div id="nav-main-past" class="header-container "><div class="itemTitle">历史信息<!--（<span>{{icpInfo.length?icpInfo.length:'0'}}</span>）--><a class="float-right" href="https://m.tianyancha.com/graphtimeinfo">案例预览</a></div></div><div class=""><a class="change1018"
         href="https://app.tianyancha.com/channel?from=companyDetail&param1=23402373&param2=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&channelCode=WAP17"
         style="display:block;"><img style="width:100%;"
                                     src="https://static.tianyancha.com/wap-require-js/public/images/company_history_0511.png"/></a></div></div><!--历史信息--><!--新闻动态--><div><div id="_container_news"></div></div><div class="b-c-gray pt15"><div class="pl15 pr15 over-hide  b-c-white"><div class="text-center f16 new-c1 pt20 pb20">热点维度</div><a href="https://m.tianyancha.com/companies" class="float-left mb15" style="width: calc(50% - 5px);"><img src="https://static.tianyancha.com/wap/images/wap_seo1.png" width="100%" alt="企业名录"></a><a href="https://m.tianyancha.com/humans" class="float-right mb15" style="width: calc(50% - 5px);"><img src="https://static.tianyancha.com/wap/images/wap_seo2.png" width="100%" alt="人员名录"></a><a href="https://m.tianyancha.com/brands/b-1201101" class="float-left mb15" style="width: calc(50% - 5px);"><img src="https://static.tianyancha.com/wap/images/wap_seo3.png" width="100%" alt="品牌名录"></a><a href="https://m.tianyancha.com/company500" class="float-right mb15" style="width: calc(50% - 5px);"><img src="https://static.tianyancha.com/wap/images/wap_seo4.png" width="100%" alt="500强名录"></a><a href="https://m.tianyancha.com/tax" class="float-left mb15" style="width: calc(50% - 5px);"><img src="https://static.tianyancha.com/wap-require-js/public/images/wap_shuihao_0524.png" width="100%"
           alt="税号查询"></a></div></div><div class="b-c-gray pt15"><div class="  b-c-white  pl10 pr15 b-c-white"><div class="pt15 pl10"><span style="color:#828282;" class="f16">新注册企业</span></div><div><ul class='pt5 pb15 mb0' style="padding-left:0px;text-align: left;list-style:none;"><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/3236388582" title="东莞市廷威电子有限公司"><span
              class="point-icon"></span>东莞市廷威电子有限公司</a><div class="seo-new-reg company_item pl10 pb3">法定代表人：瞿吉有</div></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/3236380523" title="深圳市深大新产业发展有限公司哈尔滨分公司"><span
              class="point-icon"></span>深圳市深大新产业发展有限公司哈尔滨分公司</a><div class="seo-new-reg company_item pl10 pb3">法定代表人：沈沾俊</div></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/3236319272" title="淮北汤姆猫欢乐水世界有限公司"><span
              class="point-icon"></span>淮北汤姆猫欢乐水世界有限公司</a><div class="seo-new-reg company_item pl10 pb3">法定代表人：徐伟</div></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/3236309163" title="合肥企振房屋拆除有限公司"><span
              class="point-icon"></span>合肥企振房屋拆除有限公司</a><div class="seo-new-reg company_item pl10 pb3">法定代表人：王张振</div></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/3236282808" title="东莞市楠信建筑材料有限公司"><span
              class="point-icon"></span>东莞市楠信建筑材料有限公司</a><div class="seo-new-reg company_item pl10 pb3">法定代表人：李发益</div></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/3236260205" title="宝清县靓尚服装销售有限公司"><span
              class="point-icon"></span>宝清县靓尚服装销售有限公司</a><div class="seo-new-reg company_item pl10 pb3">法定代表人：刘洪千</div></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/3236236796" title="宝清县建虹建材经销有限公司"><span
              class="point-icon"></span>宝清县建虹建材经销有限公司</a><div class="seo-new-reg company_item pl10 pb3">法定代表人：夏佩忠</div></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/3236227303" title="宝清县颗金粮食购销有限公司"><span
              class="point-icon"></span>宝清县颗金粮食购销有限公司</a><div class="seo-new-reg company_item pl10 pb3">法定代表人：杨立国</div></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/3235867566" title="上海鸽轩餐饮管理有限公司"><span
              class="point-icon"></span>上海鸽轩餐饮管理有限公司</a><div class="seo-new-reg company_item pl10 pb3">法定代表人：王林山</div></li></ul></div></div><div class="pb15"></div></div><div class="b-c-gray pb15"><div class="  b-c-white  pl10 pr15 b-c-white"><div class="pt15 pl10"><span style="color:#828282;" class="f16">同地区同行业公司</span></div><div><ul class='pt5 pb15 mb0' style="padding-left:0px;text-align: left;list-style:none;"><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/88644174" title="北京北城思通科技有限公司"><span
              class="point-icon"></span>北京北城思通科技有限公司</a><!--<div class="seo-new-reg company_item pl10 pb3" >法定代表人：</div>--></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/550199311" title="蓝鸥科技有限公司"><span
              class="point-icon"></span>蓝鸥科技有限公司</a><!--<div class="seo-new-reg company_item pl10 pb3" >法定代表人：</div>--></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/1152008" title="中德索罗门自行车（北京）有限责任公司"><span
              class="point-icon"></span>中德索罗门自行车（北京）有限责任公司</a><!--<div class="seo-new-reg company_item pl10 pb3" >法定代表人：</div>--></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/24868485" title="北京华诚置伟科技有限公司"><span
              class="point-icon"></span>北京华诚置伟科技有限公司</a><!--<div class="seo-new-reg company_item pl10 pb3" >法定代表人：</div>--></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/2358914891" title="国晟和安（北京）防务科技有限公司"><span
              class="point-icon"></span>国晟和安（北京）防务科技有限公司</a><!--<div class="seo-new-reg company_item pl10 pb3" >法定代表人：</div>--></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/526430367" title="中辆新能源轨道交通装备有限公司"><span
              class="point-icon"></span>中辆新能源轨道交通装备有限公司</a><!--<div class="seo-new-reg company_item pl10 pb3" >法定代表人：</div>--></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/19650455" title="北京市豪鑫信息咨询公司"><span
              class="point-icon"></span>北京市豪鑫信息咨询公司</a><!--<div class="seo-new-reg company_item pl10 pb3" >法定代表人：</div>--></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/5625108" title="北京科利源热电有限公司"><span
              class="point-icon"></span>北京科利源热电有限公司</a><!--<div class="seo-new-reg company_item pl10 pb3" >法定代表人：</div>--></li><li class="pt5"><a class="near_company_list_href company_item" style="width:100%;"
             href="https://m.tianyancha.com/company/15530032" title="北京蓝天瑞德环保技术股份有限公司"><span
              class="point-icon"></span>北京蓝天瑞德环保技术股份有限公司</a><!--<div class="seo-new-reg company_item pl10 pb3" >法定代表人：</div>--></li></ul></div></div></div><!--end新闻动态--><input type="text" id="_companyId" style="display: none;" value="23402373"/><input type="text" id="_companyName" style="display: none;" value="小米科技有限责任公司"/></div><div class="backToTop" onclick="backToTop.backToTop()"><div class="image"></div></div><div class="footerV2"><div class="footer1"><a href="https://m.tianyancha.com/property/1" rel="nofollow">我们</a>&nbsp;&nbsp;<span style="font-size:8px;">●</span>&nbsp;&nbsp;<a href="https://m.tianyancha.com/property/2" rel="nofollow">说明</a>&nbsp;&nbsp;<span style="font-size:8px;">●</span>&nbsp;&nbsp;<a href="https://m.tianyancha.com/property/3" rel="nofollow">版权</a>&nbsp;&nbsp;<span style="font-size:8px;">●</span>&nbsp;&nbsp;<a href="https://m.tianyancha.com/property/6" rel="nofollow">反馈</a>&nbsp;&nbsp;</div><div class="footer2 text-center footer_images_beian"><img class="" src="https://img2.tianyancha.com/beianicon.gif?_t=153829261db11" alt="." style="opacity: 0"><span>&nbsp;京ICP备14061319&nbsp;</span><span>&nbsp;增值电信业务经营许可证：京B2-20181511&nbsp;</span><br>©2018 TIANYANCHA</div></div></div><script>
  var gdt_tracker = gdt_tracker || [];
  gdt_tracker.push(["set_source_id", "33937"]);
  (function () {
    var userAgent = navigator.userAgent;
    if (userAgent.indexOf('ignore') < 0) {
      var doc = document, h = doc.getElementsByTagName("head")[0], s = doc.createElement("script");
      s.async = true;
      s.src = "https://qzs.qq.com/qzone/biz/res/gt.js";
      h && h.insertBefore(s, h.firstChild)
    }
  })();
</script><script>

  var _hmt = _hmt || [];
  (function () {
    var userAgent = navigator.userAgent;
    if (userAgent.indexOf('ignore') < 0) {
      var hm = document.createElement("script");
      hm.src = "//hm.baidu.com/hm.js?d5ceb643638c8ee5fbf79d207b00f07e";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    }
  })();

</script><script>

  (function () {
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
      bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
      bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
  })();

</script><script type="application/ld+json">

    {"@context":"https://zhanzhang.baidu.com/contexts/cambrian.jsonld","@id":"https://m.tianyancha.com/company/23402373","appid":"1559462363285617","title":"小米科技有限责任公司_工商信息_信用报告_财务报表_电话地址查询-天眼查","images":["https://img.tianyancha.com/logo/lll/ad2d5c009059ae43dae809065ad5d8cd.png@!f_200x200"],"description":"天眼查为您提供小米科技有限责任公司工商信息查询、注册信息查询、企业信用报告、财务报表查询、电话地址查询、招聘信息等企业信息查询服务,了解小米科技有限责任公司股东法人、经营状况、商业关系等详细信息,就到天眼查官网！","pubDate":"2010-03-03T00:00:00","upDate":"2018-09-29T02:01:51"}


</script><script async src="https://www.googletagmanager.com/gtag/js?id=UA-123487620-1"></script><script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-123487620-1');
</script></body></html>"""

    def parse(self,resp=None):
        if resp is None:
            postData = {
                'html': self.html,
                'sid': 'tianyancha_xy',
            }
            response = requests.post(self.url, data=postData)
            response = json.loads(response.text)
        else:
            with open('tianyancha.txt','r') as r:
                response = r.read()
                response = json.loads(response)
        try:
            title = response.get('title').get('text')
            gudongxinxi = [' '.join(_[0][1]) + ' '+''.join(_[1][0]) + ' ' + ''.join(_[1][1])
                           for _ in response.get('id_s').get('personner_wapper')[0].get('textDict')[0][0][1][0][0]]
            dongshixinxi = [' '.join(_[0][1]) + ''.join(_[1][0])
                           for _ in response.get('id_s').get('personner_wapper')[0].get('textDict')[0][1][1][0][0]]
            gudongxinxi_etc = [' '.join(_[0]) + ' ' + ''.join(_[1][0]) + ''.join(_[1][1])
                               for _ in response.get('id_s').get('_container_holder')[0].get('textDict')[0][0]]
            zhuyaorenyuan = [_[0] + ''.join(_[2]) for _ in response.get('id_s').get('_container_staff')[0].get('textDict')[0][0]]
            duiwaitouzi = [_ for _ in response.get('id_s').get('_container_invest')[0].get('textDict')[0][0]]

            rongzi = response.get('id_s').get('_container_rongzi')[0].get('textDict')
            hexintuandui = response.get('id_s').get('_container_teamMember')[0].get('textDict') #不全
            qiyeyewu = response.get('id_s').get('_container_firmProduct')[0].get('textDict')
            touzishijian = response.get('id_s').get('_container_touzi')[0].get('textDict')
            jingpinxinxi = response.get('id_s').get('_container_jingpin')[0].get('textDict')
            falvsusong = response.get('id_s').get('_container_lawsuit')[0].get('textDict')
            fayuangonggao = response.get('id_s').get('_container_court')[0].get('textDict')
            xingzhengchufa = response.get('id_s').get('_container_punish')[0].get('textDict')
            guquanchuzhi = response.get('id_s').get('_container_equity')[0].get('textDict')
            zhaotoubiao = response.get('id_s').get('_container_bid')[0].get('textDict')
            shuiwupingji = response.get('id_s').get('_container_taxcredit')[0].get('textDict')
            chouchajiancha = response.get('id_s').get('_container_check')[0].get('textDict')
            #产品信息获取失败
            shangbiaoxinxi = response.get('id_s').get('_container_tmInfo')[0].get('textDict')
            zhuanlixinxi = response.get('id_s').get('_container_patent')[0].get('textDict')
            zhuzuoquan = response.get('id_s').get('_container_copyright')[0].get('textDict')
            wangzhanbeian = response.get('id_s').get('_container_icp')[0].get('textDict')
            #新闻 产品信息 企业年报 分支机构 股权结构 企业关系 基本信息
            # print(title)
            pprint(duiwaitouzi)
            # pprint(gudongxinxi)
            # print(zhuyaorenyuan)
            # print(duiwaitouzi)
            # print(rongzi)
            # print(hexintuandui)
            # print(qiyeyewu)
            # print(touzishijian)
            # print(jingpinxinxi)
            # print(falvsusong)
            # print(fayuangonggao)

        except TypeError as error:
            print(error)
            exit()

    def tianyancha_save(self):
        postData = {
            'html': self.html,
            'sid': 'qichacha_xy',
        }
        response = requests.post(self.url, data=postData)
        print(response.text)
        # with open('tianyancha.txt', 'w') as w:
        #     w.write(response.text)



# createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
jiexi = JieXi()
jiexi.parse(resp=1)

# for _ in range(30):
#     t1 = Thread(target=jiexi.tianyancha_save,)
#     t1.setDaemon(True)
#     t1.start()
# t1.join()
