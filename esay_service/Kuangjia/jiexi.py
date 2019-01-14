# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from CompanyBean import CompanyBean
from pprint import pprint
import re
import urllib.parse
import datetime
import json
import requests
from gongju import format_headers

html = """

<!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,Chrome=1"> <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no"> <meta name="renderer" content="webkit"> <meta name="author" content="leslie"> <title>深圳市比一比网络科技有限公司_杜卫红【工商信息_电话地址_注册信息_信用信息_财务信息】查询_企查查</title> <meta name="keywords" content="深圳市比一比网络科技有限公司,深圳市比一比网络科技有限公司工商信息,深圳市比一比网络科技有限公司招聘,深圳市比一比网络科技有限公司地址电话,深圳市比一比网络科技有限公司怎么样,深圳市比一比网络科技有限公司工资待遇,深圳市比一比网络科技有限公司信用信息"> <meta name="description" content="深圳市比一比网络科技有限公司怎么样？企查查为您提供深圳市比一比网络科技有限公司的最新工商信息、诉讼信息、电话号码、招聘信息、公司简介、公司地址、公司规模、信用信息、财务信息等详细信息，让您在选择深圳市比一比网络科技有限公司前能够做到全面了解深圳市比一比网络科技有限公司的信用信息。"> <meta name="applicable-device" content="pc"> <link rel="alternate" media="only screen and(max-width: 640px)" href="https://m.qichacha.com/firm_182249d7736fdb68960201022c19647a.html" > <link rel="icon" href="/material/theme/chacha/cms/v2/images/favicon.png"> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/bootstrap.css" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/font-awesome.min.css" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/icon.css" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/font.css" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/app.css?time=20181109" type="text/css" /> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/common.css?time=20181109" type="text/css" /> <!--[if lt IE 9]>
    <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/app_ie8.css?time=1508428800" type="text/css" />
    <script src="/material/theme/chacha/cms/v2/js/html5shiv.js"></script>
    <script src="/material/theme/chacha/cms/v2/js/respond.js"></script>
    <![endif]--> <script type="text/javascript" src="/material/js/siteconfig.js"></script> <script src="/material/theme/chacha/cms/v2/js/jquery.min.js"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/qrcode.min.js"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/jquery.scrollTo.js"></script> <script src="/material/theme/chacha/cms/v2/js/bootstrap.js"></script> <script type="text/javascript" src="/material/js/echarts.min.js"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/china.js?time=1508428800"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/chartsUtil.js?time=20181109"></script> <script src="/material/theme/chacha/cms/v2/js/slimscroll/jquery.slimscroll.min.js"></script> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/toastr.css" /> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/moment.js"></script> <script src="/material/theme/chacha/cms/v2/js/toastr.js" type="text/javascript"></script> <script src="/material/theme/chacha/cms/v2/js/custom.js?time=20181109"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/zhuge.js?time=20181109"></script> <script type="text/javascript">
    </script> <script type="text/javascript">
        var qrcodePolling = false;
    </script> </head> <body> <header class="header navi-header box-shadow"> <div class="container "> <div class="navi-brand"> <a onclick="zhugeTrack('主页-顶部-logo');" href="/" > <img src="/material/theme/chacha/cms/v2/images/logo4.png" class="m-r-sm" alt="企查查"> </a> </div> <form class="navi-form" role="search" action="/search"> <div class="form-group"> <div class="input-group"> <input id="headerKey" name="key" onkeydown="searchKeydown(event,2);" class="form-control headerKey" style="font-size: 14px;" type="text" placeholder="请输入企业名称、人名，产品名等，多关键词用空格隔开，如“小米 雷军”" value="" autocomplete="off"> <span class="input-group-btn" style="float: left"> <button onclick="" type="submit" class="btn btn-primary top-searchbtn"></button> </span> </div> </div> <section class="panel headerKey header-section" id="header-search-list"></section> </form> <script type="text/javascript">
                var pathname_ = window.location.pathname; 
                if(pathname_ == '/search_riskinfo' || pathname_ == '/search_intellectualinfo'){
                    $('#tpsearch').attr('action', pathname_);
                }
            </script> <ul class="navi-nav pull-right"> <li> <a onclick="zhugeTrack('主页-顶部-APP下载');" href="/app" class="dropdown-toggle header-qrcode">
                    APP下载
                  </a> <section class="dropdown-menu qrcode-box"> <img src="/material/theme/chacha/cms/v2/images/header_qrcode@2x.png?t=2"> </section> </li> <li class="head-line">|</li> <li class=""> <a onclick="zhugeTrack('主页-顶部-VIP服务');" href="/vip">VIP服务</a> </li> <li class="head-line">|</li> <li><a onclick="" href="/user_login">登录</a></li> <li  class="head-line">|</li> <li><a onclick="" href="/user_register">免费注册</a></li> </ul> </div> </header> <script type="text/javascript" src="/material/js/jquery.cookie.js"></script> <script type="text/javascript" src="/material/js/jquery.validate.min.js"></script> <script type="text/javascript" src="/material/js/jquery.form.min.js"></script> <script type="text/javascript" src="/material/js/global.js?t=33"></script> <style type="text/css"> 
    @media (min-width:960px){
        .modal-dialog {
            width: 960px;
            margin: 30px auto;
        }
        #feedModal .modal-dialog,#shareModal .modal-dialog{
            width: 560px;
            margin: 30px auto;
        }
    }
  #fapiao-title{
      display: none;
  }
  .zhuxiao{
        color: #FD485E;
        text-align: center;
        background: #fff;
        padding: 10px;
        margin-top: -
    }
    .zhuxiao span{
        cursor: pointer;
    }
</style> <div class="container p-t" style="position: relative;"> <div class="m-b-sm"> <a href="/" style="color: #888">首页&nbsp;></a> <a href="/g_GD" style="color: #888">广东省企业查询&nbsp;></a> <a href="firm_182249d7736fdb68960201022c19647a.html" style="color: #888">深圳市比一比网络科技有限公司</a> </div> <div class="panel padder n-s nheader b-a" id="company-top"> <div class="row"> <div class="logo"> <div class="imgkuang"> <img src="https://co-image.qichacha.com/CompanyImage/182249d7736fdb68960201022c19647a.jpg?x-oss-process=style/qcc_cmp" alt="深圳市比一比网络科技有限公司" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'"> </div> <div class="m-t-xs"> <a onclick="zhugeTrack('企业主页-认证企业',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn-nrenzheng" href="/company_cert?companykey=182249d7736fdb68960201022c19647a&companyname=%E6%B7%B1%E5%9C%B3%E5%B8%82%E6%AF%94%E4%B8%80%E6%AF%94%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" target="_blank"></a> </div> </div> <div class="content"> <div class="row title"> <h1>深圳市比一比网络科技有限公司</h1> </div> <div class="row tags"> <span class="ntag  text-success ">存续</span> <span><span class="ntag  text-warning tooltip-br" data-trigger="hover" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title=" <span>深圳市一路无忧科技有限公司</span><br> ">曾用名</span></span> <span class="ntag text-primary" data-trigger="click hover" data-toggle="tooltip" data-placement="bottom" title="从事电子与信息技术、生物工程和新医药技术、新材料及应用技术、先进制造技术、航空航天技术、现代农业技术、新能源与高效节能技术、环境保护新技术、海洋工程技术、核应用技术及与上述十大领域配套的相关技术产品等的一种或多种高新技术及其产品的研究开发、生产和技术服务的企业叫做高新企业。">高新技术企业</span> </div> <div class="row"> <span class="fc "> <span class="cdes">电话：</span> <span class="cvlu"> <span style="color: #000;"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                    0755-8832****
                                </a> </span> </span> </span> <span class="cdes">官网：</span> <span class="cvlu webauth"> <i class="icon-safe webauth-i"> <div class="webauth-template"> <div> <div class="col-left"> <div class="name">深圳市比一比网络科技有限公司</div> <div class="info"><span>验证深度：</span> <span class="starts"> <span class="icon_start1"></span> <span class="icon_start1"></span> <span class="icon_start0"></span> <span class="icon_start0"></span> <span class="icon_start0"></span> </span> </div> <div class="info"><span>信誉积累：</span> 1292天</div> <div class="info"><span>有效期限：</span> 2015/04/27~2019/04/27</div> </div> <a target="_blank" rel="nofollow" href="https://v.pinpaibao.com.cn/cert/site/?site=www.beyebe.com" onclick="" class="webauth-gwtb"> <img src="/material/theme/chacha/cms/v2/images/webauth_gwtb2.png"> <span>查看证书</span> </a> <div class="clearfix"></div> <div class="des">通过了经营内容合法性、运营方实名验证、行业经营资质核验、网站安全性评估、网站优质评估等128项审核。</div> <div class="bottom">
        以上认证信息由<a target="_blank" rel="nofollow" href="https://xinyong.yunaq.com/landing?from=qichacha" style="color: #128bed;" onclick="zhugeTrack('企业主页-网站认证-创宇信用');">创宇信用</a>提供
    </div> </div> </div> </i> <a onclick="zhugeTrack('企业主页-查看官网',{'企业名称':'深圳市比一比网络科技有限公司'});" href="http://www.beyebe.com" class="" target="_blank" data-trigger="hover" data-toggle="tooltip" data-placement="right" title="进入官网" data-delay="500" rel="nofollow"> www.beyebe.com </a> <a onclick="zhugeTrack('企业主页-流量分析',{'企业名称':'深圳市比一比网络科技有限公司'});" style="color: #128bed;" class="m-l-xs" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();">流量分析 </a> </span> </div> <div class="row"> <span class="fc "> <span class="cdes">邮箱：</span> <span class="cvlu"> <a onclick="zhugeTrack('企业主页-查看邮箱',{'企业名称':'深圳市比一比网络科技有限公司'});" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                 
                                ***@qq.com
                            </a> </span> </span> <span class="cdes">地址：</span><span class="cvlu"> <a onclick="showMapModal('深圳市南山区粤海街道高新技术园中区科苑大道讯美科技广场1栋3楼306','深圳市');zhugeTrack('企业主页-查看地址',{'企业名称':'深圳市比一比网络科技有限公司'});" data-trigger="hover" data-toggle="tooltip" data-placement="right" title="查看地址" data-delay="500"> 深圳市南山区粤海街道高新技术园中区科苑大道讯美科技广场1栋3楼306</a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-附近公司',{'企业名称':'深圳市比一比网络科技有限公司'});" style="color: #128bed" class="m-l-sm"> 附近公司</a> </span> </div> <div class="row"> <span class="cdes">简介：</span> <span class="cvlu"> 公司为留美博士后和世界500强高管联合创立的高新技术企业，致力于先进技术平台构建，拟于3年内成为行业领军企业，… <a onclick="zhugeTrack('企业主页-查看简介',{'企业名称':$('#companyname').val()});" style="color: #128bed" data-toggle="modal" data-target="#jianjieModal">查看详情</a></span> </div> <div class="row dongtai  "> <a class="oxin" onclick="zhugeTrack('企业主页-查看产品信息',{'企业名称':'深圳市比一比网络科技有限公司'});" href="/product_cead27cc-bcba-42b2-8c61-527d292157c5"> <div class="img"><img src="https://img.qichacha.com/Product/cead27cc-bcba-42b2-8c61-527d292157c5.jpg"></div> <div> <span class="cdes">产品信息：</span> <span class="cvlu">深圳比一比</span> </div> <div> <span class="text-gray">融资历程 <span class="text-primary">0</span></span> <span class="text-gray m-l-xs">竞品数量 <span class="text-primary">20</span></span> </div> </a> <a class="oxin" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-查看股权穿透',{'企业名称':'深圳市比一比网络科技有限公司'});"> <div class="img"><img src="https://co-image.qichacha.com/CompanyImage/182249d7736fdb68960201022c19647a.jpg?x-oss-process=style/qcc_cmp"></div> <div> <span class="cdes">股权穿透</span> </div> <div> <span class="text-gray">挖掘深层股权结构</span> </div> </a> </div> </div> <div class="company-action"> <a onclick="zhugeTrack('企业主页-递名片',{'企业名称':'深圳市比一比网络科技有限公司'});" data-toggle="modal" data-target="#loginModal" class="c_iconDt ca_card"> <span></span>递名片
                </a> <a data-toggle="modal" data-target="#loginModal" onclick="pageAddCompare('182249d7736fdb68960201022c19647a');zhugeTrack('企业主页-对比企业',{'企业名称':'深圳市比一比网络科技有限公司'});" class="c_iconDt ca_compare"> <span></span>对比
                </a> <a id="follow" data-flag="0" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-关注企业',{'企业名称':'深圳市比一比网络科技有限公司'});" class="c_iconDt ca_focus" title="关注公司"> <span></span>关注
                </a> <a href="javascript:;" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-监控企业',{'企业名称':'深圳市比一比网络科技有限公司'});" class="c_iconDt ca_jk"> <span></span>监控
                </a> <a data-trigger="hover" class="pull-right" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="实时监控100家企业、100位老板，含工商、对外投资、司法诉讼、经营风险等全面信息监控，每日9点推送监控日报，不再错过重要情报"><i class="m_question" style="top: 8px;right: -5px;" ></i></a> <p class="m-t" title="上次更新日期：3天前" style="font-size: 15px;color: #444;position: absolute;right: 0px;"> <a class="m_bt_refresh" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-更新数据',{'企业名称':'深圳市比一比网络科技有限公司'});"> </a> 3天前更新
                </p> </div> </div> <div class="company-record"> <span>浏览：3593</span> <a onclick="zhugeTrack('企业主页-认证企业',{'企业名称':'深圳市比一比网络科技有限公司'});" class="text-warning pull-right" href="/company_cert?companykey=182249d7736fdb68960201022c19647a&companyname=%E6%B7%B1%E5%9C%B3%E5%B8%82%E6%AF%94%E4%B8%80%E6%AF%94%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8">编辑企业信息</a> </div> </div> <div class="modal fade" id="jianjieModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="modal-header"> <button class="close" type="button" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="myModalLabel">公司简介</h4> </div> <div class="modal-body"> <div class="m-t-sm m-b-sm"> <p class="mb10 cmp-txtshow" id="textShowMore">公司为留美博士后和世界500强高管联合创立的高新技术企业，致力于先进技术平台构建，拟于3年内成为行业领军企业，重点项目为各类高性能的润滑油（脂、剂）产品，产品性能国内领先，世界一流水平。现诚聘各类人才，如果你足够优秀，将享受“年薪+股权”的事业合伙人待遇。</p> </div> </div> <div class="modal-footer"> <button  type="button" data-dismiss="modal" class="btn btn-primary">确定</button> </div> </div> </div> </div> </div> <div class="container m-t"> <div class="clearfix risk-qingbao"> <div class="risk-panel b-a"> <a data-trigger="hover" class="pull-right" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="自身风险，聚合该公司自身存在的风险信息，其中包含：<br> 警示信息：裁判文书，严重违法，经营异常，行政处罚，税务行政处罚，环保处罚，动产抵押，土地抵押，税收违法，股权冻结，司法拍卖，股权出质，开庭公告；<br> 高风险信息：失信被执行人，被执行人。<br><br> 关联风险，挖掘企业的关联人（如法定代表人，自然人股东，主要人员）和关联公司（如企业股东，投资公司，分公司）风险。其中包含：<br> 关联人风险：失信被执行人和被执行人信息；<br> 关联公司风险：同企业自身风险信息。<br><br>  提示信息，法定代表人变更，大股东变更；<br><br>说明：风险扫描中的数据是基于公开信息通过风险模型大数据分析后的结果，仅供用户参考，并不代表企查查的任何明示、暗示之观点或保证。若因参考、使用该信息造成损失的，由用户自行负责，企查查不承担任何责任。"><i class="m_question"></i></a> <img src="/material/theme/chacha/cms/v2/images/risk_title@2x.png"> <span class="tl"> <a  onclick="showVipModal('风险扫描 只对VIP开放哦');zhugeTrack('企业主页-风险扫描-开通VIP',{'企业名称':'深圳市比一比网络科技有限公司'});">自身风险
                <span class="text-danger">2</span></a> <span class="">关联风险 <span class="text-danger">0</span></span> </span> <a onclick="showVipModal('风险扫描 只对VIP开放哦');zhugeTrack('企业主页-风险扫描-开通VIP',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn btn-danger pull-right">查看风险</a> </div> <div class="qingbao-panel b-a"> <img src="/material/theme/chacha/cms/v2/images/qingbao_title@2x.png"> <a style="margin-left: 42px;" onclick="zhugeTrack('企业主页-情报动态',{'企业名称':'深圳市比一比网络科技有限公司'});" href="/company_intelligence?keyno=182249d7736fdb68960201022c19647a&companyname=深圳市比一比网络科技有限公司"> <span class="m-r">2017-08-09</span>
                        变更
                                    <span class="text-primary">工商信息</span> </a> <a onclick="zhugeTrack('企业主页-情报动态',{'企业名称':'深圳市比一比网络科技有限公司'});" href="/company_intelligence?keyno=182249d7736fdb68960201022c19647a&companyname=深圳市比一比网络科技有限公司" class="btn btn-primary pull-right">查看情报</a> </div> </div> <div class="row"> <div class="col-sm-9 no-padding-right"> <header style="height: 44px;position: relative;"> <div class="company-nav " style="overflow: hidden;"> <div class="company-nav-tab                                                     current 
                        "> <a class="company-nav-head" onclick="" href="/cbase_182249d7736fdb68960201022c19647a"><h2>基本信息</h2> <span>50</span></a> <div class="company-nav-items"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">工商信息 
                                                                <span class="text-primary"></span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">股东信息 
                                                                <span class="text-primary">16</span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">股权穿透图 
                                                                <span class="text-primary"></span> </a> <span>对外投资 <span>0</span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">主要成员 
                                                                <span class="text-primary">3</span> </a> <span>分支机构 <span>0</span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">关联图谱 
                                                                <span class="text-primary"></span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">变更记录 
                                                                <span class="text-primary">29</span> </a> <span>最终受益人 <span>0</span></span> <span>控股公司 <span>0</span></span> <span>财务简析 <span></span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">同业分析 
                                                                <span class="text-primary"></span> </a> </div> </div> <div class="company-nav-tab                                                      
                        "> <a class="company-nav-head" onclick="" href="/csusong_182249d7736fdb68960201022c19647a"><h2>法律诉讼</h2> <span>2</span></a> <div class="company-nav-items"> <span>被执行人 <span>0</span></span> <span>失信信息 <span>0</span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">裁判文书 
                                                                <span class="text-danger">2</span> </a> <span>法院公告 <span>0</span></span> <span>开庭公告 <span>0</span></span> <span>送达公告 <span>0</span></span> <span>司法协助 <span>0</span></span> </div> </div> <div class="company-nav-tab                                                      
                        "> <a class="company-nav-head" onclick="" href="/crun_182249d7736fdb68960201022c19647a"><h2>经营状况</h2> <span>87</span></a> <div class="company-nav-items"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">行政许可 
                                                                <span class="text-primary">2</span> </a> <span>税务信用 <span>0</span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">产品信息 
                                                                <span class="text-primary">1</span> </a> <span>融资信息 <span>0</span></span> <span>招投标 <span>0</span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">招聘 
                                                                <span class="text-primary">80</span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">财务总览 
                                                                <span class="text-primary">1</span> </a> <span>进出口信用 <span>0</span></span> <span>微信公众号 <span>0</span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">新闻舆情 
                                                                <span class="text-primary">2</span> </a> <span>公报研报 <span>0</span></span> <span>地块公示 <span>0</span></span> <span>购地信息 <span>0</span></span> <span>土地转让 <span>0</span></span> <span>债券信息 <span>0</span></span> <span>抽查检查 <span>0</span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">电信许可 
                                                                <span class="text-primary">1</span> </a> </div> </div> <div class="company-nav-tab                                                      
                        "> <a class="company-nav-head" onclick="" href="/cfengxian_182249d7736fdb68960201022c19647a"><h2>经营风险</h2> <span>0</span></a> <div class="company-nav-items"> <span>经营异常 <span>0</span></span> <span>严重违法 <span>0</span></span> <span>股权出质 <span>0</span></span> <span>行政处罚 <span>0</span></span> <span>税收违法 <span>0</span></span> <span>动产抵押 <span>0</span></span> <span>环保处罚 <span>0</span></span> <span>清算信息 <span>0</span></span> <span>司法拍卖 <span>0</span></span> <span>土地抵押 <span>0</span></span> <span>简易注销 <span></span></span> <span>公示催告 <span>0</span></span> <span>欠税公告 <span>0</span></span> </div> </div> <div class="company-nav-tab                                                      
                        "> <a class="company-nav-head" onclick="" href="/creport_182249d7736fdb68960201022c19647a"><h2>企业年报</h2> <span>5</span></a> <div class="company-nav-items"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">2017年度报告 
                                                                <span class="text-primary"></span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">2016年度报告 
                                                                <span class="text-primary"></span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">2015年度报告 
                                                                <span class="text-primary"></span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">2014年度报告 
                                                                <span class="text-primary"></span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">2013年度报告 
                                                                <span class="text-primary"></span> </a> </div> </div> <div class="company-nav-tab                                                      
                        "> <a class="company-nav-head" onclick="" href="/cassets_182249d7736fdb68960201022c19647a"><h2>知识产权</h2> <span>46</span></a> <div class="company-nav-items"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">商标信息 
                                                                <span class="text-primary">8</span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">专利信息 
                                                                <span class="text-primary">6</span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">证书信息 
                                                                <span class="text-primary">1</span> </a> <span>作品著作权 <span>0</span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">软件著作权 
                                                                <span class="text-primary">18</span> </a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">网站信息 
                                                                <span class="text-primary">13</span> </a> </div> </div> <div class="company-nav-tab                                                      
                        "> <a class="company-nav-head" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><h2>历史信息</h2> <span>2</span></a> <div class="company-nav-items"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">工商信息 
                                                                <span class="text-primary"></span> </a> <span>对外投资 <span>0</span></span> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">历史股东 
                                                                <span class="text-primary">1</span> </a> <span>失信信息 <span>0</span></span> <span>被执行人 <span>0</span></span> <span>法院公告 <span>0</span></span> <span>裁判文书 <span>0</span></span> <span>行政处罚 <span>0</span></span> <span>动产抵押 <span>0</span></span> <span>开庭公告 <span>0</span></span> <span>股权出质 <span>0</span></span> <span>行政许可 <span>0</span></span> </div> </div> </div> </header> <a style="display: none;position: absolute;" href="/cinvestment_182249d7736fdb68960201022c19647a">对外投资</a> <a style="display: none;position: absolute;" href="/creport_182249d7736fdb68960201022c19647a">企业年报</a> <a style="display: none;position: absolute;" href="/cjob_182249d7736fdb68960201022c19647a">新闻舆情</a> <div class="data_div_login"> <div class="base_info"></div> <div class="current"><a id="base_title"></a></div> <section class="panel b-a clear m_dataTab"> <div class="panel-body" style="padding-top: 5px;"> <a href="javascript:;" onclick="boxScrollNew('#Cominfo');zhugeTrack('企业主页-基本信息-工商信息',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;">
              工商信息
          </a> <a href="javascript:;" onclick="boxScrollNew('#Sockinfo');zhugeTrack('企业主页-基本信息-股东信息',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;">
                  股东信息&nbsp;16
              </a> <a href="javascript:;" onclick="boxScrollNew('#guquan');zhugeTrack('企业主页-基本信息-股权穿透图',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;">
              股权穿透图
          </a> <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm   c_disable" style="white-space:nowrap;cursor: default">
                  对外投资&nbsp;0
              </a> <a href="javascript:;" onclick="boxScrollNew('#Mainmember');zhugeTrack('企业主页-基本信息-主要成员',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm    m-r-sm" style="white-space:nowrap;">
                  主要成员&nbsp;3
              </a> <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm   c_disable" style="white-space:nowrap;cursor: default">
                  分支机构&nbsp;0
              </a> <a href="javascript:;" onclick="boxScrollNew('#muhou');zhugeTrack('企业主页-基本信息-企业关联图谱',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn btn-sm btn-default  m-t-sm   m-r-sm" style="white-space:nowrap;">
            企业关联图谱&nbsp;
        </a> <a href="javascript:;" onclick="boxScrollNew('#Changelist');zhugeTrack('企业主页-基本信息-变更记录',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm    m-r-sm" style="white-space:nowrap;">
                  变更记录&nbsp;29
              </a> <a href="javascript:;" onclick="boxScrollNew('#Comintroduce');zhugeTrack('企业主页-基本信息-公司简介',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm   m-r-sm" style="white-space:nowrap;">
                  公司简介&nbsp;
              </a> <a href="javascript:;" class="btn btn-sm btn-default m-t-sm m-r-sm c_disable" style="white-space:nowrap;cursor: default">
                  最终受益人&nbsp;0 
              </a> <a href="javascript:;" class="btn btn-sm btn-default m-t-sm m-r-sm c_disable" style="white-space:nowrap;cursor: default">
                  控股企业&nbsp;0 
              </a> <a href="javascript:;" class="btn btn-sm btn-default m-t-sm  m-r-sm c_disable" style="white-space:nowrap;cursor: default">
                  财务简析 
              </a> <a href="javascript:;" onclick="boxScrollNew('#thyfx');zhugeTrack('企业主页-基本信息-同业分析',{'企业名称':'深圳市比一比网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;">
                  同业分析</a> </div> </section> <section class="panel b-a base_info" id="Cominfo"> <div class="tcaption"> <h3 class="title">工商信息</h3> <a onclick="zhugeTrack('企业主页-工商信息-查看工商官网快照',{'企业名称':'深圳市比一比网络科技有限公司'});" class="text-primary kz_anim" href="/snapshoot_182249d7736fdb68960201022c19647a.html" target="_blank">
                查看工商官网快照
            </a> <span class="watermark"></span> </div> <div class="prot-gltu" id="protGltu"></div> <table  class="ntable" style="margin-bottom: -1px;"> <tr> <td width="297" class="tb text-center">
                                                法定代表人信息
                                        </td> <td width="253" class="tb text-center">企业关联图谱<img class="m-l-sm" style="width: 30px;" src="/material/theme/chacha/cms/v2/images/icon_hot@2x.png"></td> <td class="tb text-center">股权结构图</td> </tr> <tr> <td height="180" class=""> <div class="boss-td"> <div class="clearfix" style="height: 76px;padding-top: 8px;overflow: hidden;"> <a href="/pl_pf041011972b479ca0cee915291ab07c.html" class="pull-left bheadimgkuang"> <span class="usericon boss color-2" first-letter="杜"></span> </a> <div class="pull-left" style="max-width: 235px;"> <a href="/pl_pf041011972b479ca0cee915291ab07c.html" class="bname"><h2 class="seo font-20">杜卫红</h2></a> <span class="brenzhi">共任职 <span class="text-danger">1</span> 家企业，主要分布：</span> </div> </div> <div class="ba-table-base"> <div class="province-info"> <div class="clearfix"> <div class="col-xs-4"> <div class="m-t-xs"><span class="icon-place"></span>广东（共<span class="text-danger">1</span>家）</div> </div> <div class="col-xs-8 text-right"> <div class="m-t-xs">
                                        
                                                                                深圳市比一比网络科技有...
                                                                              </div> </div> </div> </div> </div> </div> </td> <td class=""> <div style="height: 108px;text-align: center;cursor:pointer;" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"> <img style="width: 246px;" src="/material/theme/chacha/cms/v2/images/icon_gltp@2x.png"></a> </div> <div class="ba-table-base"><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="btn btn-primary basePageBt">查看详情</a></div> </td> <td class="guquan-static-td"> <div style="height: 108px;overflow: hidden;"> <img src="/material/theme/chacha/cms/v2/images/base_guquan_bg.png"> <div class="text1">深圳市比一比网络科技有限公司</div> <div class="text2">杜卫红</div> <div class="text3">
                      股权比例：<span class="text-warning m-r">23.32%</span> 
                      认缴金额：<span class="text-warning">258.37万元</span> </div> </div> <div data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="mengban"></div> <div class="ba-table-base"><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="btn btn-primary basePageBt">查看详情</a></div> </td> </tr> </table> <table class="ntable"> <tr> <td width="20%" class="tb">注册资本：</td> <td width="30%" class="">
                 1107.7417万元人民币             </td> <td width="20%" class="tb">实缴资本：</td> <td width="30%" class="">
                800万元人民币
            </td> </tr> <tr> <td class="tb">经营状态：</td> <td class="">
                 存续（在营、开业、在册）             </td> <td class="tb" width="18%">成立日期：</td> <td class="">
                2009-01-12
            </td> </tr> <tr> <td class="tb">统一社会信用代码：</td> <td class="">
                9144030068375453XL
            </td> <td class="tb">纳税人识别号：</td> <td class="">
                9144030068375453XL
            </td> </tr> <tr> <td class="tb">注册号：</td> <td class="">
                440301103810509
            </td> <td class="tb" width="15%">组织机构代码：</td> <td class="">
                68375453-X
            </td> </tr> <tr> <td class="tb">公司类型：</td> <td class="">
                有限责任公司
            </td> <td class="tb">所属行业：</td> <td class="">
                制造业
            </td> </tr> <tr> <td class="tb">核准日期：</td> <td class="" style="max-width:301px;">
                2018-11-01
            </td> <td class="tb">登记机关：</td> <td class="">
                深圳市市场监督管理局
            </td> </tr> <tr> <td class="tb">所属地区：</td> <td class="" style="max-width:301px;">
                广东省
            </td> <td class="tb">英文名：</td> <td class="">
                Shenzhen Yiluwuyou Technology Co., Ltd.
            </td> </tr> <tr> <td class="tb">
                曾用名
            </td> <td class=""> <span>深圳市一路无忧科技有限公司&nbsp;&nbsp;</span> </td> <td class="tb">
                参保人数
            </td> <td class="">
                42
            </td> </tr> <tr> <td class="tb">
                人员规模
            </td> <td class="">
                50-99人
            </td> <td class="tb">
                营业期限
            </td> <td class="">
                2009-01-12 至 无固定期限
            </td> </tr> <tr> <td class="tb">企业地址：</td> <td class="" colspan="3">
                 深圳市南山区粤海街道高新技术园中区科苑大道讯美科技广场1栋3楼306
                <a onclick="showMapModal('深圳市南山区粤海街道高新技术园中区科苑大道讯美科技广场1栋3楼306','')" class="m-l text-primary"> 查看地图</a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="m-l text-primary"> 附近公司</a> </td> </tr> <tr> <td class="tb">经营范围：</td> <td class="" colspan="3">
                 计算机软硬件、通讯设备、网络的技术开发和销售,技术咨询;企业管理咨询及其它信息咨询(不含人才中介服务、证券及其它限制项目);代订机票;会议策划;从事广告业务(法律、行政法规规定应进行广告经营审批登记的,另行办理审批登记后方可经营);国内贸易(法律、行政法规、国务院决定规定在登记前须经批准的项目除外)。             </td> </tr> </table> </section> <section class="panel b-a clear m_comInfoList" id="Sockinfo"> <div class="tcaption"> <h3 class="title">股东信息</h3> <span class="tbadge">16</span> <span class="thist">（查看更多1条 <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">历史股东</a>）</span> <span class="watermark"></span> </div> <table class="ntable ntable-odd"> <tr> <th class="tx">序号</th> <th width="">股东（发起人）
                          </th> <th width="90">持股比例</th> <th width="155">认缴出资额(万元)</th> <th width="130">认缴出资日期</th> </tr> <tr> <td class="tx">1</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-9" first-letter="杜"></span> </div> </td> <td> <a href="/pl_pf041011972b479ca0cee915291ab07c.html"><h3 class="seo font-14">杜卫红</h3></a> <img style="margin-left: 5px;margin-top: -5px;width: 44px;" src="/material/theme/chacha/cms/v2/images/dagudong@2x.png"> <div class="m-t-xs"> <span class="ntag sm text-danger m-r-xs">实际控制人</span> </div> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_pf041011972b479ca0cee915291ab07c.html">他关联1家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    23.32%
                </td> <td class="text-center">
                      258.3666                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">2</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-8" first-letter="梁"></span> </div> </td> <td> <a href="/pl_p5a8ef899114677ea39258ce1d927618.html"><h3 class="seo font-14">梁飞鹏</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_p5a8ef899114677ea39258ce1d927618.html">他关联13家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    12.23%
                </td> <td class="text-center">
                      135.497                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">3</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-13" first-letter="崔"></span> </div> </td> <td> <a href="/pl_p3fea0a9bdc30ebb8a1988fe70eba138.html"><h3 class="seo font-14">崔善仁</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_p3fea0a9bdc30ebb8a1988fe70eba138.html">他关联1家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    10.00%
                </td> <td class="text-center">
                      110.7852                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">4</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-1" first-letter="徐"></span> </div> </td> <td> <a href="/pl_p31a8061cd66dffa5249b6d77af11da9.html"><h3 class="seo font-14">徐成</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_p31a8061cd66dffa5249b6d77af11da9.html">他关联8家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    8.68%
                </td> <td class="text-center">
                      96.2                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">5</td> <td> <table class="insert-table"> <tr> <td width="50"> <span class="headimg"> <img src="https://qccdata.qichacha.com/AutoImage/989fd43dc4f1993e430476602dca4477.jpg?x-oss-process=image/resize,w_120"> </span> </td> <td> <a href="/firm_989fd43dc4f1993e430476602dca4477.html" target="_blank"><h3 class="seo font-14">
                            前海路路兴投资管理（深圳）有限公司</h3></a> </td> </tr> </table> </td> <td class="text-center">
                    7.26%
                </td> <td class="text-center">
                      80.4711                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">6</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-7" first-letter="王"></span> </div> </td> <td> <a href="/pl_pr7f1b847e10be21392c7cb2d4f1784e.html"><h3 class="seo font-14">王海荣</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_pr7f1b847e10be21392c7cb2d4f1784e.html">他关联1家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    7.00%
                </td> <td class="text-center">
                      77.5419                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">7</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-7" first-letter="蔡"></span> </div> </td> <td> <a href="/pl_pe28cb0e0fc5b968bf594ecd94087036.html"><h3 class="seo font-14">蔡明星</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_pe28cb0e0fc5b968bf594ecd94087036.html">他关联14家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    5.76%
                </td> <td class="text-center">
                      63.8479                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">8</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-14" first-letter="谢"></span> </div> </td> <td> <a href="/pl_p7f87d7afe9561009a8a4c9122265a16.html"><h3 class="seo font-14">谢立欧</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_p7f87d7afe9561009a8a4c9122265a16.html">他关联3家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    5.05%
                </td> <td class="text-center">
                      55.9684                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">9</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-8" first-letter="叶"></span> </div> </td> <td> <a href="/pl_pr882b2e2ecd35bea830ae13bd226480.html"><h3 class="seo font-14">叶喜光</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_pr882b2e2ecd35bea830ae13bd226480.html">他关联1家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    5.00%
                </td> <td class="text-center">
                      55.3871                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">10</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-9" first-letter="许"></span> </div> </td> <td> <a href="/pl_pf0f32e2b89d7e1f3fe5cf082a3ea06a.html"><h3 class="seo font-14">许健航</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_pf0f32e2b89d7e1f3fe5cf082a3ea06a.html">他关联3家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    3.31%
                </td> <td class="text-center">
                      36.6426                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">11</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-9" first-letter="雷"></span> </div> </td> <td> <a href="/pl_p57156b45e95c64e00f4558ecc45c4d2.html"><h3 class="seo font-14">雷祖云</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_p57156b45e95c64e00f4558ecc45c4d2.html">他关联1家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    2.73%
                </td> <td class="text-center">
                      30.2201                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">12</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-4" first-letter="廉"></span> </div> </td> <td> <a href="/pl_p265b141964bfd56af5001ad576d62ed.html"><h3 class="seo font-14">廉健</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_p265b141964bfd56af5001ad576d62ed.html">他关联17家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    2.40%
                </td> <td class="text-center">
                      26.5956                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">13</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-7" first-letter="章"></span> </div> </td> <td> <a href="/pl_p74903795403c56bd14357ae017d4d7a.html"><h3 class="seo font-14">章莉</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_p74903795403c56bd14357ae017d4d7a.html">他关联3家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    2.21%
                </td> <td class="text-center">
                      24.4474                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">14</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-13" first-letter="储"></span> </div> </td> <td> <a href="/pl_pr86619178967decf03c16add5db68cf.html"><h3 class="seo font-14">储敏健</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_pr86619178967decf03c16add5db68cf.html">他关联1家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    2.00%
                </td> <td class="text-center">
                      22.1548                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">15</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-13" first-letter="李"></span> </div> </td> <td> <a href="/pl_p7a21d3940e6ddc045a24cc74acad02b.html"><h3 class="seo font-14">李崇仁</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_p7a21d3940e6ddc045a24cc74acad02b.html">他关联7家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    1.93%
                </td> <td class="text-center">
                      21.4016                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> <tr> <td class="tx">16</td> <td> <table class="insert-table"> <tr> <td width="50"> <div class="headimg"> <span class="usericon headn color-4" first-letter="钟"></span> </div> </td> <td> <a href="/pl_pe87662246ebb26358d1d98b191cd522.html"><h3 class="seo font-14">钟青</h3></a> </td> <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_pe87662246ebb26358d1d98b191cd522.html">他关联9家公司 > </a> </td> </tr> </table> </td> <td class="text-center">
                    1.10%
                </td> <td class="text-center">
                      12.2144                        <br/> </td> <td class="text-center">
                     -                 </td> </tr> </table> </section> <section class="panel b-a clear guquan-section" id="guquan"> <div class="tcaption"> <h3 class="title">股权穿透图</h3> <span class="watermark"></span> </div> <table class="ntable"> <tr> <th style="text-align: left;position: relative;">
                深圳市比一比网络科技有限公司
                <div id="guquanIframeTool" class="guquan-tool"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" target="_blank"><span class="screen">&nbsp;</span><span>全屏查看</span></a> <a class="m-l" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="save">&nbsp;</span><span>下载图谱</span></a> </div> </th> </tr> <tr> <td style="padding: 0px;"> <iframe id="guquanIframe" scrolling="no" src="company_guquan?keyNo=182249d7736fdb68960201022c19647a&iframe=1" frameborder="0"></iframe> </td> </tr> </table> </section> <section class="panel b-a clear" id="Mainmember"> <div class="tcaption"> <h3 class="title"> 主要人员</h3> <span class="tbadge">3</span> <span class="watermark"></span> </div> <table class="ntable ntable-odd"> <tr> <th class=""> 序号</th> <th class=""> 姓名</th> <th class="">职务</th> </tr> <tr> <td class="tx">1</td> <td width="50%"> <a href="/pl_p6d6ee98b1bebe675ecd39127ac7912e.html" class="c_a" title="蒋立民"><h3 class="seo font-14">蒋立民</h3></a> <a class="btn-touzi pull-right" href="/pl_p6d6ee98b1bebe675ecd39127ac7912e.html">他关联1家公司 > </a> </td> <td  class="text-center">
                监事
            </td> </tr> <tr> <td class="tx">2</td> <td width="50%"> <a href="/pl_pf041011972b479ca0cee915291ab07c.html" class="c_a" title="杜卫红"><h3 class="seo font-14">杜卫红</h3></a> <a class="btn-touzi pull-right" href="/pl_pf041011972b479ca0cee915291ab07c.html">他关联1家公司 > </a> </td> <td  class="text-center">
                总经理
            </td> </tr> <tr> <td class="tx">3</td> <td width="50%"> <a href="/pl_pf041011972b479ca0cee915291ab07c.html" class="c_a" title="杜卫红"><h3 class="seo font-14">杜卫红</h3></a> <a class="btn-touzi pull-right" href="/pl_pf041011972b479ca0cee915291ab07c.html">他关联1家公司 > </a> </td> <td  class="text-center">
                执行董事
            </td> </tr> </table> </section> <section class="panel b-a clear guquan-section" id="muhou"> <div class="tcaption"> <h3 class="title">企业关联图谱</h3> <span class="watermark"></span> </div> <table class="ntable"> <tr> <th style="text-align: left;position: relative;">
                深圳市比一比网络科技有限公司
                <div id="muhouIframeTool" class="guquan-tool"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" target="_blank"><span class="screen">&nbsp;</span><span>全屏查看</span></a> <a class="m-l" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="save">&nbsp;</span><span>下载图谱</span></a> </div> </th> </tr> <tr> <td style="padding: 0px;"> <iframe id="muhouIframe" scrolling="no" data-src="company_muhouinsertqiye?keyNo=182249d7736fdb68960201022c19647a&iframe=1" src="" frameborder="0"></iframe> </td> </tr> </table> <script type="text/javascript">
        var isIE = (!!window.ActiveXObject || "ActiveXObject" in window);
        if(isIE){
            $('#guquanDownload').hide();
        }
    </script> </section> <section class="panel b-a" id="Changelist"> <div class="tcaption"> <h3 class="title"> 变更记录</h3> <span class="tbadge">29</span> <div class="tdrop pull-right"> <span class="btn" data-toggle="dropdown"> <span class="changelisttype">全部类型</span> <span class="caret m-l"></span> </span> <ul class="dropdown-menu dropdown-menu-right"> <li><a onclick="changeRecordsFilter('',this)">全部类型</a></li> <li><a onclick="changeRecordsFilter('期限变更（经营期限、营业期限、驻在期限等变更）',this)">期限变更（经营期限、营业期限、驻在期限等变更）</a></li> <li><a onclick="changeRecordsFilter('章程或章程修正案通过日期',this)">章程或章程修正案通过日期</a></li> <li><a onclick="changeRecordsFilter('投资人变更（包括出资额、出资方式、出资日期、投资人名称等）',this)">投资人变更（包括出资额、出资方式、出资日期、投资人名称等）</a></li> <li><a onclick="changeRecordsFilter('注册资本变更（注册资金、资金数额等变更）',this)">注册资本变更（注册资金、资金数额等变更）</a></li> <li><a onclick="changeRecordsFilter('地址变更（住所地址、经营场所、驻在地址等变更）',this)">地址变更（住所地址、经营场所、驻在地址等变更）</a></li> <li><a onclick="changeRecordsFilter('其他事项备案',this)">其他事项备案</a></li> <li><a onclick="changeRecordsFilter('实收资本',this)">实收资本</a></li> <li><a onclick="changeRecordsFilter('监事信息',this)">监事信息</a></li> <li><a onclick="changeRecordsFilter('监事成员',this)">监事成员</a></li> <li><a onclick="changeRecordsFilter('名称变更（字号名称、集团名称等）',this)">名称变更（字号名称、集团名称等）</a></li> <li><a onclick="changeRecordsFilter('指定联系人',this)">指定联系人</a></li> <li><a onclick="changeRecordsFilter('经营范围变更（含业务范围变更）',this)">经营范围变更（含业务范围变更）</a></li> </ul> </div> </div> <table class="ntable"> <tr> <th class="tx">序号</th> <th>变更日期</th> <th>变更项目</th> <th>变更前</th> <th>变更后</th> </tr> <tr data-pname="期限变更（经营期限、营业期限、驻在期限等变更）"> <td class="tx">1</td> <td width="103" class="text-center">2018-11-01</td> <td width="" class="text-center">
                期限变更（经营期限、营业期限、驻在期限等变更）
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>从2009-01-12至2019-01-12</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>永续经营</em> <br> </div> </td> </tr> <tr data-pname="章程或章程修正案通过日期"> <td class="tx">2</td> <td width="103" class="text-center">2018-11-01</td> <td width="" class="text-center">
                章程或章程修正案通过日期
                            </td> <td width="30%"> <div style="max-width: 300px">
                     2018-<em>0</em>1-<em>29</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     2018-<em>1</em>0<em>-3</em>1
                    <br> </div> </td> </tr> <tr data-pname="投资人变更（包括出资额、出资方式、出资日期、投资人名称等）"> <td class="tx">3</td> <td width="103" class="text-center">2018-08-21</td> <td width="" class="text-center">
                投资人变更（包括出资额、出资方式、出资日期、投资人名称等）
                <br><span class="text-gray" style="font-size: 12px">带有*标记的为法定代表人</span> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:钟青,出资额:<em>12.2144</em>,出资比例:<em>1.3127</em> <br>  名称:蔡明星,出资额:<em>63.8479</em>,出资比例:<em>6.8617</em> <br>  名称:前海路路兴投资管理(深圳)有限公司,出资额:<em>80.4711</em>,出资比例:<em>8.6481</em> <br>  名称:梁飞鹏,出资额:<em>135.497</em>,出资比例:<em>14.5617</em> <br>  名称:雷祖云,出资额:<em>30.2201</em>,出资比例:<em>3.2477</em> <br>  名称:廉健,出资额:<em>26.5956</em>,出资比例:<em>2.8582</em> <br>  名称:李崇仁,出资额:<em>21.4016</em>,出资比例:<em>2.3</em> <br>  名称:章莉,出资额:<em>24.4474</em>,出资比例:<em>2.6273</em> <br>  名称:谢立欧,出资额:<em>55.9684</em>,出资比例:<em>6.0149</em> <br>  名称:徐成,出资额:<em>96.2</em>,出资比例:<em>10.3385</em> <br>  名称:许健航,出资额:<em>36.6426</em>,出资比例:<em>3.9379</em> <br>  名称:杜卫红*,出资额:<em>258.3666</em>,出资比例:<em>27.7663</em> <br>  名称:崔善仁,出资额:<em>88.6304</em>,出资比例:<em>9.525</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:雷祖云,出资额:30.2201,出资比例:<em>2.728081（-0.52%）</em> <br>  名称:杜卫红*,出资额:258.3666,出资比例:<em>23.323722（-4.443%）</em> <br>  名称:蔡明星,出资额:63.8479,出资比例:<em>5.763789（-1.098%）</em> <br> <em>名称:叶喜光,出资额:55.3871,出资比例:5.000001【新增】</em> <br>  名称:许健航,出资额:36.6426,出资比例:<em>3.307865（-0.63%）</em> <br>  名称:前海路路兴投资管理(深圳)有限公司,出资额:80.4711,出资比例:<em>7.264428（-1.384%）</em> <br> <em>名称:储敏健,出资额:22.1548,出资比例:1.999996【新增】</em> <br> <em>名称:王海荣,出资额:77.5419,出资比例:6.999998【新增】</em> <br>  名称:李崇仁,出资额:21.4016,出资比例:<em>1.932002（-0.368%）</em> <br>  名称:钟青,出资额:12.2144,出资比例:<em>1.102639（-0.21%）</em> <br>  名称:章莉,出资额:24.4474,出资比例:<em>2.206958（-0.42%）</em> <br>  名称:谢立欧,出资额:55.9684,出资比例:<em>5.052477（-0.962%）</em> <br>  名称:廉健,出资额:26.5956,出资比例:<em>2.400884（-0.457%）</em> <br>  名称:徐成,出资额:96.2,出资比例:<em>8.684334（-1.654%）</em> <br>  名称:崔善仁,出资额:<em>110.7852（+22.155）</em>,出资比例:<em>10.000995（+0.476%）</em> <br>  名称:梁飞鹏,出资额:135.497,出资比例:<em>12.231822（-2.33%）</em> <br> </div> </td> </tr> <tr data-pname="注册资本变更（注册资金、资金数额等变更）"> <td class="tx">4</td> <td width="103" class="text-center">2018-08-21</td> <td width="" class="text-center">
                注册资本变更（注册资金、资金数额等变更）
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>930.5031</em>人民币
                    <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>1107.7417</em>人民币<em>（+19.05%）</em> <br> </div> </td> </tr> <tr data-pname="章程或章程修正案通过日期"> <td class="tx">5</td> <td width="103" class="text-center">2018-08-21</td> <td width="" class="text-center">
                章程或章程修正案通过日期
                            </td> <td width="30%"> <div style="max-width: 300px">
                     201<em>6</em>-1<em>2</em>-2<em>3</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     201<em>8</em>-<em>0</em>1<em>-</em>2<em>9</em> <br> </div> </td> </tr> <tr data-pname="地址变更（住所地址、经营场所、驻在地址等变更）"> <td class="tx">6</td> <td width="103" class="text-center">2017-01-09</td> <td width="" class="text-center">
                地址变更（住所地址、经营场所、驻在地址等变更）
                            </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市南山区粤海街道<em>科苑路15号科兴科学</em>园<em>B</em>1<em>-4F</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市南山区粤海街道<em>高新技术园中区</em>科苑<em>大道讯美科技广场</em>1<em>栋3楼306</em> <br> </div> </td> </tr> <tr data-pname="投资人变更（包括出资额、出资方式、出资日期、投资人名称等）"> <td class="tx">7</td> <td width="103" class="text-center">2017-01-09</td> <td width="" class="text-center">
                投资人变更（包括出资额、出资方式、出资日期、投资人名称等）
                <br><span class="text-gray" style="font-size: 12px">带有*标记的为法定代表人</span> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:杜卫红*,出资额:<em>258.3666</em>,出资比例:<em>30.681</em> <br>  名称:雷祖云,出资额:<em>30.2201</em>,出资比例:<em>3.5886</em> <br>  名称:蔡明星,出资额:<em>63.8479</em>,出资比例:<em>7.5819</em> <br>  名称:谢立欧,出资额:<em>55.9684</em>,出资比例:<em>6.6462</em> <br>  名称:钟青,出资额:<em>12.2144</em>,出资比例:<em>1.4505</em> <br>  名称:廉健,出资额:<em>26.5956</em>,出资比例:<em>3.1582</em> <br>  名称:章莉,出资额:<em>24.4474</em>,出资比例:<em>2.9031</em> <br>  名称:许健航,出资额:<em>36.6426</em>,出资比例:<em>4.3513</em> <br>  名称:梁飞鹏,出资额:<em>135.497</em>,出资比例:<em>16.0903</em> <br>  名称:崔善仁,出资额:<em>42.1053</em>,出资比例:<em>5</em> <br>  名称:徐成,出资额:<em>96.2</em>,出资比例:<em>11.4237</em> <br>  名称:前海路路兴投资管理(深圳)有限公司,出资额:<em>60</em>,出资比例:<em>7.125</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:许健航,出资额:36.6426,出资比例:<em>3.9379（-0.413%）</em> <br>  名称:雷祖云,出资额:30.2201,出资比例:<em>3.2477（-0.341%）</em> <br>  名称:廉健,出资额:26.5956,出资比例:<em>2.8582（-0.3%）</em> <br>  名称:钟青,出资额:12.2144,出资比例:<em>1.3127（-0.138%）</em> <br>  名称:谢立欧,出资额:55.9684,出资比例:<em>6.0149（-0.631%）</em> <br>  名称:章莉,出资额:24.4474,出资比例:<em>2.6273（-0.276%）</em> <br>  名称:蔡明星,出资额:63.8479,出资比例:<em>6.8617（-0.72%）</em> <br> <em>名称:李崇仁,出资额:21.4016,出资比例:2.3【新增】</em> <br>  名称:杜卫红*,出资额:258.3666,出资比例:<em>27.7663（-2.915%）</em> <br>  名称:梁飞鹏,出资额:135.497,出资比例:<em>14.5617（-1.529%）</em> <br>  名称:徐成,出资额:96.2,出资比例:<em>10.3385（-1.085%）</em> <br>  名称:崔善仁,出资额:<em>88.6304（+46.525）</em>,出资比例:<em>9.525（+4.525%）</em> <br>  名称:前海路路兴投资管理(深圳)有限公司,出资额:<em>80.4711（+20.471）</em> <br> </div> </td> </tr> <tr data-pname="注册资本变更（注册资金、资金数额等变更）"> <td class="tx">8</td> <td width="103" class="text-center">2017-01-09</td> <td width="" class="text-center">
                注册资本变更（注册资金、资金数额等变更）
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>842.1053</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>930.5031</em><em>（+10.5%）</em> <br> </div> </td> </tr> <tr data-pname="投资人变更（包括出资额、出资方式、出资日期、投资人名称等）"> <td class="tx">9</td> <td width="103" class="text-center">2016-05-23</td> <td width="" class="text-center">
                投资人变更（包括出资额、出资方式、出资日期、投资人名称等）
                <br><span class="text-gray" style="font-size: 12px">带有*标记的为法定代表人</span> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:钟青,出资额:<em>12.2144</em>,出资比例:<em>1.5268</em> <br>  名称:雷祖云,出资额:<em>30.2201</em>,出资比例:<em>3.7775</em> <br>  名称:许健航,出资额:<em>36.6426</em>,出资比例:<em>4.5803</em> <br>  名称:廉健,出资额:<em>26.5956</em>,出资比例:<em>3.3245</em> <br>  名称:章莉,出资额:<em>24.4474</em>,出资比例:<em>3.0559</em> <br>  名称:杜卫红*,出资额:<em>258.3666</em>,出资比例:<em>32.2958</em> <br>  名称:谢立欧,出资额:<em>55.9684</em>,出资比例:<em>6.9961</em> <br>  名称:梁飞鹏,出资额:<em>135.497</em>,出资比例:<em>16.9371</em> <br>  名称:蔡明星,出资额:<em>63.8479</em>,出资比例:<em>7.981</em> <br>  名称:徐成,出资额:<em>96.2</em>,出资比例:<em>12.025</em> <br>  名称:前海路路兴投资管理(深圳)有限公司,出资额:<em>60</em>,出资比例:<em>7.5</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:杜卫红*,出资额:258.3666,出资比例:<em>30.681（-1.615%）</em> <br>  名称:雷祖云,出资额:30.2201,出资比例:<em>3.5886（-0.189%）</em> <br>  名称:蔡明星,出资额:63.8479,出资比例:<em>7.5819（-0.399%）</em> <br>  名称:谢立欧,出资额:55.9684,出资比例:<em>6.6462（-0.35%）</em> <br>  名称:钟青,出资额:12.2144,出资比例:<em>1.4505（-0.076%）</em> <br>  名称:廉健,出资额:26.5956,出资比例:<em>3.1582（-0.166%）</em> <br>  名称:章莉,出资额:24.4474,出资比例:<em>2.9031（-0.153%）</em> <br>  名称:许健航,出资额:36.6426,出资比例:<em>4.3513（-0.229%）</em> <br>  名称:梁飞鹏,出资额:135.497,出资比例:<em>16.0903（-0.847%）</em> <br> <em>名称:崔善仁,出资额:42.1053,出资比例:5【新增】</em> <br>  名称:徐成,出资额:96.2,出资比例:<em>11.4237（-0.601%）</em> <br>  名称:前海路路兴投资管理(深圳)有限公司,出资额:60,出资比例:<em>7.125（-0.375%）</em> <br> </div> </td> </tr> <tr data-pname="注册资本变更（注册资金、资金数额等变更）"> <td class="tx">10</td> <td width="103" class="text-center">2016-05-23</td> <td width="" class="text-center">
                注册资本变更（注册资金、资金数额等变更）
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>800</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>842.1053</em><em>（+5.26%）</em> <br> </div> </td> </tr> <tr data-pname="投资人变更（包括出资额、出资方式、出资日期、投资人名称等）"> <td class="tx">11</td> <td width="103" class="text-center">2016-03-29</td> <td width="" class="text-center">
                投资人变更（包括出资额、出资方式、出资日期、投资人名称等）
                <br><span class="text-gray" style="font-size: 12px">带有*标记的为法定代表人</span> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:谢立欧,出资额:55.9684,出资比例:6.9961
                    <br>  名称:廉健,出资额:26.5956,出资比例:3.3245
                    <br> <em>名称:蔡衍群,出资额:60,出资比例:7.5【退出】</em> <br>  名称:蔡明星,出资额:63.8479,出资比例:7.981
                    <br>  名称:杜卫红*,出资额:258.3666,出资比例:32.2958
                    <br>  名称:梁飞鹏,出资额:135.497,出资比例:16.9371
                    <br>  名称:钟青,出资额:12.2144,出资比例:1.5268
                    <br>  名称:徐成,出资额:96.2,出资比例:12.025
                    <br>  名称:许健航,出资额:36.6426,出资比例:4.5803
                    <br>  名称:雷祖云,出资额:30.2201,出资比例:3.7775
                    <br>  名称:章莉,出资额:24.4474,出资比例:3.0559
                    <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:钟青,出资额:12.2144,出资比例:1.5268
                    <br>  名称:雷祖云,出资额:30.2201,出资比例:3.7775
                    <br>  名称:许健航,出资额:36.6426,出资比例:4.5803
                    <br>  名称:廉健,出资额:26.5956,出资比例:3.3245
                    <br>  名称:章莉,出资额:24.4474,出资比例:3.0559
                    <br>  名称:杜卫红*,出资额:258.3666,出资比例:32.2958
                    <br>  名称:谢立欧,出资额:55.9684,出资比例:6.9961
                    <br>  名称:梁飞鹏,出资额:135.497,出资比例:16.9371
                    <br>  名称:蔡明星,出资额:63.8479,出资比例:7.981
                    <br>  名称:徐成,出资额:96.2,出资比例:12.025
                    <br> <em>名称:前海路路兴投资管理(深圳)有限公司,出资额:60,出资比例:7.5【新增】</em> <br> </div> </td> </tr> <tr data-pname="其他事项备案"> <td class="tx">12</td> <td width="103" class="text-center">2015-12-23</td> <td width="" class="text-center">
                其他事项备案
                            </td> <td width="30%"> <div style="max-width: 300px"> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>9144030068375453XL</em> <br> </div> </td> </tr> <tr data-pname="地址变更（住所地址、经营场所、驻在地址等变更）"> <td class="tx">13</td> <td width="103" class="text-center">2015-12-23</td> <td width="" class="text-center">
                地址变更（住所地址、经营场所、驻在地址等变更）
                            </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市南山区科<em>技园朗山</em>路<em>同方信息港E栋</em>5<em>楼</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市南山区<em>粤海街道</em>科<em>苑路15号科兴科学</em>园<em>B1-4F</em> <br> </div> </td> </tr> <tr data-pname="实收资本"> <td class="tx">14</td> <td width="103" class="text-center">2015-02-26</td> <td width="" class="text-center">
                实收资本
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>500</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>800</em><em>（+60%）</em> <br> </div> </td> </tr> <tr data-pname="实收资本"> <td class="tx">15</td> <td width="103" class="text-center">2015-02-26</td> <td width="" class="text-center">
                实收资本
                            </td> <td width="30%"> <div style="max-width: 300px">
                     人民币<em>500.0000</em>万元
                    <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     人民币<em>800.0000</em>万元<em>（+60%）</em> <br> </div> </td> </tr> <tr data-pname="投资人变更（包括出资额、出资方式、出资日期、投资人名称等）"> <td class="tx">16</td> <td width="103" class="text-center">2015-02-26</td> <td width="" class="text-center">
                投资人变更（包括出资额、出资方式、出资日期、投资人名称等）
                <br><span class="text-gray" style="font-size: 12px">带有*标记的为法定代表人</span> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:徐成,出资额:<em>65</em>,出资比例:<em>13</em> <br>  名称:许健航,出资额:<em>24.7585</em>,出资比例:<em>4.9517</em> <br>  名称:谢立欧,出资额:<em>37.8165</em>,出资比例:<em>7.5633</em> <br>  名称:杜卫红*,出资额:<em>174.572</em>,出资比例:<em>34.9144</em> <br>  名称:章莉,出资额:<em>16.5185</em>,出资比例:<em>3.3037</em> <br>  名称:蔡明星,出资额:<em>43.1405</em>,出资比例:<em>8.6281</em> <br>  名称:钟青,出资额:<em>8.253</em>,出资比例:<em>1.6506</em> <br>  名称:梁飞鹏,出资额:<em>91.552</em>,出资比例:<em>18.3104</em> <br>  名称:雷祖云,出资额:<em>20.419</em>,出资比例:<em>4.0838</em> <br>  名称:廉健,出资额:<em>17.97</em>,出资比例:<em>3.594</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:谢立欧,出资额:<em>55.9684（+18.152）</em>,出资比例:<em>6.9961（-0.567%）</em> <br>  名称:廉健,出资额:<em>26.5956（+8.626）</em> <br> <em>名称:蔡衍群,出资额:60,出资比例:7.5【新增】</em> <br>  名称:蔡明星,出资额:<em>63.8479（+20.707）</em>,出资比例:<em>7.981（-0.647%）</em> <br>  名称:杜卫红*,出资额:<em>258.3666（+83.795）</em>,出资比例:<em>32.2958（-2.619%）</em> <br>  名称:梁飞鹏,出资额:<em>135.497（+43.945）</em>,出资比例:<em>16.9371（-1.373%）</em> <br>  名称:钟青,出资额:<em>12.2144（+3.961）</em> <br>  名称:徐成,出资额:<em>96.2（+31.2）</em> <br>  名称:许健航,出资额:<em>36.6426（+11.884）</em>,出资比例:<em>4.5803（-0.371%）</em> <br>  名称:雷祖云,出资额:<em>30.2201（+9.801）</em>,出资比例:<em>3.7775（-0.306%）</em> <br>  名称:章莉,出资额:<em>24.4474（+7.929）</em>,出资比例:<em>3.0559（-0.248%）</em> <br> </div> </td> </tr> <tr data-pname="注册资本变更（注册资金、资金数额等变更）"> <td class="tx">17</td> <td width="103" class="text-center">2015-02-26</td> <td width="" class="text-center">
                注册资本变更（注册资金、资金数额等变更）
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>500</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>800</em><em>（+60%）</em> <br> </div> </td> </tr> <tr data-pname="监事信息"> <td class="tx">18</td> <td width="103" class="text-center">2015-02-26</td> <td width="" class="text-center">
                监事信息
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>杨翠娟(监事)【退出】</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>蒋立民(监事)【新增】</em> <br> </div> </td> </tr> <tr data-pname="监事成员"> <td class="tx">19</td> <td width="103" class="text-center">2015-02-26</td> <td width="" class="text-center">
                监事成员
                <br><span class="text-gray" style="font-size: 12px">带有*标记的为法定代表人</span> </td> <td width="30%"> <div style="max-width: 300px"> <em>杨翠娟(监事)【退出】</em> <br>  杜卫红*(总经理)
                    <br>  杜卫红*(执行(常务)董事)
                    <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>蒋立民(监事)【新增】</em> <br>  杜卫红*(执行(常务)董事)
                    <br>  杜卫红*(总经理)
                    <br> </div> </td> </tr> <tr data-pname="地址变更（住所地址、经营场所、驻在地址等变更）"> <td class="tx">20</td> <td width="103" class="text-center">2013-07-09</td> <td width="" class="text-center">
                地址变更（住所地址、经营场所、驻在地址等变更）
                            </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市<em>福田</em>区<em>福田保税区红棉道8号英达利</em>科技<em>数码</em>园<em>C</em>栋<em>302(C、D号)</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市<em>南山</em>区科技园<em>朗山路同方信息港E</em>栋<em>5楼</em> <br> </div> </td> </tr> <tr data-pname="名称变更（字号名称、集团名称等）"> <td class="tx">21</td> <td width="103" class="text-center">2013-04-08</td> <td width="" class="text-center">
                名称变更（字号名称、集团名称等）
                            </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市一<em>路无忧</em>科技有限公司
                    <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市<em>比</em>一<em>比网络</em>科技有限公司
                    <br> </div> </td> </tr> <tr data-pname="指定联系人"> <td class="tx">22</td> <td width="103" class="text-center">2013-04-08</td> <td width="" class="text-center">
                指定联系人
                            </td> <td width="30%"> <div style="max-width: 300px"> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>刘玲妹</em> <br> </div> </td> </tr> <tr data-pname="实收资本"> <td class="tx">23</td> <td width="103" class="text-center">2013-01-24</td> <td width="" class="text-center">
                实收资本
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>326.8</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>500</em><em>（+53%）</em> <br> </div> </td> </tr> <tr data-pname="投资人变更（包括出资额、出资方式、出资日期、投资人名称等）"> <td class="tx">24</td> <td width="103" class="text-center">2013-01-24</td> <td width="" class="text-center">
                投资人变更（包括出资额、出资方式、出资日期、投资人名称等）
                <br><span class="text-gray" style="font-size: 12px">带有*标记的为法定代表人</span> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:梁飞鹏,出资额:<em>68.78</em>,出资比例:<em>21.0465</em> <br>  名称:杜卫红*,出资额:<em>131.15</em>,出资比例:<em>40.1315</em> <br>  名称:雷祖云,出资额:<em>15.34</em>,出资比例:<em>4.694</em> <br>  名称:钟青,出资额:<em>6.2</em>,出资比例:<em>1.8972</em> <br>  名称:许健航,出资额:<em>18.6</em>,出资比例:<em>5.6916</em> <br>  名称:谢立欧,出资额:<em>28.41</em>,出资比例:<em>8.6934</em> <br>  名称:廉健,出资额:<em>13.5</em>,出资比例:<em>4.131</em> <br>  名称:蔡明星,出资额:<em>32.41</em>,出资比例:<em>9.9174</em> <br>  名称:章莉,出资额:<em>12.41</em>,出资比例:<em>3.7974</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>名称:徐成,出资额:65,出资比例:13【新增】</em> <br>  名称:许健航,出资额:<em>24.7585（+6.158）</em> <br>  名称:谢立欧,出资额:<em>37.8165（+9.406）</em> <br>  名称:杜卫红*,出资额:<em>174.572（+43.422）</em>,出资比例:<em>34.9144（-5.217%）</em> <br>  名称:章莉,出资额:<em>16.5185（+4.108）</em> <br>  名称:蔡明星,出资额:<em>43.1405（+10.731）</em> <br>  名称:钟青,出资额:<em>8.253（+2.053）</em> <br>  名称:梁飞鹏,出资额:<em>91.552（+22.772）</em>,出资比例:<em>18.3104（-2.736%）</em> <br>  名称:雷祖云,出资额:<em>20.419（+5.079）</em>,出资比例:<em>4.0838（-0.61%）</em> <br>  名称:廉健,出资额:<em>17.97（+4.47）</em>,出资比例:<em>3.594（-0.537%）</em> <br> </div> </td> </tr> <tr data-pname="注册资本变更（注册资金、资金数额等变更）"> <td class="tx">25</td> <td width="103" class="text-center">2013-01-24</td> <td width="" class="text-center">
                注册资本变更（注册资金、资金数额等变更）
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>326.8</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>500</em><em>（+53%）</em> <br> </div> </td> </tr> <tr data-pname="投资人变更（包括出资额、出资方式、出资日期、投资人名称等）"> <td class="tx">26</td> <td width="103" class="text-center">2012-08-10</td> <td width="" class="text-center">
                投资人变更（包括出资额、出资方式、出资日期、投资人名称等）
                <br><span class="text-gray" style="font-size: 12px">带有*标记的为法定代表人</span> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:谢立欧,出资额:<em>28.41</em>,出资比例:<em>13.74</em> <br>  名称:梁飞鹏,出资额:<em>23.78</em>,出资比例:<em>11.5</em> <br>  名称:许健航,出资额:<em>18.6</em>,出资比例:<em>9</em> <br>  名称:雷祖云,出资额:<em>10.34</em>,出资比例:<em>5</em> <br>  名称:杜卫红*,出资额:<em>81.15</em>,出资比例:<em>39.24</em> <br>  名称:章莉,出资额:<em>12.41</em>,出资比例:<em>6</em> <br>  名称:蔡明星,出资额:<em>12.41</em>,出资比例:<em>6</em> <br>  名称:钟青,出资额:<em>6.2</em>,出资比例:<em>3</em> <br>  名称:廉健,出资额:<em>13.5</em>,出资比例:<em>6.52</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     名称:梁飞鹏,出资额:<em>68.78（+45）</em>,出资比例:<em>21.0465（+9.547%）</em> <br>  名称:杜卫红*,出资额:<em>131.15（+50）</em>,出资比例:<em>40.1315（+0.892%）</em> <br>  名称:雷祖云,出资额:<em>15.34（+5）</em>,出资比例:<em>4.694（-0.306%）</em> <br>  名称:钟青,出资额:6.2,出资比例:<em>1.8972（-1.103%）</em> <br>  名称:许健航,出资额:18.6,出资比例:<em>5.6916（-3.308%）</em> <br>  名称:谢立欧,出资额:28.41,出资比例:<em>8.6934（-5.047%）</em> <br>  名称:廉健,出资额:13.5,出资比例:<em>4.131（-2.389%）</em> <br>  名称:蔡明星,出资额:<em>32.41（+20）</em>,出资比例:<em>9.9174（+3.917%）</em> <br>  名称:章莉,出资额:12.41,出资比例:<em>3.7974（-2.203%）</em> <br> </div> </td> </tr> <tr data-pname="注册资本变更（注册资金、资金数额等变更）"> <td class="tx">27</td> <td width="103" class="text-center">2012-08-10</td> <td width="" class="text-center">
                注册资本变更（注册资金、资金数额等变更）
                            </td> <td width="30%"> <div style="max-width: 300px"> <em>206.8</em> <br> </div> </td> <td width="30%"> <div style="max-width: 300px"> <em>326.8</em><em>（+58.03%）</em> <br> </div> </td> </tr> <tr data-pname="地址变更（住所地址、经营场所、驻在地址等变更）"> <td class="tx">28</td> <td width="103" class="text-center">2012-07-24</td> <td width="" class="text-center">
                地址变更（住所地址、经营场所、驻在地址等变更）
                            </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市福田区<em>车公庙工业</em>区<em>中联大厦第4层4</em>0<em>1B</em>(<em>仅限办公</em>)
                    <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     深圳市福田区<em>福田保税</em>区<em>红棉道8号英达利科技数码园C栋3</em>0<em>2</em>(<em>C、D号</em>)
                    <br> </div> </td> </tr> <tr data-pname="经营范围变更（含业务范围变更）"> <td class="tx">29</td> <td width="103" class="text-center">2012-07-24</td> <td width="" class="text-center">
                经营范围变更（含业务范围变更）
                            </td> <td width="30%"> <div style="max-width: 300px">
                     计算机软硬件、通讯设备、网络的技术开发和销售,技术咨询
                    <br>  企业管理咨询及其它信息咨询(不含人才中介服务、证券及其它限制项目)
                    <br>  代订机票
                    <br>  会议策划
                    <br>  从事广告业务(法律、行政法规规定应进行广告经营审批登记的,另行办理审批登记后方可经营)。
                    <br> </div> </td> <td width="30%"> <div style="max-width: 300px">
                     计算机软硬件、通讯设备、网络的技术开发和销售,技术咨询
                    <br>  企业管理咨询及其它信息咨询(不含人才中介服务、证券及其它限制项目)
                    <br>  代订机票
                    <br>  会议策划
                    <br>  从事广告业务(法律、行政法规规定应进行广告经营审批登记的,另行办理审批登记后方可经营)
                    <br> <em>国内贸易(法律、行政法规、国务院决定规定在登记前须经批准的项目除外)</em>。
                    <br> </div> </td> </tr> </table> </section> <section class="panel b-a" id="Comintroduce"> <div class="tcaption"> <h3 class="title">公司简介</h3> <span class="watermark"></span> </div> <div class="" style="width:100%;margin: 0 auto;"> <div style="border:#E6E6E6 1px solid;padding: 15px;"> <p class="mb10 cmp-txtshow" id="textShowMore">公司为留美博士后和世界500强高管联合创立的高新技术企业，致力于先进技术平台构建，拟于3年内成为行业领军企业，重点项目为各类高性能的润滑油（脂、剂）产品，产品性能国内领先，世界一流水平。现诚聘各类人才，如果你足够优秀，将享受“年薪+股权”的事业合伙人待遇。</p> </div> </div> </section> <section class="panel b-a clear"> <div class="m_ptsc" style="padding:20px 0;">数据来源：国家企业信用信息公示系统。</div> </section> <script type="text/javascript">


  

setTimeout(function(){
    var touziIndustry = JSON.parse('null');
    var touziProvince = JSON.parse('null');
    touziChart(touziIndustry,touziProvince);

    showHistoryTip();
    drawGuquanStatic('深圳市比一比网络科技有限公司',[{"Org":2,"KeyNo":"pf041011972b479ca0cee915291ab07c","HasImage":false,"CompanyCount":1,"StockName":"\u675c\u536b\u7ea2","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"23.32%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"258.3666","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":23.32,"ShouldCapiAmount":258.3666,"StockPercentNew":"23.32","kzr":true},{"Org":2,"KeyNo":"p5a8ef899114677ea39258ce1d927618","HasImage":false,"CompanyCount":13,"StockName":"\u6881\u98de\u9e4f","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"12.23%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"135.497","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":12.23,"ShouldCapiAmount":135.497,"StockPercentNew":"12.23"},{"Org":2,"KeyNo":"p3fea0a9bdc30ebb8a1988fe70eba138","HasImage":false,"CompanyCount":1,"StockName":"\u5d14\u5584\u4ec1","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"10.00%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"110.7852","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":10,"ShouldCapiAmount":110.7852,"StockPercentNew":"10.00"},{"Org":2,"KeyNo":"p31a8061cd66dffa5249b6d77af11da9","HasImage":false,"CompanyCount":8,"StockName":"\u5f90\u6210","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"8.68%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"96.2","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":8.68,"ShouldCapiAmount":96.2,"StockPercentNew":"8.68"},{"Org":0,"KeyNo":"989fd43dc4f1993e430476602dca4477","HasImage":false,"CompanyCount":4,"StockName":"\u524d\u6d77\u8def\u8def\u5174\u6295\u8d44\u7ba1\u7406\uff08\u6df1\u5733\uff09\u6709\u9650\u516c\u53f8","StockType":"\u4f01\u4e1a\u6cd5\u4eba","StockPercent":"7.26%","IdentifyType":"\u6cd5\u4eba\u8425\u4e1a\u6267\u7167","IdentifyNo":"91440300326526416U","ShouldCapi":"80.4711","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":7.26,"ShouldCapiAmount":80.4711,"ImageUrl":"https:\/\/qccdata.qichacha.com\/AutoImage\/989fd43dc4f1993e430476602dca4477.jpg?x-oss-process=image\/resize,w_120","StockPercentNew":"7.26"},{"Org":2,"KeyNo":"pr7f1b847e10be21392c7cb2d4f1784e","HasImage":false,"CompanyCount":1,"StockName":"\u738b\u6d77\u8363","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"7.00%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"77.5419","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":7,"ShouldCapiAmount":77.5419,"StockPercentNew":"7.00"},{"Org":2,"KeyNo":"pe28cb0e0fc5b968bf594ecd94087036","HasImage":false,"CompanyCount":14,"StockName":"\u8521\u660e\u661f","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"5.76%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"63.8479","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":5.76,"ShouldCapiAmount":63.8479,"StockPercentNew":"5.76"},{"Org":2,"KeyNo":"p7f87d7afe9561009a8a4c9122265a16","HasImage":false,"CompanyCount":3,"StockName":"\u8c22\u7acb\u6b27","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"5.05%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"55.9684","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":5.05,"ShouldCapiAmount":55.9684,"StockPercentNew":"5.05"},{"Org":2,"KeyNo":"pr882b2e2ecd35bea830ae13bd226480","HasImage":false,"CompanyCount":1,"StockName":"\u53f6\u559c\u5149","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"5.00%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"55.3871","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":5,"ShouldCapiAmount":55.3871,"StockPercentNew":"5.00"},{"Org":2,"KeyNo":"pf0f32e2b89d7e1f3fe5cf082a3ea06a","HasImage":false,"CompanyCount":3,"StockName":"\u8bb8\u5065\u822a","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"3.31%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"36.6426","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":3.31,"ShouldCapiAmount":36.6426,"StockPercentNew":"3.31"},{"Org":2,"KeyNo":"p57156b45e95c64e00f4558ecc45c4d2","HasImage":false,"CompanyCount":1,"StockName":"\u96f7\u7956\u4e91","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"2.73%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"30.2201","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":2.73,"ShouldCapiAmount":30.2201,"StockPercentNew":"2.73"},{"Org":2,"KeyNo":"p265b141964bfd56af5001ad576d62ed","HasImage":false,"CompanyCount":17,"StockName":"\u5ec9\u5065","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"2.40%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"26.5956","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":2.4,"ShouldCapiAmount":26.5956,"StockPercentNew":"2.40"},{"Org":2,"KeyNo":"p74903795403c56bd14357ae017d4d7a","HasImage":false,"CompanyCount":3,"StockName":"\u7ae0\u8389","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"2.21%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"24.4474","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":2.21,"ShouldCapiAmount":24.4474,"StockPercentNew":"2.21"},{"Org":2,"KeyNo":"pr86619178967decf03c16add5db68cf","HasImage":false,"CompanyCount":1,"StockName":"\u50a8\u654f\u5065","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"2.00%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"22.1548","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":2,"ShouldCapiAmount":22.1548,"StockPercentNew":"2.00"},{"Org":2,"KeyNo":"p7a21d3940e6ddc045a24cc74acad02b","HasImage":false,"CompanyCount":7,"StockName":"\u674e\u5d07\u4ec1","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"1.93%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"21.4016","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":1.93,"ShouldCapiAmount":21.4016,"StockPercentNew":"1.93"},{"Org":2,"KeyNo":"pe87662246ebb26358d1d98b191cd522","HasImage":false,"CompanyCount":9,"StockName":"\u949f\u9752","StockType":"\u81ea\u7136\u4eba\u80a1\u4e1c","StockPercent":"1.10%","IdentifyType":"\u5c45\u6c11\u8eab\u4efd\u8bc1","IdentifyNo":"","ShouldCapi":"12.2144","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":1.1,"ShouldCapiAmount":12.2144,"StockPercentNew":"1.10"}]);
    $('body').on('click','.sanbanGd a',function(){
        var date = $(this).attr('data-value');
        $.ajax({
            type:'get',
            url:INDEX_URL + '/company_getSanbanGd',
            data:{code:'',date:date},
            dataType:'html',
            success:function(data){
                if(data){
                    $('#ipoSockinfo').html(data);
                    //$.scrollTo('#ipoSockinfo',{duration: 100, offset: -60});
                }
            }
        })
    });
  },500);
</script> </div> <p class="baidu-des" style="color:#f2f4f8;display:none">
                深圳市比一比网络科技有限公司怎么样？,企查查为您提供深圳市比一比网络科技有限公司的最新工商信息、诉讼信息、电话号码、招聘信息、公司简介、公司地址、公司规模、信用信息、财务信息等详细信息，让您在选择深圳市比一比网络科技有限公司前能够做到全面了解深圳市比一比网络科技有限公司的信用信息。
            </p> </div> <div class="col-sm-3 m_rightPanels"> <div class="panel b-a n-s" id="fapiao-title"> <div class="panel-heading b-b btab"> <a href="#qiyeQrcode" onclick="changeQrTAB(1,this);zhugeTrack('企业主页-企业二维码',{'企业名称':'深圳市比一比网络科技有限公司'});" data-toggle="tab"><h2>企业二维码</h2></a> <a href="#fapiaoQrcode" onclick="changeQrTAB(2,this);zhugeTrack('企业主页-发票抬头',{'企业名称':'深圳市比一比网络科技有限公司'});" data-toggle="tab" class="active"><h2>发票抬头</h2></a> </div> <div class="panel-body text-center"> <div id="qiyeQrcode" style="display: none;"> <div id="qiye_taitou" class="m_qrp"></div> <div class="m-t-xs text-dark m-b">企查查APP扫一扫查看企业详情</div> </div> <div id="fapiaoQrcode"> <a id="fapiao_taitou" class="m_qrp" href="/tax_view?keyno=182249d7736fdb68960201022c19647a"> </a> <div class="m-t-xs text-dark">企查查APP扫一扫保存发票抬头</div> <div class="m-t-md TaxView" style="display: none"> <p class="text-left">名称&nbsp;:&nbsp;<span class="Name"></span></p> <p class="text-left">税号&nbsp;:&nbsp;<span class="CreditCode"></span></p> <p class="text-left">地址&nbsp;:&nbsp;<span class="Address"></span></p> <p class="text-left">电话&nbsp;:&nbsp;<span class="PhoneNumber"></span></p> <p class="text-left">开户银行&nbsp;:&nbsp;<span class="Bank"></span></p> <p class="text-left">银行账户&nbsp;:&nbsp;<span class="Bankaccount"></span></p> </div> </div> </div> </div> <div class="panel b-a n-s"> <div class="panel-heading b-b"> <span class="font-bold font-15 text-dark"><h2>下载报告</h2></span> </div> <div class="panel-body"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-下载报告',{'企业名称':'深圳市比一比网络科技有限公司'});" target="_blank"> <img src="/material/theme/chacha/cms/v2/images/report.png?t=3" alt="企查查报告" style="width: 100%;margin-bottom: 10px;"/> </a> <a class="btn btn-primary basePageBt" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-下载报告',{'企业名称':'深圳市比一比网络科技有限公司'});" target="_blank">下载报告</a> </div> </div> <section class="panel b-a n-s"> <div class="panel-heading b-b"> <span class="font-bold font-15 text-dark"><h2>企业图谱</h2></span> </div> <div class="panel-body"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-查看企业图谱',{'企业名称':'深圳市比一比网络科技有限公司'});"> <img src="/material/theme/chacha/cms/v2/images/qytu.png?t=3" alt="企查查图谱" style="width: 100%;margin-bottom: 10px;"/> </a> <a class="btn btn-primary basePageBt" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-查看企业图谱',{'企业名称':'深圳市比一比网络科技有限公司'});">查看企业图谱</a> </div> </section> <section class="panel b-a n-s"> <div class="panel-heading b-b"> <span class="font-bold font-15 text-dark"><h2>股权穿透图</h2></span> </div> <div class="panel-body"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-查看投资图谱',{'企业名称':'深圳市比一比网络科技有限公司'});"> <img src="/material/theme/chacha/cms/v2/images/tupu.png?t=3" alt="企查查股权穿透图" style="width: 100%;margin-bottom: 10px;"/> </a> <a class="btn btn-primary basePageBt" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-查看投资图谱',{'企业名称':'深圳市比一比网络科技有限公司'});">查看股权穿透</a> </div> </section> <section class="panel b-a n-s"> <div class="panel-heading b-b"> <span class="font-bold font-15 text-dark"><h2>关联图谱</h2></span> </div> <div class="panel-body"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" target="_blank"> <img src="/material/theme/chacha/cms/v2/images/muhou.png?t=3" style="width: 100%;margin-bottom: 10px;" alt="企查查关联图谱" /> </a> <a class="btn btn-primary basePageBt" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha();zhugeTrack('企业主页-查看关联图谱',{'企业名称':'深圳市比一比网络科技有限公司'});" target="_blank">查看关联图谱</a> </div> </section> <section class="panel b-a n-s"> <div class="panel-heading b-b"> <span class="font-bold font-15 text-dark"><h2>您可能感兴趣的公司</h2></span> </div> <ul class="list-group no-bg auto"> <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'上海皋森实业有限公司'});" href="/firm_89621c8593c4c0759941fdc0e181c4e2" class="list-group-item clearfix"> <span class="clear"> <span>上海皋森实业有限公司</span><br/> </span> </a> <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'石家庄尚佳信息技术咨询服务有限公司'});" href="/firm_89331f886ca8e6f26b9af757de247cdd" class="list-group-item clearfix"> <span class="clear"> <span>石家庄尚佳信息技术咨询服务有限公司</span><br/> </span> </a> <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'封开县长岗镇起业碎石加工场'});" href="/firm_893faa6cfbd8545c942d8ac7fb606095" class="list-group-item clearfix"> <span class="clear"> <span>封开县长岗镇起业碎石加工场</span><br/> </span> </a> <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'浙江联和消防科技有限公司'});" href="/firm_8931e04971c20d8b4bd2705aacabe704" class="list-group-item clearfix"> <span class="clear"> <span>浙江联和消防科技有限公司</span><br/> </span> </a> <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'昆山市张浦镇迪展模具厂'});" href="/firm_0eb9982c2200bf21c4bf9d7fe76273e0" class="list-group-item clearfix"> <span class="clear"> <span>昆山市张浦镇迪展模具厂</span><br/> </span> </a> </ul> </section> <section class="panel b-a n-s"> <div class="panel-heading b-b"> <span class="font-bold font-15 text-dark"><h2>最新动态</h2></span> <a class="pull-right v3e_more" href="/cjob_182249d7736fdb68960201022c19647a" id="job_title" tabid="job">查看更多></a> </div> <ul class="list-group no-bg auto"> <a href="/postnews_94fdc136bd6b00e1e47a555752120fb7.html" target="_blank" class="list-group-item clearfix"> <span class="clear"> <span>长信科技：华林证券有限责任公司关于公司发行股份购买资产之独立财务顾问报告</span> </span> <span class="text-muted text-xs"><i class="i i-clock"></i> 2014-01-03</span> <span class="pull-right text-muted text-xs" style="padding: 4px">http://sc.stock.cnfol.com</span> </a> <a href="/postnews_73cc3181894e895bf04c395da335e3d7.html" target="_blank" class="list-group-item clearfix"> <span class="clear"> <span>长信科技：发行股份购买资产报告书</span> </span> <span class="text-muted text-xs"><i class="i i-clock"></i> 2014-01-03</span> <span class="pull-right text-muted text-xs" style="padding: 4px">http://sc.stock.cnfol.com</span> </a> </ul> </section> <section class="panel b-a n-s usercomment"> <div class="panel-heading b-b"> <span class="font-bold font-15 text-dark"><h2>用户评论</h2></span> </div> <ul class="list-group no-bg auto" id="commentList"> <li class="list-group-item"> <div class="pnodata"> <img src="/material/theme/chacha/cms/v2/images/nno_image.png"> <p>暂无评论</p> </div> </li> </ul> <div class="submit"> <div class="input-group"> <input type="text" id="commentcontentnew" value="" placeholder="请输入评论" name="content" class="form-control" required="required" autocomplete="off"> <span class="input-group-btn"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="btn btn-primary">评论</a> </span> </div> </div> </section> <script type="text/javascript">
    if($('#commentList').height()>=434){
        $('#commentList').slimScroll({
            wheelStep: 3,
            height:434
        });
    }
</script> </div> </div> </div> <style>
    #appDownloadModal .modal-dialog{
        width: 360px;
        height: 480px;
    }
    #appDownloadModal .modal-dialog .modal-content{
        width: 360px;
        height: 480px;
    }
    #appDownloadModal .modal-body{
        padding: 40px;
    }
    #appDownloadModal .modal-footer{
        margin-top: 0;
        text-align: left;
    }
    .qocdeBox{
        width: 278px;
        height: 278px;
        padding: 5px;
        border: 1px solid #c7c7c7;
        margin:auto;
    }
    .qocdeBox img{
        width: 100%;
    }
</style> <div class="modal fade" id="appDownloadModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">下载APP</h4> </div> <div class="modal-body"> <div class="qocdeBox"> <img src="/material/theme/chacha/cms/app/images/download_qcode.png" alt="企查查APP下载"/> </div> </div> <div class="modal-footer">
                扫描下载企查查APP，公司股权占比一览无余
            </div> </div> </div> </div> <script type="text/javascript">
zhugeTrack('企业主页',{'企业名称':'深圳市比一比网络科技有限公司'});

  var ipoTag = false;
 $(function(){
    getSCAN('182249d7736fdb68960201022c19647a');
    if(ipoTag){
        setCompanyNavFixed(440);
    }else{
        setCompanyNavFixed(410);
    }
    
 })  

</script> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/company-footer.css?time=1497542400" type="text/css"/> <div class="modal fade" id="shareModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="modal-body"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <div class="share"> <h3>分享到</h3> <p>微信扫描二维码分享</p> <div id="qrcode" data=""></div> <a href="http://service.weibo.com/share/share.php?title=企业内幕：你所不了解的深圳市比一比网络科技有限公司 | 查企业，就上企查查！&amp;url=http://www.qichacha.com/firm_182249d7736fdb68960201022c19647a" class="btn btn-lg btn-icon btn-danger btn-rounded btn-inactive m-r-xs m-t" target="_blank"> <i class="fa fa-weibo"></i></a> <a href="mailto:?subject=企业内幕：你所不了解的深圳市比一比网络科技有限公司 | 查企业，就上企查查！&amp;body=http://www.qichacha.com/firm_182249d7736fdb68960201022c19647a" class="btn btn-lg  btn-icon btn-info btn-rounded btn-inactive m-l m-t" target="_blank"><i class="fa fa-envelope"></i></a> </div> </div> </div> </div> </div> <div class="modal fade" id="groupModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal" style="width: 600px;"> <div class="modal-content"> <div class="modal-header"> <button id="editNewClose" type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">添加关注</h4> </div> <div class="modal-body"> <div class="group-panel"> <ul class="tab clearfix"> <li class="active"> <a href="#groupEdit" data-toggle="tab"> 加入已有分组 </a> </li> <li> <a href="#groupAdd" data-toggle="tab">加入新分组</a> </li> </ul> <div class="tab-content"> <div class="tab-pane fade in active" id="groupEdit"> <div class="edit-wrap"> <table class="table" id="groupList"> </table> </div> </div> <div class="tab-pane fade" id="groupAdd"> <input type="text" class="form-control" placeholder="请输入新分组名称" value=""/> </div> </div> </div> </div> <div class="modal-footer"> <input type="hidden" value="182249d7736fdb68960201022c19647a" id="groupCompanykey"/> <button type="button" onclick="editDone()" class="btn btn-primary">
                    确定
                </button> </div> </div> </div> </div> <div class="modal fade" id="transferFilesModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal nmodal-sm"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">申请工商调档</h4> </div> <div class="modal-body"> <form class="form-horizontal" role="form"> <div class="form-group"> <label class="col-sm-2">手机号码</label> <div class="col-sm-10"> <input type="text" class="form-control transferFilesPhone" placeholder="请输入您的手机号码"> <span class="phonemsg text-danger"></span> </div> </div> <div class="form-group"> <label class="col-sm-2">姓名</label> <div class="col-sm-10"> <input type="text" class="form-control transferFilesName" placeholder="请输入您的真实姓名"> <span class="emailmsg text-danger"></span> </div> </div> <div class="form-group"> <label class="col-sm-2">查档类型</label> <div class="col-sm-10"> <textarea class="form-control transferFilesType" rows="3" placeholder="请输入您要查询的档案类型"></textarea> <span class="text-danger"></span> </div> </div> <div class="form-group m-t-lg"> <label class="col-sm-2">&nbsp;</label> <div class="col-sm-10 text-center"> <input type="hidden" class="transferFilesCompanykey" value="182249d7736fdb68960201022c19647a"/> <span class="btn btn-primary btn-block transferFilesSubmit">提交</span> </div> </div> </form> </div> </div> </div> </div> <div class="modal fade" id="contactModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal nmodal-sm"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">委托联系</h4> </div> <div class="modal-body"> <form class="form-horizontal" role="form" id="contactCompany"> <div id="contactForm" style="height: 530px;"> <div class="form-group"> <label class="col-sm-2">您的姓名</label> <div class="col-sm-10"> <input type="text" class="form-control" name="name" placeholder="请输入您的姓名"> <span msgfor="name"></span> </div> </div> <div class="form-group"> <label class="col-sm-2">手机号</label> <div class="col-sm-10"> <input type="text" class="form-control" name="phone" placeholder="请输入手机号"> <span msgfor="phone"></span> </div> </div> <div class="form-group"> <label class="col-sm-2">邮箱</label> <div class="col-sm-10"> <input type="text" class="form-control" name="email" placeholder="请输入邮箱"> <span msgfor="email"></span> </div> </div> <div class="form-group"> <label class="col-sm-2">公司名称</label> <div class="col-sm-10"> <input type="text" class="form-control" name="companyName" placeholder="请输入公司名称"> <span msgfor="companyName"></span> </div> </div> <div class="form-group"> <label class="col-sm-2">所在行业</label> <div class="col-sm-10"> <input type="text" class="form-control" name="industry" placeholder="请输入所在行业"> <span msgfor="industry"></span> </div> </div> <div class="form-group"> <label class="col-sm-2">职位</label> <div class="col-sm-10"> <input type="text" class="form-control" name="job" placeholder="请输入职位"> <span msgfor="job"></span> </div> </div> <div class="form-group"> <label class="col-sm-2">委托事由</label> <div class="col-sm-10"> <textarea style="resize:none;line-height: 1.2;" class="form-control" rows="4" maxlength="140" name="content" placeholder="请输入委托事由" onChange="checkWord(this);" onKeyUp="checkWord(this);" onMouseDown="checkWord(this);"></textarea> <div id="inputLimit" style="position: absolute;display: none; color: #999;font-size: 12px;right: 14px;"><span>120</span>/140字</div> <span msgfor="content"></span> </div> </div> <div class="m_declare"> <p>重要声明：</p> <p style="line-height: 1.3;">请您如实的填写以上信息，企查查仅对您填写的信息进行形式审查，因您填写的信息虚假、错误等造成的后果，由委托人自行承担，企查查不承担任何责任。委托人填写的委托事由，应当符合国家法律、法规、规章的规定，否则造成的任何后果由委托人自行承担。若因法律、法规的规定由企查查承担责任的，企查查有权向委托人追偿。 </p> </div> </div> <div id="contactPreview" style="display: none;height: 530px;background: url(/material/theme/chacha/cms/v2/images/wtmb.png) no-repeat; background-size: 100%;"> <div class="mbyl-middle"> <div class="title">深圳市比一比网络科技有限公司，您好：</div> <div class="subtitle">
                                我是 <span id="ylCompanyName"></span> 的 <span id="ylName"></span>，真诚期待与贵公司合作，以下是我的联系方式，期待您的回复！
                            </div> <div class="tip-contact">行业：<span id="ylIndustry"></span></div> <div class="tip-contact">职位：<span id="ylJob"></span></div> <div class="tip-contact">手机：<span id="ylPhone"></span></div> <div class="tip-contact">邮箱：<span id="ylEmail"></span></div> <div class="tip-contact">委托事由：<span id="ylContent"></span></div> <div class="tip-wrap"> <div class="step-title">重要说明：</div> <div class="step-content">
                                    该邮件是企查查接受平台用户 <span id="ylName2"></span> 的委托，向贵公司发送的系统邮件（请勿直接回复），以帮助企业促成商务合作，邮件内容及信息不代表企查查的任何观点及保证，请自行判断商业风险，企查查不承担任何责任。
                                </div> </div> </div> </div> <div class="form-group m-t-md"> <label class="col-sm-2">&nbsp;</label> <div class="col-sm-10 text-right"> <input type="hidden" name="type" value="2"/> <input type="hidden" name="companykey" value="182249d7736fdb68960201022c19647a"/> <input type="hidden" name="toCompanyName" value="深圳市比一比网络科技有限公司"/> <span class="btn btn-primary m-r-sm" id="ylBtn" onclick="contactCompanyPreview();">邮件预览</span> <button type="submit" class="btn btn-primary contactCompany1">委托发送</button> </div> </div> </form> </div> </div> </div> </div> <div class="modal fade" id="postCardModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal sm"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title postcard-tep1">设置名片</h4> <h4 class="modal-title postcard-tep2">发送名片</h4> </div> <form class="form-horizontal pform" role="form" id="postCardForm"> <div class="modal-body postcard-tep1"> <div class="form-group"> <label class="col-pre">选择头像<span class="redstar">*</span></label> <div class="col-after" style="margin-top: 8px;"> <div id="uploadFaceImgArea" class="fileinput"> <div class="img" onclick="fileinput('faceImg')" style="display: block;"> <img src="" onerror="this.src='/material/theme/chacha/cms/v2/images/default_face.png'"> <span>上传头像</span> </div> <input type="hidden" name="faceimg"> <span class="message" msgfor="faceimg"> </span> </div> </div> </div> <div class="form-group"> <label class="col-pre">真实姓名<span class="redstar">*</span></label> <div class="col-after"> <input type="text" class="form-control" name="name" placeholder="请输入真实姓名" value=""> <span msgfor="name"></span> </div> </div> <div class="form-group"> <label class="col-pre">公司<span class="redstar">*</span></label> <div class="col-after"> <input type="hidden" name="my_company_keyno" id="postCardCompanyKey" value=""> <input type="text" class="form-control" name="my_company_name" id="postCardCompanyName" onclick="scompanyList(this.value,'postCardCompanyList','postCardCompanyName','postCardCompanyKey')" onkeyup="scompanyList(this.value,'postCardCompanyList','postCardCompanyName','postCardCompanyKey')" autocomplete="off" placeholder="请输入所属公司" value=""> <section class="scompany-list" id="postCardCompanyList" style="position: absolute;width: 427px"></section> <span msgfor="my_company_name"></span> </div> </div> <div class="form-group"> <label class="col-pre">职位<span class="redstar">*</span></label> <div class="col-after"> <input type="text" class="form-control" name="position" placeholder="请输入公司职位" value=""> <span msgfor="position"></span> </div> </div> <div class="form-group"> <label class="col-pre">电话<span class="redstar">*</span></label> <div class="col-after"> <input type="hidden" name="phone_prefix" value=""> <input type="text" class="form-control" name="phone" value="" placeholder="请输入联系电话" value=""> <span msgfor="phone"></span> </div> </div> <div class="form-group"> <label class="col-pre">邮箱<span class="redstar">*</span></label> <div class="col-after"> <input type="text" class="form-control" name="email" value="" placeholder="请输入联系邮箱" value=""> <span msgfor="email"></span> </div> </div> <div class="form-group"> <div class="col-all"> <p class="ts">发送的名片将以APP通知或邮件形式送达指定企业，禁止发布广告、骚扰等无关信息。如收到举报并核实，企查查有权永久封禁被举报账号。</p> </div> </div> </div> <div class="modal-body postcard-tep2"> <div class="postcard-wrap"> <div class="pcard-content"> <div class="clearfix"> <div class="col-ft"> <div class="img"> <img id="postcardImg" onerror="this.src='/material/theme/chacha/cms/v2/images/default_face.png'"> </div> </div> <div class="col-bd"> <div class="title"> <h4 id="postcardName">雷军</h4> <span id="postCardCompany">小米科技有限责任公司</span> </div> </div> </div> <div class="clearfix m-t-sm"> <span class="des">职位：</span> <span id="postCardPostion" class="value">CEO</span> </div> <div class="clearfix m-t-xs"> <span class="des">电话：</span> <span id="postCardPhone" class="value">13872119231</span> </div> <div class="clearfix m-t-xs"> <span class="des">邮箱：</span> <span id="postCardEmail" class="value">leijun@xiaomi.com</span> </div> </div> </div> <div class="form-group m-t-md"> <div class="col-all"> <textarea style="resize: none;" rows="3" name="cooperation_intention" class="form-control" placeholder="请输入合作意向，详细介绍你的合作意向，有助于推动对方快速联系你"></textarea> <span msgfor="cooperation_intention"></span> </div> </div> <div class="form-group"> <div class="col-all"> <p class="ts">发送的名片将以APP通知或邮件形式送达指定企业，禁止发布广告、骚扰等无关信息。如收到举报并核实，企查查有权永久封禁被举报账号。</p> </div> </div> </div> <div class="modal-footer"> <input type="hidden" name="to_company_keyno" value="182249d7736fdb68960201022c19647a"> <input type="hidden" name="to_company_email" value="1679705234@qq.com"> <input type="hidden" name="to_company_name" value="深圳市比一比网络科技有限公司"> <button type="button" onclick="postcardTep(2)" class="btn btn-primary postcard-tep1">下一步</button> <a href="/user_setting?from=f" class="btn btn-default postcard-tep2">修改信息</a> <button type="submit" class="btn btn-primary postcard-tep2">发送名片</button> </div> </form> <form class="pform-uploadimg" enctype="multipart/form-data" id="uploadFaceImg"> <input type="file" id="faceImg" name="pic"> </form> </div> </div> </div> <div class="modal fade" id="toSettingModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal sm"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">提示</h4> </div> <div class="modal-body"> <div class="pnodata lg"> <img src="/material/theme/chacha/cms/v2/images/nno_image.png"> <p>投递名片，请先完善邮箱及个人信息</p> </div> </div> <div class="modal-footer"> <a href="/user_setting?from=f" class="btn btn-primary">去设置</a> </div> </div> </div> </div> <div class="modal fade" id="phoneModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal" style="width: 400px"> <div class="modal-content qy-modal"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">更多号码</h4> </div> <div class="modal-body"> <div class="opercor-lvip"><p>更多号码 只对VIP开放哦</p><a href="/vip" target="_blank" class="btn btn-primary">立即开通</a></div> </div> </div> </div> </div> <div class="modal fade" id="zhixingModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="zhixingModalLabel">被执行人详情</h4> </div> <div class="modal-body"> <div id="zhixingview"></div> </div> </div> </div> </div> <div class="modal fade" id="shixinModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="shixinModalLabel">失信被执行人详情</h4> </div> <div class="modal-body"> <div id="shixinview"></div> </div> </div> </div> </div> <div class="modal fade" id="ktnoticeModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="ktnoticeModalLabel">开庭公告详情</h4> </div> <div class="modal-body"> <div id="ktggview"></div> </div> </div> </div> </div> <div class="modal fade" id="wenModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="wenModalModalLabel">裁判文书详情</h4> </div> <div class="modal-body"> <div id="wsview"></div> </div> </div> </div> </div> <div class="modal fade" id="gonggaoModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="gonggaoModalLabel">法院公告详情</h4> </div> <div class="modal-body"> <div id="gonggaoview"></div> </div> </div> </div> </div> <div class="modal fade" id="zzqModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="zzqModalModalLabel">著作权详情</h4> </div> <div class="modal-body"> <div class="zzqview"></div> <div class="clearfix"></div> </div> </div> </div> </div> <div class="modal fade" id="zhuxiaoModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">简易注销</h4> </div> <div class="modal-body"> <table class="ntable" id="flowlist"> <tr> <td class="tb" width="20%" rowspan="5">企业公告信息</td> <td>企业名称</td> <td>-</td> </tr> <tr> <td>统一社会信用代码/注册号</td> <td>-</td> </tr> <tr> <td>登记机关</td> <td>-</td> </tr> <tr> <td>公告期</td> <td>-</td> </tr> <tr> <td>全体投资人承诺书</td> <td>
                            -                        </td> </tr> <tr> <td class="tb" width="20%" rowspan="3">异议信息</td> <td>异议申请人</td> <td>-</td> </tr> <tr> <td>异议时间</td> <td>-</td> </tr> <tr> <td>异议内容</td> <td>-</td> </tr> <tr> <td class="tb" width="20%" rowspan="3">简易注销结果</td> <td>简易注销结果</td> <td>-</td> </tr> <tr> <td>公告申请日期</td> <td>-</td> </tr> </table> </div> </div> </div> </div> <div class="modal fade" id="noteModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">写笔记</h4> </div> <div class="modal-body"> <form class="form-horizontal" role="form"> <div class="form-group"> <div class="col-sm-12"> <textarea class="form-control noteContent" style="resize: vertical" rows="5" placeholder="亲爱的用户：请在这里填写您对该企业的笔记"></textarea> <span class="contentmsg text-danger"></span> </div> </div> <div class="form-group m-t-lg"> <div class="col-sm-12 text-center"> <input type="hidden" class="noteCompanykey" value="182249d7736fdb68960201022c19647a"/> <input type="hidden" class="noteCompanyname" value="深圳市比一比网络科技有限公司"/> <span class="btn btn-primary noteSubmit btn-block">提交</span> </div> </div> </form> </div> </div> </div> </div> <div class="modal fade" id="note2Modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal" style="width: 600px;"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">笔记</h4> </div> <div class="modal-body" style="padding: 20px;"> <div id="nNodeList" class="nnote-list"> </div> <div class="form-horizontal" role="form"> <div class="form-group"> <div class="col-sm-12"> <textarea class="form-control" id="nNoteContent" style="resize: none;" rows="5" placeholder="亲爱的用户：请在这里填写您对该企业的笔记"></textarea> <span class="contentmsg text-danger"></span> <input type="hidden" id="nNoteId" value=""/> </div> </div> </div> <div class="clearfix m-t-md m-b-sm"> <button onclick="noteSave('182249d7736fdb68960201022c19647a','深圳市比一比网络科技有限公司',this)" style="width: 82px;outline: none;" class="btn btn-primary pull-right">提交</button> </div> </div> </div> </div> </div> <div class="modal fade" id="reportModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content nmodal"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">下载报告</h4> </div> <div class="modal-body"> <section class="panel b-a buy_info"> <div class="panel-heading b-b"> <span class="font-bold font-15 text-dark">企业基础信用报告</span> </div> <div class="panel-body"> <div class="clear"> <div class="col-md-12 font-bold">报告内容：</div> <ul> <li class="col-md-4 m-t-sm module-content">基本信息</li> <li class="col-md-4 m-t-sm module-content">法律诉讼</li> <li class="col-md-4 m-t-sm module-content">企业风险</li> </ul> <ul> <li class="col-md-4 m-b-sm module-content">年报信息</li> <li class="col-md-4 m-b-sm module-content">知识产权</li> <li class="col-md-4 m-b-sm module-content">经营信息</li> </ul> <div class="col-md-12 m-t-md"> <div class="pull-left font-bold font-15  m-t-md text-danger">报告价格：免费 <span class="text-muted">（普通会员每天可以免费下载10份报告， <a href="/vip" target="_blank" class="text-primary">成为VIP,每天可以下载100份报告</a>）</span></div> <div class=" pull-right m-t-md"> <a class="btn btn-primary pull-right m-r" href="/report_free?companykey=182249d7736fdb68960201022c19647a" target="_blank">
                                        立即获取
                                    </a> </div> </div> </div> </div> </section> </div> </div> </div> </div> <input type="hidden" id="provice" name="provice" value=""> <input type="hidden" id="unique" name="unique" value="182249d7736fdb68960201022c19647a"> <input type="hidden" id="companyname" value="深圳市比一比网络科技有限公司"> <input type="hidden" id="companyid" name="companyid" value=""> <input type="hidden" id="brandcount" name="brandcount" value=""> <input type="hidden" id="companylogo" value=""> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/jquery.scrollTo.min.js"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/browser.js"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/jquery.scrollTo.js"></script> <script src="/material/theme/chacha/cms/v2/js/d3.min.js"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/company.js?version=20181109"></script> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/modalview.js?version=20181109"></script> <div class="modal fade" id="opercorModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal" style="width: 1170px"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="opercor ModalModalLabel">人物图谱</h4> </div> <div class="modal-body n-p"> <div id="opercorview"> </div> </div> </div> </div> </div> <div class="modal fade" id="guquanModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal" style="width: 1170px"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="guquanModalModalLabel">股权结构图</h4> </div> <div class="modal-body n-p"> <div style="height: 641px;" id="guquanview"></div> </div> </div> </div> </div> <div class="modal fade" id="investAgencyModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal" style="width: 1170px"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="investAgencyModalLabel">投资机构</h4> </div> <div class="modal-body"> <table class="ntable"> <tr> <th>序号</th> <th>机构图片</th> <th>投资机构</th> <th>城市</th> <th>简介</th> </tr> </table> </div> </div> </div> </div> <div class="modal fade" id="RelatModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal relat-modal"> <div class="modal-content relat-modal-list"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">被执行人详情</h4> </div> <div class="modal-body"> <section class="clear"> <div id="relatList"></div> </section> </div> </div> <div class="modal-content relat-modal-detail"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <a href="javascript:;" class="fa fa-chevron-left" onclick="backRelatList()"></a> <h4 class="modal-title"> 被执行人详情</h4> </div> <div class="modal-body"> <section class="clear"> <div class="tcaption">关联失信被执行人</div> <div id="relatDetail"> </div> </section> </div> </div> </div> </div> <script type="text/javascript">
function showRelatModal(tag,dataId) {
    $('#RelatModal').modal('show');
    var url = INDEX_URL+'/company_'+tag+'Relat';
    $.ajax({
        type:'GET',
        url:url,
        data:{
            id:dataId
        },
        dataType:"html",
        success:function(result){
            $('#relatList').html(result);
        }
    });
    if(tag=='zhixing'){
        $('.relat-modal-list .modal-title').text('被执行人详情');
        $('.relat-modal-detail .modal-title').text('被执行人详情');
    }else if(tag=='shixin'){
        $('.relat-modal-list .modal-title').text('失信被执行人详情');
        $('.relat-modal-detail .modal-title').text('失信被执行人详情');
    }else if(tag=='wenshu'){
        $('.relat-modal-list .modal-title').text('裁判文书详情');
        $('.relat-modal-detail .modal-title').text('裁判文书详情');
    }else if(tag=='ktnotice'){
        $('.relat-modal-list .modal-title').text('开庭公告详情');
        $('.relat-modal-detail .modal-title').text('开庭公告详情');
    }
    
  
}

function showRelatDetail(tag,dataId){
    $('.relat-modal-list').css('margin-left','-100%');
    $('.relat-modal-detail').css('margin-left','0px');
    if(tag=='zhixing'){
        zhixingView(dataId,true);
        $('.relat-modal-detail .tcaption').text('关联被执行人');
    }else if(tag=='shixin'){
        shixinView(dataId,true);
        $('.relat-modal-detail .tcaption').text('关联失信被执行人');
    }else if(tag=='wenshu'){
        wsView(dataId,true);
        $('.relat-modal-detail .tcaption').text('关联裁判文书');
    }else if(tag=='ktnotice'){
        ktnoticeView(dataId,true);
        $('.relat-modal-detail .tcaption').text('关联开庭公告');
    } 
}

function backRelatList(){
    $('.relat-modal-list').css('margin-left','0px');
    $('.relat-modal-detail').css('margin-left','100%');
}

$('#RelatModal').on('hidden.bs.modal', function () {
  $('.relat-modal-list').css('margin-left','0px');
  $('.relat-modal-detail').css('margin-left','100%');
  $('#relatList').empty();
  $('#relatDetail').empty();
});
</script> <style type="text/css">
#allmap {width: 100%;height: 600px;}
#mapPreview:hover{cursor:pointer;}
#mapModal .modal-dialog{
    width: 960px;
    margin: 30px auto;
}
</style> <script type="text/javascript" src="https://api.map.baidu.com/api?v=2.0&ak=U0QGae7viQsN0yLBirGsRD90XI0tlcGO&s=1"></script> <div class="modal fade" id="mapModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal lg"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="myModalLabel">完整地图</h4> </div> <div class="modal-body"> <div id="allmap"></div> </div> </div> </div> </div> <script type="text/javascript">
  var isLoadMap;
  // loadScript()
  function showMapModal(address,city,lat,lng){
      $('#mapModal').modal('show');
      if(isLoadMap != address){
          loadmap(address,city);
          isLoadMap = address;
      }
  }


  function loadScript() {  
      var script = document.createElement("script");  
      script.src = "https://api.map.baidu.com/getscript?v=2.0&ak=jYNU39RZ3k37NUz1QduizaYD&services=&t=20171014112628";  
      document.body.appendChild(script);  
  }  


  function loadmap (address,city,lat,lng) {
      /*弹窗大地图*/
      var map = new BMap.Map("allmap");
      map.addControl(new BMap.NavigationControl());
      map.addControl(new BMap.MapTypeControl());
      map.addControl(new BMap.OverviewMapControl());
      map.enableScrollWheelZoom(true);
      // 创建地址解析器实例
      var gc = new BMap.Geocoder();

      //$.colorbox({inline:true, href:"#baiduMap",title:"公司地址"});
      //var address = "深圳市南山区粤海街道高新技术园中区科苑大道讯美科技广场1栋3楼306";
      map.setCurrentCity(city);
      map.setZoom(12);
      
      gc.getPoint(address, function(point){
          if (point) {
              var p = new BMap.Point(point.lng, point.lat);
              var marker = new BMap.Marker(p);  // 创建标注
              map.addOverlay(marker);              // 将标注添加到地图中
              setTimeout(function(){
                  map.centerAndZoom(p, 15);
              },800);
              map.setZoom(14);
              if(address.length>16){
                address = address.substr(0,15)+'…';
              }
              var sContent =
                      "<h4 style='margin:0 0 5px 0;padding:0.2em 0'>"+city+"</h4>" +
                      "<p style='margin:0;line-height:1.5;font-size:13px;text-indent:0em'>"+address+"</p>" +
                      "</div>";
              var infoWindow = new BMap.InfoWindow(sContent);  // 创建信息窗口对象
              //图片加载完毕重绘infowindow
              marker.openInfoWindow(infoWindow);
          }else{
              faldia({'content':'无法在地图上找到该公司地址'});
          }
      }, city);
  }
</script> <script type="text/javascript">

    function checkWord(dom){
        $('#inputLimit').show();
        $('#inputLimit>span').text(dom.value.length);
    }

    function deputeLoad(iframe){
        var html = iframe.contentWindow.document.getElementsByTagName('html')[0];
        $(html).css('transform-origin','0% 0%');
        $(html).css('transform','scale(0.55)');
        $(html).css('-ms-transform-origin','0% 0%');
        $(html).css('-ms-transform','scale(0.55)');
        $(html).css('-webkit-transform-origin','0% 0%');
        $(html).css('-webkit-transform','scale(0.55)');
        $(html).css('-moz-transform-origin','0% 0%');
        $(html).css('-moz-transform','scale(0.55)');
    }

</script> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/footer.css?time=20181109" type="text/css"/> <link rel="stylesheet" href="/material/theme/chacha/cms/v2/css/animate.css?time=1508428800" type="text/css"/> <footer class="footer"> <div class="container"> <div class="footer-top clearfix"> <div class="about" style=""> <h4>关于我们</h4> <ul class="list-unstyled"> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'联系我们'});" href="/cms?id=13">联系我们</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'用户协议'});" href="/cms?id=14">用户协议</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'用户隐私权'});" href="/cms?id=15">用户隐私权</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'友情链接'});" href="/cms?id=16">友情链接</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'关于我们'});" href="/cms?id=892">关于我们</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'用户帮助'});" href="/cms?id=14578">用户帮助</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'名词百科'});" href="/cms?id=146498">名词百科</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'产品标签'});" href="/cms?id=146499">产品标签</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'更新记录'});" href="/cms?id=146500">更新记录</a></li> </ul> </div> <div class="contact"> <h4>联系方式</h4> <ul class="list-unstyled"> <li>企查查官方电话：400-928-2212</li> <li>官方客服QQ：<a target="_blank" href="http://wpa.b.qq.com/cgi/wpa.php?ln=1&key=XzkzODA0NDMwM180ODcyNjFfNDAwOTk4NTIxMl8yXw">4009985212</a></li> <li>客服邮箱：<a href="mailto:kf@qichacha.com">kf@qichacha.com</a></li> <li>微信客服：qccgf1234</li> <li>微信公众号：qcc365</li> <li>地址：江苏省苏州市工业园区东长路88号2.5产业园C1幢5楼</li> </ul> </div> <div class="service" style=""> <h4>查查服务</h4> <ul class="list-unstyled"> <li> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'500强企业'});" href="https://www.qichacha.com/cms_top500" target="_blank" >500强企业</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'权查查'});" href="http://www.qccip.com/" target="_blank" >权查查</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'客找找'});" href="http://www.kezhaozhao.com/" target="_blank" >客找找</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'疫苗查查'});" href="http://ai.qichacha.com/" target="_blank" >疫苗查查</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'融资查询'});" href="https://www.qichacha.com/elib_financing" target="_blank" >融资查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企风控'});" href="http://www.qifengkong.com/a/login?source=websiteFoot" target="_blank" >企风控</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业库'});" href="http://www.qichacha.com/elib" target="_blank" >企业库</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'裁判文书查询'});" href="http://www.qichacha.com/more_wenshus" target="_blank" >裁判文书查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'新三板企业查询'});" href="http://sanban.qichacha.com" target="_blank" >新三板企业查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'上市企业查询'});" href="http://ipo.qichacha.com/" target="_blank" >上市企业查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查企业查询'});" href="https://www.qichacha.com/gongsi" target="_blank" >企查查企业查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查移动版'});" href="https://m.qichacha.com" target="_blank" >企查查移动版</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查社区'});" href="https://www.qichacha.com/dianping" target="_blank" >企查查社区</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业风险搜索'});" href="https://www.qichacha.com/more_shixins" target="_blank" >企业风险搜索</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'商标专利搜索'});" href="https://www.qichacha.com/more_brands" target="_blank" >商标专利搜索</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业网址导航'});" href="https://www.qichacha.com/daohang" target="_blank" >企业网址导航</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业高管查询'});" href="https://www.qichacha.com/boss" target="_blank" >企业高管查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业税号查询'});" href="https://www.qichacha.com/tax" target="_blank" >企业税号查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业新闻头条'});" href="https://www.qichacha.com/news" target="_blank" >企业新闻头条</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业大数据导航'});" href="https://hao.qichacha.com" target="_blank" >企业大数据导航</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查下载'});" href="https://www.qichacha.com/weixin" target="_blank" >企查查下载</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业失信查询'});" href="https://www.qichacha.com/more_shixins" target="_blank" >企业失信查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查接口平台'});" href="http://www.yjapi.com/?from=qichacha" target="_blank" rel="nofollow">企查查接口平台</a> <a href="/yellowpage">公司黄页</a> <a href="/cms_dirhot">人员名录</a> <a href="http://open.qichacha.com" target="_blank"> 开放平台</a> </li> </ul> </div> <div class="qrcode"> <div class="qrcode-item"> <img src="/material/theme/chacha/cms/v2/images/v3/code_xcx.png?t=3" alt="企查查APP下载"> <span class="ma_xcx">小程序</span> </div> <div class="qrcode-item"> <img src="/material/theme/chacha/cms/v2/images/v3/code_app.png?t=3" alt="企查查APP下载"> <span class="ma_app">扫码下载APP</span> </div> <div class="qrcode-item"> <img src="/material/theme/chacha/cms/v2/images/v3/code_wx.png?t=3" alt="企查查微信公众号"> <span class="ma_wx">微信公众号</span> </div> </div> </div> <div class="footer-link"> <div class="footer-row clearfix"> <div class="footer-row-head">
                    数据来源：
                </div> <div class="footer-row-content"> <span class="item">全国企业信用信息公示系统</span> <span class="item">中国裁判文书网</span> <span class="item">中国执行信息公开网</span> <span class="item">国家知识产权局</span> <span class="item">商标局</span> <span class="item">版权局</span> </div> </div> <div class="footer-row clearfix"> <div class="footer-row-head">
                    热点省份：
                </div> <div class="footer-row-content"> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'安徽企业'});" href="http://ah.qichacha.com" target="_blank">安徽企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'北京企业'});" href="http://bj.qichacha.com" target="_blank">北京企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'重庆企业'});" href="http://cq.qichacha.com" target="_blank">重庆企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'福建企业'});" href="http://fj.qichacha.com" target="_blank">福建企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'甘肃企业'});" href="http://gs.qichacha.com" target="_blank">甘肃企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'广东企业'});" href="http://gd.qichacha.com" target="_blank">广东企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'广西企业'});" href="http://gx.qichacha.com" target="_blank">广西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'贵州企业'});" href="http://gz.qichacha.com" target="_blank">贵州企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'海南企业'});" href="http://hain.qichacha.com" target="_blank">海南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'河北企业'});" href="http://hb.qichacha.com" target="_blank">河北企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'黑龙江企业'});" href="http://hlj.qichacha.com" target="_blank">黑龙江企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'河南企业'});" href="http://hen.qichacha.com" target="_blank">河南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'湖北企业'});" href="http://hub.qichacha.com" target="_blank">湖北企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'湖南企业'});" href="http://hun.qichacha.com" target="_blank">湖南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'江苏企业'});" href="http://js.qichacha.com" target="_blank">江苏企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'江西企业'});" href="http://jx.qichacha.com" target="_blank">江西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'吉林企业'});" href="http://jl.qichacha.com" target="_blank">吉林企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'辽宁企业'});" href="http://ln.qichacha.com" target="_blank">辽宁企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'内蒙古企业'});" href="http://nmg.qichacha.com" target="_blank">内蒙古企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'宁夏企业'});" href="http://nx.qichacha.com" target="_blank">宁夏企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'青海企业'});" href="http://qh.qichacha.com" target="_blank">青海企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'山东企业'});" href="http://sd.qichacha.com" target="_blank">山东企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'上海企业'});" href="http://sh.qichacha.com" target="_blank">上海企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'山西企业'});" href="http://sx.qichacha.com" target="_blank">山西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'陕西企业'});" href="http://sax.qichacha.com" target="_blank">陕西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'四川企业'});" href="http://sc.qichacha.com" target="_blank">四川企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'天津企业'});" href="http://tj.qichacha.com" target="_blank">天津企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'新疆企业'});" href="http://xj.qichacha.com" target="_blank">新疆企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'西藏企业'});" href="http://xz.qichacha.com" target="_blank">西藏企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'云南企业'});" href="http://yn.qichacha.com" target="_blank">云南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'浙江企业'});" href="http://zj.qichacha.com" target="_blank">浙江企业</a> </div> </div> </div> </div> </div> <div class="footer-copy-bg"> <div class="container"> <div class="footer-copy clearfix"> <div class="pull-left"> <div class="m-t-sm">交流QQ群：
                        <span>928689619</span> <span>&nbsp;&nbsp;&nbsp;467569586(已满)</span> <span>&nbsp;369254293(已满)</span> <span>&nbsp;257048933(已满)</span> <span>&nbsp;259189047(已满)</span> <span>&nbsp;371601207(已满)</span> </div> <div class="m-t-xs"> <a href="javascript:void(0)" title="企查查">&copy;2014-2018</a> <a href="http://www.miibeian.gov.cn/" target="_blank"> 苏ICP备15042526号-4</a>
                        版权所有&nbsp;苏州朗动网络科技有限公司
                        &nbsp;增值电信业务经营许可证：<a href="http://jscainfo.miitbeian.gov.cn/state/outPortal/loginPortal.action" rel="nofollow" target="_blank">苏ICP证B2-20180251</a> </div> </div> <div class="auth"> <a href="https://ss.knet.cn/verifyseal.dll?sn=e17091132050068868mhtm000000&comefrom=trust" rel="nofollow" target="_blank"> <img class="m-l-sm" style="width: 128px" src="/material/theme/chacha/cms/v2/images/dependable.png"/> </a> <a href="http://www.jsdsgsxt.gov.cn/mbm/entweb/elec/certView.shtml?siteId=2f2c5b85a5154355a56eb3dee98ad8a3" rel="nofollow" target="_blank"> <img class="m-l-sm" style="width: 50px" src="/material/theme/chacha/cms/v2/images/jsdsgsxt.png"/> </a> <a href="https://v.pinpaibao.com.cn/cert/site/?site=www.qichacha.com&at=official" rel="nofollow" target="_blank"> <img class="m-l-sm" style="width: 124px;" src="https://static.anquan.org/static/outer/image/gw_124x47.png"/> </a> </div> </div> </div> </div> </footer> <div class="modal fade" id="feedModal" tabindex="-1" role="dialog" style="overflow: hidden;" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal nmodal-sm"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="myModalLabel">意见反馈</h4> </div> <div class="modal-body"> <form class="form-horizontal" role="form"> <div class="form-group"> <label for="inputEmail3" class="col-sm-2">反馈内容</label> <div class="col-sm-10"> <textarea class="form-control content" rows="5"  name="content" placeholder="亲爱的用户：请在这里直接填写您遇到的问题或意见建议，您的意见是我们前进的动力"></textarea> <span class="contentmsg text-danger"></span> </div> </div> <div class="form-group"> <label for="inputPassword3" class="col-sm-2">联系方式</label> <div class="col-sm-10"> <input type="text" class="form-control email" name="email" placeholder="请输入邮箱，方便我们联系您。"> <span class="emailmsg text-danger"></span> </div> </div> <div class="form-group"> <div class="col-sm-10 col-sm-offset-2"> <label>亲爱的顾客，您也可以直接拨打企查查官方电话：400-928-2212 或者 联系企查查官方客服QQ：4009985212，我们将及时为您解答问题。</label> </div> </div> <div class="form-group m-t-lg"> <label for="inputPassword3" class="col-sm-2"></label> <div class="col-sm-10  text-center"> <span class="btn btn-primary btn-guest btn-block">提交反馈</span> </div> </div> </form> </div> </div> </div> </div> <div style="display:none;"> <script src="https://s4.cnzz.com/z_stat.php?id=1254842228&web_id=1254842228" language="JavaScript"></script> <script>
      var _hmt = _hmt || [];
      (function() {
          var hm = document.createElement("script");
          hm.src = "https://hm.baidu.com/hm.js?3456bee468c83cc63fb5147f119f1075";
          var s = document.getElementsByTagName("script")[0];
          s.parentNode.insertBefore(hm, s);
      })();
  </script> <script>(function(){
          var src = (document.location.protocol == "http:") ? "http://js.passport.qihucdn.com/11.0.1.js?db135ad770b0860a90c3a2ca38cf577c":"https://jspassport.ssl.qhimg.com/11.0.1.js?db135ad770b0860a90c3a2ca38cf577c";
          document.write('<script src="' + src + '" id="sozz"><\/script>');
      })();
  </script> </div> <div class="modal fade" id="noteEditModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">编辑笔记</h4> </div> <div class="modal-body"> <form class="form-horizontal" role="form"> <div class="form-group"> <div class="col-sm-12"> <textarea class="form-control noteEditContent noteDetail" data-id="" rows="5" placeholder="亲爱的用户：请在这里填写您对该企业的笔记"></textarea> <span class="contentmsg text-danger"></span> </div> </div> <div class="form-group m-t-lg"> <div class="col-sm-12 text-center"> <span class="btn btn-primary  btn-block noteEditSubmit">提交</span> </div> </div> </form> </div> </div> </div> </div> <script type="text/javascript">
    function noteDetail(id){
        $.get(INDEX_URL+'/user_noteDetail', {id:id} ,function(result){
            if(result.success){
                $('.noteDetail').val(result.content);
                $('.noteDetail').attr('data-id',id);
            }
        });
    }

    //编辑笔记
    $('.noteEditSubmit').on('click',function(){
        var id = $(".noteEditContent").attr('data-id');
        var content = $.trim($(".noteEditContent").val());
        if(content==""){
            faldia({content:"请输入内容！"});
            return false;
        }
        $.ajax({
            type: 'POST',
            url:INDEX_URL+'/user_editNote',
            data:{id:id,content:content},
            success: function(result){
                if(result.success){
                    sucdia({content:"编辑成功！"});
                    $(".noteEditContent").val('');
                    window.location.reload();
                }else{
                    faldia({content:"编辑失败！"});
                }
            }
        });
    });
</script> <script type="text/javascript">
    (function(){
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
</script> <link rel="stylesheet" type="text/css" href="/material/theme/chacha/cms/v2/css/rnav.css?timestamp=20181109"> <div id="RNav" class="visible-lg i_hide"> <div class="i_menu"> <ul class="i_bts-outer" style="bottom:69px;"> <li onclick="zhugeTrack('企业主页-对比企业',{'企业名称':'深圳市比一比网络科技有限公司'});" class="i_bt_lg i_bt_com i_to-option spanHide i_bt_xy" to="RNCom"> <i></i> <label>对比</label><span style="display: none;" id="ComCount">0</span></li> <li class="i_bt_sm i_bt_xcx"><i></i> <label>小程序</label><img src="/material/theme/chacha/cms/v2/images/leftnav/bg_xcx.png?t=2" alt="企查查"></li> <li class="i_bt_sm i_bt_wx"><i></i> <label>公众号</label><img src="/material/theme/chacha/cms/v2/images/leftnav/bg_wx.png?t=2" alt="企查查"></li> <li onclick="zhugeTrack('下载APP悬浮按钮');" class="i_bt_sm i_bt_dow"><i></i> <label>下载</label><img src="/material/theme/chacha/cms/v2/images/leftnav/bg_app.png?t=3" alt="企查查"></li> <script type="text/javascript" src="/material/js/jquery.cookie.js"></script> <script type="text/javascript" src="/material/js/jquery.validate.min.js"></script> <script type="text/javascript" src="/material/js/jquery.form.min.js"></script> <script type="text/javascript" src="/material/js/global.js?t=33"></script> <li id="RNBack" class="i_bt_sm i_bt_back" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><i></i> <label>反馈</label></li> <li class="i_bt_sm i_bt_kf" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><i></i> <label>客服</label></li> <li id="RNTop" class="i_bt_sm i_bt_top"><i></i> <label>置顶</label></li> </ul> </div> <div class="i_container"> <div class="i_nodata">暂无数据</div> <div id="RNFoc" class="i_wrap"> <div class="i_title">我的关注</div> <div class="i_com-wrap"> <div style="height:1px;width:240px;"></div> </div> <div class="i_botbt"> <a href="/user_follow">打开全部</a> </div> </div> <div id="RNCom" class="i_wrap"> <div class="i_title">企业对比</div> <div class="i_toast">
				还可以添加<span id="ComLastCount">5</span>家企业 
				<a id="ClearCompares" class="c_a">清空</a> </div> <div class="i_com-wrap"> <div class="i_com i_addcom" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"> <img src="/material/theme/chacha/cms/v2/images/leftnav/icon-add.png" alt="企查查"/> <a class="c_a" href="javascript:;">添加企业</a> </div> <div style="height:1px;width:240px;"></div> </div> <div class="i_botbt"> <a href="javascript:;" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">对比企业</a> </div> </div> <div id="RNRel" class="i_wrap"> <div class="i_title">找关系</div> <div class="i_toast">
				还可以添加<span id="RelLastCount">5</span>家企业 
				<a class="c_a" id="ClearRels">清空</a> </div> <div class="i_com-wrap"> <div class="i_com i_addcom" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"> <img src="/material/theme/chacha/cms/v2/images/leftnav/icon-add.png" alt="企查查"/> <a class="c_a" href="javascript:;">添加企业或个人</a> </div> <div style="height:1px;width:240px;"></div> </div> <div class="i_botbt"> <a href="javascript:;" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">找关系</a> </div> </div> </div> <div class="modal fade" id="qaddComPanel" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content" style="width:600px;"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">添加企业</h4> </div> <div class="modal-body" style="height: 330px"> <form class="form-horizontal" role="form"> <div class="form-group"> <div class="col-sm-12 m-t-md"> <input type="text" id="qcomName" name="comName" class="form-control" value="" placeholder="请输入公司/人" autocomplete="off" oninput="qsearchCom(event,this)"/> <section class="panel hidden-xs" id="qsearchList" style="position: absolute;width: 560px;z-index: 10;display: none;"></section> </div> <div class="col-sm-12 text-center m-t-lg" style="padding-left: 18px;padding-right: 18px;"> <span id="qaddComPanelConfirm" class="btn-primary btn-guest btn-block" style="padding-top: 5px;padding-bottom: 5px;cursor:pointer;">添加企业</span> </div> </div> </form> </div> </div> </div> </div> <div class="modal fade" id="addRelPanel" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content" style="width:600px;"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">添加企业或个人</h4> </div> <div class="modal-body" style="height: 445px"> <form class="form-horizontal" role="form"> <div class="form-group"> <div class="col-sm-12 m-t-md"> <input type="text" id="qrcomName" name="comName" class="form-control" value="" placeholder="请输入公司名称" autocomplete="off" oninput="qrsearchCom(event,this)"/> <section class="panel hidden-xs" id="qrsearchList" style="position: absolute;width: 560px;z-index: 10;display: none;"></section> </div> </div> </form> </div> </div> </div> </div> </div> <script type="text/javascript">
	 /*rightNav.js 使用变量*/
	 var personImg =  "/material/theme/chacha/cms/v2/images/leftnav/person.png";
	 var frimUrl = "";
	 var comDefaultImg = "/material/theme/chacha/cms/v2/images/company.jpg"
          
    function jumpTax(){
        window.location.href=encodeURI(INDEX_URL+"tax");
    }       
</script> <script src="/material/theme/chacha/cms/v2/js/rightNav.js?timestamp=1497542400"></script> <link type="text/css" href="/material/theme/chacha/cms/v2/css/login.css?version=20181109" rel="stylesheet" /> <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" data-backdrop="static"> <div class="modal-dialog login-madal-dialog"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="myModalLabel">登录企查查</h4> </div> <div class="modal-body"> <div class="login-sao-panel"> <div class="title">扫码登录请使用<br> <a href="/app" target="_blank" class="text-primary">企查查APP</a> > 我的 > 扫一扫</div> <div class="qrcodewrap"> <div class="qrcode" id='qrcodeModalLogin'></div> <img class="qrcodets" src="/material/theme/chacha/cms/v2/images/qrcode_ts.png"> </div> <div class="tip"><span></span> 扫一扫功能支持企查查 APP11.0.6 及以上版本</div> </div> <div class="login-panel" style="display: none;" id="normalLoginPanel"> <div class="login-panel-head clearfix"> <div class="login-tab"> <a href="javascript:;" id="verifyLogin">快捷登录</a> </div> <div class="login-tab"> <a href="javascript:;" class="active">密码登录</a> </div> </div> <div class="login-panel-body"> <form class="form-group login-form" role="form" id="user_login_normal"> <div class="form-group"> <input type='hidden' class='phone_prefix_input' value="+86" name='phone_prefix' /> <div class="phone-select dropdown"> <a class="phone_prefix" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"> 中国 +86<b class="caret text-primary"></b></a> <div class="phoneline"></div> <ul class="phone_prefix_ul dropdown-menu"></ul> </div> <input id="nameNormal" name="nameNormal" type="text" class="form-control form-control-error" placeholder="请输入手机号码"> <span msgfor="nameNormal"></span> </div> <div class="form-group m-t-md"> <div class="show-pwd"></div> <input id="pwdNormal" name="pwdNormal" type="password" class="form-control form-control-error" placeholder="请输入密码"> <span msgfor="pwdNormal"></span> </div> <div class="form-group m-t-md"> <div id="dom_id_one"></div> </div> <div class="checkbox m-t-md"> <label class="text-dark-lter"> <input type="checkbox" name="keep" checked="checked" value="option1"> 一周内保持登录状态
                                </label> </div> <button type="submit" class="btn btn-primary btn-block m-t-md login-btn"> <strong>立即登录</strong></button> <input type='hidden' id='csessionid_one' name='csessionid_one' /> <input type='hidden' id='sig_one' name='sig_one' /> <input type='hidden' id='token_one' name='token_one' /> <input type='hidden' id='scene_one' name='scene_one' /> <input type='hidden' name='verify_type' value="1" /> </form> <div class="login-other m-t-md"> <div class="clearfix"> <div class="pull-left"> <a href="/user_register" class="text-primary">账号注册</a> </div> <div class="pull-left text-dark-lt m-l-sm"> <a href="/user_forgetpassword">忘记密码？</a> </div> <div class="pull-right"> <a href="https://open.weixin.qq.com/connect/qrconnect?appid=wx9b26295cdfab4175&redirect_uri=http://www.qichacha.com/user_wxloginok?back=&response_type=code&scope=snsapi_login&state=#wechat_redirect" class="btn-wx"></a> <a href="/user_qqlogin?back=&replace=1" class="btn-qq m-l-xs"> </a> <a href="/user_weiboLogin" class="btn-weibo m-l-xs"> </a> </div> </div> </div> </div> </div> <div class="login-panel" id="verifyLoginPanel"> <div class="login-panel-head clearfix"> <div class="login-tab"> <a href="javascript:;" class="active">快捷登录</a> </div> <div class="login-tab"> <a href="javascript:;" id="normalLogin">密码登录</a> </div> </div> <div class="login-panel-body"> <form class="form-group login-form" role="form" id="user_login_verify"> <div class="form-group"> <input type='hidden' class='phone_prefix_input' value="+86" name='phone_prefix' /> <div class="phone-select dropdown"> <a class="phone_prefix" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"> 中国 +86<b class="caret text-primary"></b></a> <div class="phoneline"></div> <ul class="phone_prefix_ul dropdown-menu"></ul> </div> <input id="nameVerify" name="nameVerify" onkeyup="phoneKeyup()" oninput="phoneKeyup()" type="text" class="form-control form-control-error" placeholder="请输入手机号码"> <span msgfor="nameVerify"></span> </div> <div class="form-group m-t-md"> <div id="dom_id_two"></div> </div> <div class="form-group m-t-md"> <input id="vcodeNormal" maxlength="6" name="codeVerify" type="text" class="form-control form-control-error" placeholder="短信验证码"> <a href="javascript:;" class="text-primary vcode-btn get-mobile-code">
                         获取验证
                      </a> <span msgfor="codeVerify"> </span> </div> <div class="checkbox m-t-md"> <label class="text-dark-lter"> <input type="checkbox" name="keep" checked="checked" value="option1"> 一周内保持登录状态
                                </label> </div> <button type="submit" class="btn btn-primary btn-block m-t-md login-btn"> <strong>立即登录</strong></button> <input type='hidden' id='csessionid_two' name='csessionid_two' /> <input type='hidden' id='sig_two' name='sig_two' /> <input type='hidden' id='token_two' name='token_two' /> <input type='hidden' id='scene_two' name='scene_two' /> </form> <div class="login-other m-t-md"> <div class="clearfix"> <div class="pull-left"> <a onclick="" href="/user_register" class="text-primary">账号注册</a> </div> <div class="pull-left text-dark-lt m-l-sm"> <a onclick="" href="/user_forgetpassword">忘记密码？</a> </div> <div class="pull-right"> <a onclick="" href="https://open.weixin.qq.com/connect/qrconnect?appid=wx9b26295cdfab4175&redirect_uri=http://www.qichacha.com/user_wxloginok?back=&response_type=code&scope=snsapi_login&state=#wechat_redirect" class="btn-wx"></a> <a onclick="" href="/user_qqlogin?back=&replace=1" class="btn-qq m-l-xs"> </a> <a onclick="" routerLink="/user" class="btn-weibo m-l-xs"> </a> </div> </div> </div> </div> </div> </div> </div> </div> </div> <link type="text/css" href="//g.alicdn.com/sd/ncpc/nc.css?t=1520579483" rel="stylesheet" /> <script type="text/javascript" src="//g.alicdn.com/sd/ncpc/nc.js?t=1520579483"></script> <div id="_umfp" style="display:inline;width:1px;height:1px;overflow:hidden"></div> <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/login.js?version=20181109"></script> <script>

    //普通登录
    formset({
        "id":"user_login_normal",
        "url":"user_loginaction",
        "rule":{
            "nameNormal":{
                required:true,
            },
            "pwdNormal":{
                required:true,
                minlength:6
            }
        },

        "messages":{
            "nameNormal":{
                required:"请输入手机号",
            },
            "pwdNormal":{
                required:"请输入密码",
                minlength:"密码最少6位"
            }
        },
        "sucfunc":function(rs){
            $('#loginModalClose').click();
            location.reload();
        },
        "falfunc":function(rs){
            faldia({'content':'登录失败：'+rs.msg});
            getAliCaptcha('one');
            document.getElementById('csessionid_one').value = '';
            document.getElementById('sig_one').value = '';
            document.getElementById('token_one').value = '';
            document.getElementById('scene_one').value = '';
        }
    });
    //手机验证码登录
    formset({
        "id":"user_login_verify",
        "url":"user_loginbyverify",
        "rule":{
            "nameVerify":{
                required:true,
            },
            "codeVerify":{
                required:true,
                minlength:6
            }
        },

        "messages":{
            "nameVerify":{
                required:"请输入手机号",
            },
            "codeVerify":{
                required: "请输入手机激活码",
                minlength: "手机激活码最少{0}个字"
            }
        },
        "sucfunc":function(rs){
            $('#loginModalClose').click();
            location.reload();
        },
        "falfunc":function(rs){
            faldia({'content':'登录失败：'+rs.msg});
            getAliCaptcha('two');
            document.getElementById('csessionid_two').value = '';
            document.getElementById('sig_two').value = '';
            document.getElementById('token_two').value = '';
            document.getElementById('scene_two').value = '';
        }
    });

    var codeStatus = true;//状态
    var waitSec = 60; //设置秒数(单位秒)
    var i = 1;
    var clock;

    function sTimer() {
        var r = waitSec - i;
        if (r == 0) {
            clearInterval(clock);
            $(".get-mobile-code").html("重新获取");
            codeStatus = true;
            $(".get-mobile-code").data('clicked', false).removeClass('disabled');
        } else {
            $(".get-mobile-code").html("(" + r + ")秒重新发送");
            i++;
        }
    };
    function startClock(t) {
        codeStatus = false;
        i = parseInt(t);
        clock = setInterval(sTimer, 1000);
    }

    function phoneKeyup(){
      
    }

    

    //获取手机验证码
    function mobileCode() {
        $(".get-mobile-code").bind('click', function () {
            if ($(this).data('clicked')) return false;
            var phone = $("input[name=nameVerify]").val();
            var scene = $("input[name='scene_two']").val();
            var token = $("input[name='token_two']").val();
            var sig = $("input[name='sig_two']").val();
            var csessionid = $("input[name='csessionid_two']").val();
            var phone_prefix = $("input[name='phone_prefix']").val();
            var afsFlag = '';

            if ($("input[name=nameVerify]").hasClass('validate-error')) {
                faldia('请重新输入手机号码！');
                return false;
            }

            if (!phone) {
                faldia('手机号码不能为空！');
                return false;
            }

            if(afsFlag){
                if(!scene || !token || !sig || !csessionid){
                    faldia('请先拖动滑块！');
                    return false;
                }
            }

            $.post(INDEX_URL + '/user_regmobileCode', {
                scene:scene,
                token:token,
                sig:sig,
                csessionid:csessionid,
                phone: phone,
                type: 4,
                verify_type:1,
                phone_prefix:phone_prefix
            }, function (data) {
                if (data.success) {
                    $("input[name=mobilecode]").removeAttr('disabled');
                    startClock(1);
                    $(".get-mobile-code").data('clicked', true).addClass('disabled').html("(" + waitSec + ")秒重新发送");
                } else {
                    faldia(data.msg);
                    getAliCaptcha('two');
                    $("input[name=mobilecode]").removeAttr('disabled');
                    $(".get-mobile-code").html("重新获取").data('clicked', false).removeClass('disabled');
                }
            }, 'json');
            return false;
        });
    }

    mobileCode();
</script> <script>

    function getCaptcha() {
        getAliCaptcha('two');

    }

    function getAliCaptcha(num){
        var renderDom = '#dom_id_'+num;
        var csessionidDom = 'csessionid_'+num;
        var sigDom = 'sig_'+num;
        var tokenDom = 'token_'+num;
        var sceneDom = 'scene_'+num;
        var nc = new noCaptcha();
        var nc_appkey = 'QNYX';  // 应用标识,不可更改
        var nc_scene = 'login';  //场景,不可更改
        var nc_token = [nc_appkey, (new Date()).getTime(), Math.random()].join(':');
        var nc_option = {
            renderTo: renderDom,
            appkey: nc_appkey,
            scene: nc_scene,
            token: nc_token,
            callback: function (data) {
                document.getElementById(csessionidDom).value = data.csessionid;
                document.getElementById(sigDom).value = data.sig;
                document.getElementById(tokenDom).value = nc_token;
                document.getElementById(sceneDom).value = nc_scene;
            }
        };
        nc.init(nc_option);
    }
    
    $('#verifyLogin').on('click',function(){
        getAliCaptcha('two');
        if($("input[name=nameNormal]").val()){
          $("input[name=nameVerify]").val($("input[name=nameNormal]").val());
        }else{
          setTimeout(function() {$("input[name=nameVerify]").focus();}, 10);
        }
        $('#verifyLoginPanel').show();
        $('#normalLoginPanel').hide();
        window.localStorage.setItem('logintype',0);
    });
    $('#normalLogin').on('click',function(){
        getAliCaptcha('one');
        if($("input[name=nameVerify]").val()){
          $("input[name=nameNormal]").val($("input[name=nameVerify]").val());
        }
        $('#normalLoginPanel').show();
        $('#verifyLoginPanel').hide();
        window.localStorage.setItem('logintype',1);
    });

    $.ajax({
        type: "get",
        url: "/material/theme/chacha/cms/v2/images/phoneCode.json",
        dataType: "json",
        success: function(data) {
            $('.phone_prefix_ul').empty();
            $('.phone_prefix_ul').append('<li onclick="pSelect(this)" value="+86"><span> 中国</span>+86</li>');
            $.each(data,function(i,v){
                $('.phone_prefix_ul').append('<li onclick="pSelect(this)" value="+'+v.country_code+'"><span> '+v.country_name_cn+'</span>+'+v.country_code+'</li>');
            })
        }
    });
    function pSelect(dom){
      var tname = $(dom).find('span').text();
      if(tname.length>5){
        tname = tname.substr(0,6)+'…';
      }
      $('.phone_prefix').html(tname+' +'+dom.value+'<b class="caret text-primary"></b>');
      $('.phone_prefix_input').val('+'+dom.value);
      var width = 58;
      if($('#verifyLoginPanel').is(':visible')){
        width = $('#verifyLoginPanel .phone_prefix').width();
      }else{
        width = $('#normalLoginPanel .phone_prefix').width();
      }
      $('.phoneline').css('left',width+18);
      $('.login-panel .phone-select+input').css('padding-left',width+27);
    }
    $('.show-pwd').click(function(){
        if($('.show-pwd').hasClass('active')){
            $('.show-pwd').removeClass('active');
            $('.show-pwd').next().attr('type','password');
        }else{
            $('.show-pwd').addClass('active');
            $('.show-pwd').next().attr('type','text');
        }
    });
    var loginJumpUrl;
    $('#loginModal').on('show.bs.modal', function (e) {
        loginQrcodeGenerate('qrcodeModalLogin');
        loginQrcodePoll('qrcodeModalLogin');
    })
    $('#loginModal').on('hidden.bs.modal', function (e) {
        clearInterval(loginQrcodePollTimer);
    })
    setLoginType();
</script> <style type="text/css">
    #vipModal .modal-dialog{
      width: 750px;
    }
    #vipModal .modal-content{
      height: 708px;
      border-radius: 0px;
      text-align: center;
      
    }
    #vipModal .close{
      color: #FFF;
      font-size: 40px;
      opacity: 0.8;
      font-weight: normal;
      margin-right: 10px;
    }
</style> <link type="text/css" href="/material/theme/chacha/cms/v2/css/vip.css?version=20181109" rel="stylesheet"/> <div class="modal fade" id="vipModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="vip-top"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <div class="vip-buy-panel"> <div class="vip-year-list clearfix"> <div data-id="17" class="vip-kuang vip-year active"> <div class="price"> <span>720元</span> <span style="color: #F9552A">/</span>
                                3年
                            </div> <div class="origin-price">原价：2160元</div> <div class="vip-rec"></div> </div> <div data-id="7" class="vip-kuang vip-year"> <div class="price"> <span>540元</span> <span style="color: #F9552A">/</span>
                                2年
                            </div> <div class="origin-price">原价：1440元</div> </div> <div data-id="6" class="vip-kuang vip-year"> <div class="price"> <span>360元</span> <span style="color: #F9552A">/</span>
                                1年
                            </div> <div class="origin-price">原价：720元</div> </div> </div> <a onclick="modalJumpVip()" class="vip-btn">立即开通</a> <div class="vip-publicity">支付后可开发票</div> </div> </div> <div class="vip-container"> <div class="table-caption"> <img style="width: 51px;" src="/material/theme/chacha/cms/v2/images/vip_tq@2x.png"><span>查企业、查老板、找关系</span> <a href="/vip" class="pull-right">查看全部></a> </div> <table class="vip-table table table-striped"> <tr> <td width="32%">功能介绍</td> <td class="vip-text-re" width="34%">VIP会员</td> <td width="34%">普通会员</td> </tr> <tr> <td class="vip-text-bl">查询结果显示条数</td> <td class="vip-text-re">5000条</td> <td>100(<a href="http://www.qichacha.com" target="_blank">Web端</a>)/40(<a href="http://www.qichacha.com/app" target="_blank">App端</a>)</td> </tr> <tr> <td class="vip-text-bl">查询结果数据下载</td> <td class="vip-text-re">10次/天（每次最多5000条）</td> <td><span class="x">×</span></td> </tr> <tr> <td class="vip-text-bl">老板查询</td> <td class="vip-text-re">不限次</td> <td><span class="x">×</span></td> </tr> <tr> <td class="vip-text-bl">历史信息</td> <td class="vip-text-re">不限次</td> <td><span class="x">×</span></td> </tr> <tr> <td class="vip-text-bl">雷达监控</td> <td class="vip-text-re">100家企业/100位人员</td> <td>100家企业</td> </tr> <tr> <td class="vip-text-bl">风险扫描</td> <td class="vip-text-re">不限次</td> <td><span class="x">×</span></td> </tr> <tr> <td class="vip-text-bl">更多号码</td> <td class="vip-text-re">不限次</td> <td><span class="x">×</span></td> </tr> </table> </div> <input name="goods_id" type="hidden" value="17"> </div> </div> </div> <script type="text/javascript">
    var vipModalTitle;
    var userid = '';
    function showVipModal(title){
        if(!userid){
          getCaptcha();
          $('#loginModal').modal('show');
          return;
        }

        if(title){
            $('#vipModal .title').text(title);
        }else{
            $('#vipModal .title').text('该功能 只对VIP开放哦');
        }
        vipModalTitle = title;
        $('#vipModal').modal('show');
    }

    function modalJumpVip(){
      location.href = INDEX_URL+'/vip?goods_id='+$("input[name='goods_id']").val();
      if(vipModalTitle){
        //zhugeTrack(vipModalTitle.split(' ')[0]+'-开通VIP');
      }else{
        //zhugeTrack('VIP弹框-开通VIP');
      }
    }

    $('.vip-year-list .vip-kuang').on('click',function(){
        $('.vip-year-list .vip-kuang').removeClass('active');
        $(this).addClass('active');
        var id = $(this).attr('data-id');
        $("input[name='goods_id']").val(id);
    });
</script> <div id="openSuspend" class="openSuspend" style="cursor:pointer;"></div> <div class="bottomSuspend" id="bottomSuspend" style="margin-left: -100%;background-image: url('https://co-image.qichacha.com/upload/chacha/img/20181107/1541554251418032.png');"> <div id="attendDownload" class="attendDownload" data-href="https://www.qichacha.com/weixin_jump?from=web<audio controls="controls" style="display:none;"></audio>"></div> <div id="closeSuspend" class="closeSuspend"></div> </div> <script type="text/javascript">
    bottomSus();
</script> <script type="text/javascript">
    var keyno = '182249d7736fdb68960201022c19647a';
    $.ajax({
        type:'get',
        url:INDEX_URL + '/tax_view',
        data:{keyno:keyno,ajaxflag:1},
        success:function(result){
            if(result.success){
                $('#fapiao-title .Name').text(result.data.Name || '暂无');
                $('#fapiao-title .CreditCode').text(result.data.CreditCode || '暂无');
                $('#fapiao-title .Address').text(result.data.Address || '暂无');
                $('#fapiao-title .PhoneNumber').text(result.data.PhoneNumber || '暂无');
                $('#fapiao-title .Bank').text(result.data.Bank || '暂无');
                $('#fapiao-title .Bankaccount').text(result.data.Bankaccount || '暂无');
                $('#fapiao-title .TaxView').show();
            }
        }
    })
</script> </body> </html>
"""
soup = BeautifulSoup(html, 'lxml')
crude_gudongxinxi = [_ for _ in soup.find('section', id='Sockinfo').find('table', class_="ntable ntable-odd").find_all('tr', recursive=False)]
for _ in crude_gudongxinxi:
    if _.find_all('td'):
        i = [i.text.replace('\n', ' ').replace(' ', '').replace('>', '') for i in _.find_all('td', recursive=False)]
        print(i)
        # num = _.find('td', class_='tx')
        # print(num)
        # print(_.find_all)





"""工商信息"""
# if soup.find('section', id='Cominfo'):
#     name = soup.find('h1').text
#     name = {'GongSiMing': name}
#     crude_gongshangxinxi = soup.find('section', id='Cominfo').find_all('table', class_='ntable')[1]
#     tr = crude_gongshangxinxi.find_all('tr')
#     td_1 = ['ZhuCeZiBen', 'ShiJiaoZiBen', 'JingYingZhuangTai', 'ChengLiRiQi', 'XinYongDaiMa', 'ShiBieHao',
#             'ZhuCeHao', 'ZuZhiJiGouDaiMa', 'GongSiLeiXing', 'SuoShuHangYe', 'HeZhunRiQi', 'DengJiJiGuan',
#             'SuoShuDiQu', 'YingWenMing', 'CengYongMing', 'CanBaoRenYuan', 'RenYuanGuiMo', 'YingYeQiXian',
#             'QiYeDiZhi', 'JingYingFanWei']
#     td_2 = []
#     for _ in tr:
#         for i in _.find_all('td', class_=''):
#             i = None if i.text.strip().replace('\n', '').replace(' ', '') == '-' \
#                 else i.text.strip().replace('\n', '').replace(' ', '')
#             td_2.append(i)
#     gongshangxinxi = dict(zip(td_1, td_2))
#     gongshangxinxi.update(name)
#     companybean.gong_shang_xin_xi.companyName = gongshangxinxi.get('GongSiMing')
#     companybean.gong_shang_xin_xi.companyId = re.search('firm_(.*?)\.', soup.find('link').attrs['href']).group(1)
#     companybean.gong_shang_xin_xi.registerId = gongshangxinxi.get('ZhuCeHao')
#     companybean.gong_shang_xin_xi.societyId = gongshangxinxi.get('XinYongDaiMa')
#     companybean.gong_shang_xin_xi.taxpayerId = gongshangxinxi.get('ShiBieHao')
#     companybean.gong_shang_xin_xi.orgCode = gongshangxinxi.get('ZuZhiJiGouDaiMa')
#     companybean.gong_shang_xin_xi.entType = gongshangxinxi.get('GongSiLeiXing')
#     companybean.gong_shang_xin_xi.industry = gongshangxinxi.get('SuoShuHangYe')
#     companybean.gong_shang_xin_xi.busStatus = gongshangxinxi.get('JingYingZhuangTai')
#     companybean.gong_shang_xin_xi.allMoney = gongshangxinxi.get('ZhuCeZiBen')
#     companybean.gong_shang_xin_xi.canUseMoney = gongshangxinxi.get('ShiJiaoZiBen')
#     if gongshangxinxi.get('ChengLiRiQi'):
#         companybean.gong_shang_xin_xi.regTime = datetime.datetime.strptime(gongshangxinxi.get('ChengLiRiQi'), "%Y-%m-%d")
#     companybean.gong_shang_xin_xi.optPeriod = gongshangxinxi.get('YingYeQiXian')
#     companybean.gong_shang_xin_xi.busScope = gongshangxinxi.get('JingYingFanWei')
#     companybean.gong_shang_xin_xi.regAuthority = gongshangxinxi.get('DengJiJiGuan')
#     if gongshangxinxi.get('HeZhunRiQi'):
#         companybean.gong_shang_xin_xi.appDate = datetime.datetime.strptime(gongshangxinxi.get('HeZhunRiQi'), "%Y-%m-%d")
#     companybean.gong_shang_xin_xi.busPlace = gongshangxinxi.get('QiYeDiZhi')
#     companybean.gong_shang_xin_xi.admArea = gongshangxinxi.get('SuoShuDiQu')
#     companybean.gong_shang_xin_xi.englishName = gongshangxinxi.get('YingWenMing')
#     companybean.gong_shang_xin_xi.usedName = gongshangxinxi.get('CengYongMing')
#     if gongshangxinxi.get('CanBaoRenYuan'):
#         companybean.gong_shang_xin_xi.contributorsSize = int(gongshangxinxi.get('CanBaoRenYuan'))
#     companybean.gong_shang_xin_xi.staffSize = gongshangxinxi.get('RenYuanGuiMo')

"""股东信息"""
# if soup.find('section', id='Sockinfo'):
#     gudongxinxi = []
#     gudongxinxi_title = []
#     crude_gudongxinxi_title = [_.text for _ in soup.find('section', id='Sockinfo')\
#         .find('table',class_="ntable ntable-odd").find_all('th')]
#     for _ in crude_gudongxinxi_title:
#         if '股东' in _:
#             gudongxinxi_title.append('shName')
#         if '持股比例' in _:
#             gudongxinxi_title.append('percentInfo')
#         if '认缴出资额' in _:
#             gudongxinxi_title.append('subMoney')
#         if '认缴出资日期' in _:
#             gudongxinxi_title.append('subDate')
#         if '实缴出资额' in _:
#             gudongxinxi_title.append('actMoney')
#         if '实缴出资日期' in _:
#             gudongxinxi_title.append('actDate')
#     crude_gudongxinxi = [_ for _ in soup.find('section', id='Sockinfo')
#         .find('table',class_="ntable ntable-odd").find_all('tr')]
#     for _ in crude_gudongxinxi:
#         if _.find_all('td'):
#             i = [None if i.text.replace('\n', ' ').replace(' ', '').replace('>', '') == '-'
#                  else i.text.replace('\n', ' ').replace(' ', '').replace('>', '')
#                  for i in _.find_all('td')]
#             gudongxinxi.append(i)
#     for _ in gudongxinxi:
#         _.pop(0)
#         for num, i in enumerate(_):
#             if i is None:
#                 continue
#             if '他关联' in i:
#                 _[num] = re.sub('他关联.*', '', i)
#
#     gudongxinxi_count = len(gudongxinxi)
#     gudongxinxi1 = companybean.GuDongXinXiBean()
#     for i in gudongxinxi:
#         for num, _ in enumerate(gudongxinxi_title):
#             if 'shName' == _:
#                 if i[num]:
#                     gudongxinxi1.shName = i[num]
#             if 'percentInfo' == _:
#                 if i[num]:
#                     gudongxinxi1.percentInfo = i[num]
#             if 'subMoney' == _:
#                 if i[num]:
#                     gudongxinxi1.subMoney = float(i[num])
#             if 'subDate' == _:
#                 if i[num]:
#                     gudongxinxi1.subDate = datetime.datetime.strptime(i[num], "%Y-%m-%d")
#             if 'actMoney' == _:
#                 if i[num]:
#                     gudongxinxi1.actMoney = float(i[num])
#             if 'actDate' == _:
#                 if i[num]:
#                     gudongxinxi1.actDate = datetime.datetime.strptime(i[num], "%Y-%m-%d")
#         companybean.lstGuDongXiXin.append(gudongxinxi1)
#         gudongxinxi1 = companybean.GuDongXinXiBean()

"""主要人员"""
# if soup.find('section', id='Mainmember'):
#     zhuyaorenyuan = []
#     zhuyaorenyuan_title = []
#     crude_zhuyaorenyuan_title = [_.text.replace('\n', '').replace(' ', '')
#                                 for _ in soup.find('section', id='Mainmember')
#                                             .find('table', class_="ntable ntable-odd").find_all('th')]
#     crude_zhuyaorenyuan = [_.find_all('td') for _ in
#                            soup.find('section', id='Mainmember')
#                                .find('table', class_="ntable ntable-odd").find_all('tr')]
#     for _ in crude_zhuyaorenyuan_title:
#         if '姓名' in _:
#             zhuyaorenyuan_title.append('personName')
#         if '职务' in _:
#             zhuyaorenyuan_title.append('position')
#     for _ in crude_zhuyaorenyuan:
#         if _:
#             zhuyaorenyuan.append([i.text.replace('\n', '').replace(' ', '') for i in _])
#     for _ in zhuyaorenyuan:
#         _.pop(0)
#         for num, i in enumerate(_):
#             if i is None:
#                 continue
#             if '他关联' in i:
#                 _[num] = re.sub('他关联.*', '', i)
#             if '-' == i:
#                 _[num] = None
#
#     zhuyaorenyuan1 = companybean.ZhuYaoRenYuanBean()
#     for i in zhuyaorenyuan:
#         for num, _ in enumerate(zhuyaorenyuan_title):
#             if 'personName' == _:
#                 if i[num]:
#                     zhuyaorenyuan1.personName = i[num]
#             if 'position' == _:
#                 if i[num]:
#                     zhuyaorenyuan1.position = i[num]
#         companybean.lstZhuYaoRenYuan.append(zhuyaorenyuan1)
#         zhuyaorenyuan1 = companybean.ZhuYaoRenYuanBean()

"""变更记录"""
# if soup.find('section', id='Changelist'):
#     biangengjilu = []
#     biangengjilu_title = []
#     crude_biangengjilu_title = [_.text for _ in
#                           soup.find('section', id='Changelist').find('table', class_="ntable").find_all('th')]
#     for _ in crude_biangengjilu_title:
#         if '变更日期' in _:
#             biangengjilu_title.append('changeDate')
#         if '变更项目' in _:
#             biangengjilu_title.append('changeProject')
#         if '变更前' in _:
#             biangengjilu_title.append('beforeChangeDetail')
#         if '变更后' in _:
#             biangengjilu_title.append('afterChangeDetail')
#
#     crude_biangengjilu = [_.find_all('td') for _ in
#                           soup.find('section', id='Changelist').find('table', class_="ntable").find_all('tr')]
#     for _ in crude_biangengjilu:
#         if _:
#             biangengjilu.append([i.text.replace('\n', '').replace(' ', '') for i in _])
#     for _ in biangengjilu:
#         _.pop(0)
#         for num, i in enumerate(_):
#             if i is None:
#                 continue
#             if '-' == i:
#                 _[num] = None
#
#     biangengjilu1 = companybean.BianGengJiLuBean()
#     for i in biangengjilu:
#         for num, _ in enumerate(biangengjilu_title):
#             if 'changeDate' == _:
#                 if i[num]:
#                     biangengjilu1.changeDate = datetime.datetime.strptime(i[num], "%Y-%m-%d")
#             if 'changeProject' == _:
#                 if i[num]:
#                     biangengjilu1.changeProject = i[num]
#             if 'beforeChangeDetail' == _:
#                 if i[num]:
#                     biangengjilu1.beforeChangeDetail = i[num]
#             if 'afterChangeDetail' == _:
#                 if i[num]:
#                     biangengjilu1.afterChangeDetail = i[num]
#         companybean.lstBianGengJiLu.append(biangengjilu1)
#         biangengjilu1 = companybean.BianGengJiLuBean()

# pprint(companybean.getDictWithoutNone())
# pprint(companybean.getDictAll())
# exit()


"""列表页解析"""
# for _ in soup.find('table',class_='m_srchList').find_all('tr'):
#     if _.find('a', class_='text-primary'):
#         name = _.find('a', class_="ma_h1").text
#         farendaibiao = _.find('a', class_='text-primary').text
#         try:
#             cid = urllib.parse.quote(_.find('a', class_="ma_h1").attrs['href'])
#             cid = cid.split('_')[1].split(".")[0]
#             cid = companybean.IDEncodeDecode(cid)
#         except KeyError:
#             cid = None
#         content_list = [_.text.replace('\n', '').replace(' ', '') for _ in _.find_all('span', class_='m-l')]
#         if re.search('注册资本：(.*?) ', ' '.join(content_list)):
#             zhuceziben = re.search('注册资本：(.*?) ', ' '.join(content_list)).group(1)
#         if re.search('股本：(.*?) ', ' '.join(content_list)):
#             zhuceziben = re.search('股本：(.*?) ', ' '.join(content_list)).group()
#         chenglishijian = re.search('成立时间：(.*?) ', ' '.join(content_list)).group(1)
#         dianhua = re.search('电话：(.*)', ' '.join(content_list)).group(1)
#         youxiang = re.search('邮箱：\s*(.*?)\s' ,_.text.replace(' ', '').replace('\n',' ')).group(1)
#         dizhi = re.search('地址：(.*?)\s', _.text.replace(' ', '').replace('\n', ' ')).group(1)
#         logo = _.find('img').attrs['src']
#         cunxuzhuangtai = _.find('span', class_='nstatus text-success-lt m-l-xs').text \
#             if _.find('span', class_='nstatus text-success-lt m-l-xs') else None
#         content_dict = {'name': name, 'farendaibiao': farendaibiao, 'cid': cid, 'zhuceziben': zhuceziben,
#                         'chenglishijian': chenglishijian, 'dianhua': dianhua, 'youxiang': youxiang,
#                         'dizhi': dizhi, 'cunxuzhuangtai': cunxuzhuangtai, 'logo': logo}
#     else:
#         continue

