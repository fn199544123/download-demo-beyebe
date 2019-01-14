# -*- coding:utf-8 -*-
import requests
import json
from pprint import pprint



html = r"""
<!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,Chrome=1"> <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no"> <meta name="renderer" content="webkit"> <meta name="author" content="leslie"> <title>比一比_企查查</title> <meta name="keywords" content="企查查,企业查询,公司查询,工商查询,企业信用信息查询系统,企业工商信息查询平台,企业财务信息查询,企业失信信息查询,启信宝,天眼查,天眼通"> <meta name="description" content="企查查信息来自国家企业信用信息公示系统，提供企业信息查询,工商查询,企业信用查询宝,公司查询等相关信息查询；帮您快速了解企业信息,企业工商信息,企业信用信息等经营和人员投资状况！"> <link rel="icon" href="https://www.qichacha.com/material/theme/chacha/cms/v2/images/favicon.png"> <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/bootstrap.css" type="text/css" /> <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/font-awesome.min.css" type="text/css" /> <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/icon.css" type="text/css" /> <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/font.css" type="text/css" /> <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/app.css?time=20181105" type="text/css" /> <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/common.css?time=20181105" type="text/css" /> <!--[if lt IE 9]>
    <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/app_ie8.css?time=1508428800" type="text/css" />
    <script src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/html5shiv.js"></script>
    <script src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/respond.js"></script>
    <![endif]--> <script type="text/javascript" src="https://www.qichacha.com/material/js/siteconfig.js"></script> <script src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/jquery.min.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/qrcode.min.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/jquery.scrollTo.js"></script> <script src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/bootstrap.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/js/echarts.min.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/china.js?time=1508428800"></script> <script type="text/javascript" src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/chartsUtil.js?time=20181105"></script> <script src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/slimscroll/jquery.slimscroll.min.js"></script> <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/toastr.css" /> <script type="text/javascript" src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/moment.js"></script> <script src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/toastr.js" type="text/javascript"></script> <script src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/custom.js?time=20181105"></script> <script type="text/javascript" src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/zhuge.js?time=20181105"></script> <script type="text/javascript">
    </script> <script type="text/javascript">
        var qrcodePolling = false;
    </script> </head> <body> <header class="header navi-header box-shadow"> <div class="container "> <div class="navi-brand"> <a onclick="zhugeTrack('主页-顶部-logo');" href="https://www.qichacha.com/" > <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/logo4.png" class="m-r-sm" alt="企查查"> </a> </div> <form class="navi-form" role="search" action="/search"> <div class="form-group"> <div class="input-group"> <input id="headerKey" name="key" onkeydown="searchKeydown(event,2);" class="form-control headerKey" style="font-size: 14px;" type="text" placeholder="请输入企业名称、人名，产品名等，多关键词用空格隔开，如“小米 雷军”" value="比一比" autocomplete="off"> <span class="input-group-btn" style="float: left"> <button onclick="" type="submit" class="btn btn-primary top-searchbtn"></button> </span> </div> </div> <section class="panel headerKey header-section" id="header-search-list"></section> </form> <script type="text/javascript">
                var pathname_ = window.location.pathname; 
                if(pathname_ == '/search_riskinfo' || pathname_ == '/search_intellectualinfo'){
                    $('#tpsearch').attr('action', pathname_);
                }
            </script> <ul class="navi-nav pull-right"> <li> <a onclick="zhugeTrack('主页-顶部-APP下载');" href="https://www.qichacha.com/app" class="dropdown-toggle header-qrcode">
                    APP下载
                  </a> <section class="dropdown-menu qrcode-box"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/header_qrcode@2x.png?t=2"> </section> </li> <li class="head-line">|</li> <li class=""> <a onclick="zhugeTrack('主页-顶部-VIP服务');" href="https://www.qichacha.com/vip">VIP服务</a> </li> <li class="head-line">|</li> <li><a onclick="" href="https://www.qichacha.com/user_login">登录</a></li> <li  class="head-line">|</li> <li><a onclick="" href="https://www.qichacha.com/user_register">免费注册</a></li> </ul> </div> </header> <script type="text/javascript" src="https://www.qichacha.com/material/js/jquery.cookie.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/js/jquery.validate.min.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/js/jquery.form.min.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/js/global.js?t=33"></script> <style>
    #excelTipsModal .modal-dialog,#filtrationModal .modal-dialog{
        width: 400px;
        margin: 30px auto;
    }
    #excelTipsModalBody{
        width: 100%;
        height: 60px;
    }
    
   
</style> <div id="V3_SL" class="container"> <div class="row"> <div class="col-md-9 no-padding"> <div style="padding-left: 15px;position: relative;"> <section class="panel b-a  no-shadow m-b"> <div class="clear m-t m-l m-r-lg"> <a class="proinv-scroll-btn prev disable" onclick="proinvScroll(0,this)"> </a> <div class="proinv-scroll" style="width: 1304px;"> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'<em>比一比</em>'});" href="https://www.qichacha.com/product_f594ec1e-f6eb-485b-9e95-6b180756aa3f.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/f594ec1e-f6eb-485b-9e95-6b180756aa3f.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name"><em>比一比</em></span> <span class="proinv-status">项目</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>不明确</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            比一比是一个电子元器件一站式在线交易平台，目前汇聚了国内外高端供应商500多家，电子元器件现货库存1200多万条。隶属于北京远大创新科技有限公司。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'深圳<em>比一比</em>'});" href="https://www.qichacha.com/product_cead27cc-bcba-42b2-8c61-527d292157c5.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/cead27cc-bcba-42b2-8c61-527d292157c5.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name">深圳<em>比一比</em></span> <span class="proinv-status">项目</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>不明确</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            深圳比一比是一家大数据提供商，是国家高新技术企业。公司以数据定制、数据仓库、数据分析，数据可视化等多维度的大数据应用服务为业务核心。数据服务对象涉及金融财经、医疗健康、商业经济、物流、环境、科学文化、企业信息等多个领域。
                        </div> </a> </div> <div class="proinv-wrap"> <a onclick="zhugeTrack('查企业-搜索列表页-查看投资机构/项目',{'投资机构/项目名称':'零<em>比一</em>'});" href="https://www.qichacha.com/product_b3049fd4-f5d4-4cdc-ba51-cfb5c9022621.html"> <div class="clearfix"> <div class="col-xs-2"> <div class="proinv-head"> <img src="https://img.qichacha.com/Product/b3049fd4-f5d4-4cdc-ba51-cfb5c9022621.jpg"> </div> </div> <div class="col-xs-10"> <div class="proinv-name m-l-sm"><span class="name">零<em>比一</em></span> <span class="proinv-status">项目</span></div> <div class="m-l-sm"> <span style="min-width: 140px;display: inline-block;"><span class="text-gray">融资信息：</span>不明确</span> <span class="text-gray">竞品信息：</span>20                                </div> </div> </div> <div class="m-t proinv-desc"> <span class="text-gray">简介：</span>
                            专业羽球装备商城，你所想的装备，都在这里。
                        </div> </a> </div> </div> <div class="prvinv-mengban"></div> <a class="proinv-scroll-btn next" onclick="proinvScroll(1,this)"></a> </div> </section> </div> <script type="text/javascript">
    var proinvScrollIndex = 0;
    function proinvScroll(next,dom){
        if($(dom).hasClass('disable')){
            return;
        }
        var width = parseInt($('.proinv-scroll').css('width'));
        if(next){
            proinvScrollIndex++;
        }else{
            proinvScrollIndex--;
        }
        ml = -proinvScrollIndex*368;
        if(proinvScrollIndex>=0&&proinvScrollIndex<=width/368-2){
            $('.proinv-scroll').css('margin-left',ml+'px');
        }
        if(proinvScrollIndex==0){
           $('.proinv-scroll-btn.prev').addClass('disable'); 
        }else{
            $('.proinv-scroll-btn.prev').removeClass('disable');
        }
        if(proinvScrollIndex==parseInt(width/368)-2){
           $('.proinv-scroll-btn.next').addClass('disable'); 
        }else{
            $('.proinv-scroll-btn.next').removeClass('disable');
        }
    }
    var isWebkit = false;
    if (navigator.userAgent.indexOf('Chrome') > -1 || 
     navigator.userAgent.indexOf('Safari') > -1) {
        isWebkit = true;
     }
    var proinvDesc = $('.proinv-desc');
    for(var i=0;i<proinvDesc.length;i++){
        if(proinvDesc[i].scrollHeight>40 && !isWebkit){
            proinvDesc.eq(i).append('<div class="more">…</div>');
        }
        
    }
</script> <div class="col-md-12 search-sidebar hidden-xs no-padding-right" id="smartBox"> <div class="v3_sl_tab"> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="active">公司</a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="">风险信息</a> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="">知识产权</a> </div> <section class="panel b-a n-s" id="search-options"> <div id="SearchBox"> <dl class="sfilter-tag clearfix indexChoose" id="indexOld"> <div class="pull-left" style="width:76px;"><dt>查找范围</dt></div> <div class="pull-left" style="width:80%;"> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        企业名
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        法人或股东
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        高管
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        品牌/产品
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        联系方式
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        经营范围
                                    </a> </dd> </div> </dl> <dl class="sfilter-tag clearfix searchTypeChoose" id="indexOld"> <div class="pull-left" style="width:76px;"><dt>机构类型</dt></div> <div class="pull-left" style="width:80%;"> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        企业
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        社会组织
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        香港公司
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        台湾公司
                                    </a> </dd> </div> </dl> <dl class="sfilter-tag clearfix coyTypeChoose" id="coytypeOld"> <div class="pull-left" style="width:76px;"><dt>企业类型</dt></div> <div class="pull-left" style="width:80%;"> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        有限责任公司
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        股份有限公司
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        国企
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        外商投资企业
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        独资企业
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        合伙制企业
                                    </a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        个体工商户
                                    </a> </dd> </div> </dl> <dl class="sfilter-tag clearfix" id="statuscodeOld"> <div class="pull-left" style="width:76px;"><dt>企业状态</dt></div> <div class="pull-left" style="width:85%;"> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">在业</a></dd> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">存续</a></dd> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">筹建</a></dd> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">清算</a></dd> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">迁入</a></dd> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">迁出</a></dd> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">停业</a></dd> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">撤销</a></dd> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">吊销</a></dd> <dd><a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">注销</a></dd> </div> </dl> <dl class="sfilter-tag clearfix" id="registcapiOld"> <div class="pull-left" style="width:76px;"><dt>注册资本</dt></div> <div class="pull-left" style="width:80%;"> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">500万以下</a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">500~1000万</a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">1000~5000万</a> </dd> <dd> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">5000万以上</a> </dd> <dd> <a class="custom" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"> <span class="i-s"><span class="x">自定义</span> <span class="caret"></span></span> </a> </dd> </div> </dl> <dl class="sfilter-tag clearfix" id="startdateOld"> <div class="pull-left" style="width:76px;"><dt>成立日期</dt></div> <div class="pull-left" style="width:80%;"> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2018&nbsp;(493)
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2017&nbsp;(736)
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2016&nbsp;(720)
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2015&nbsp;(636)
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2014&nbsp;(562)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2013&nbsp;(478)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2012&nbsp;(409)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2011&nbsp;(432)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2010&nbsp;(395)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2009&nbsp;(339)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2008&nbsp;(361)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2007&nbsp;(307)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2006&nbsp;(279)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2005&nbsp;(256)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2004&nbsp;(273)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2003&nbsp;(264)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2002&nbsp;(256)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2001&nbsp;(246)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        2000&nbsp;(255)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1999&nbsp;(157)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1998&nbsp;(154)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1997&nbsp;(140)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1996&nbsp;(84)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1995&nbsp;(97)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1994&nbsp;(92)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1993&nbsp;(108)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1992&nbsp;(57)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1991&nbsp;(46)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1990&nbsp;(42)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1989&nbsp;(33)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1988&nbsp;(19)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1987&nbsp;(19)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1986&nbsp;(12)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1985&nbsp;(18)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1984&nbsp;(9)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1983&nbsp;(6)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1982&nbsp;(8)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1981&nbsp;(18)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1980&nbsp;(17)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1979&nbsp;(4)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1978&nbsp;(1)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1975&nbsp;(1)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1974&nbsp;(1)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1971&nbsp;(1)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1965&nbsp;(1)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1964&nbsp;(2)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1963&nbsp;(2)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1959&nbsp;(1)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1956&nbsp;(2)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1953&nbsp;(1)
                                    </a> </dd> <dd class="startdate-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        1949&nbsp;(1)
                                    </a> </dd> <dd> <a class="custom" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"> <span class="i-s"><span class="x">自定义</span> <span class="caret"></span></span> </a> </dd> </div> <a class="btn btn-link btn-sm pull-right v3_a_more" id="show-date" style="margin-top:-3px;"><span>更多</span> <i class="i i-arrow-down4"></i></a> </dl> <dl class="sfilter-tag clearfix" id="provinceOld"> <div class="pull-left" style="width:76px;"><dt>省份地区</dt></div> <div class="pull-left" style="width:80%;"> <dd class="province-dd" style="display:none;" > </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        安徽 ( 221 )
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        北京 ( 476 )
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        重庆 ( 168 )
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        福建 ( 403 )
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        广东 ( 1687 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        甘肃 ( 36 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        广西 ( 218 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        贵州 ( 90 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        海南 ( 58 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        河北 ( 135 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        河南 ( 245 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        香港特别行政区 ( 17 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        黑龙江 ( 129 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        湖北 ( 281 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        湖南 ( 489 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        吉林 ( 91 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        江苏 ( 682 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        江西 ( 168 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        辽宁 ( 217 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        内蒙古 ( 83 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        宁夏 ( 38 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        青海 ( 30 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        陕西 ( 180 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        四川 ( 356 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        山东 ( 340 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        上海 ( 538 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        山西 ( 83 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        天津 ( 131 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        台湾省 ( 129 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        新疆 ( 236 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        西藏 ( 21 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        云南 ( 332 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        浙江 ( 573 )
                                    </a> </dd> <dd class="province-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="showCity">
                                        总局 ( 3 )
                                    </a> </dd> </div> <a class="btn btn-link btn-sm pull-right v3_a_more" id="show-province" style="margin-top:-3px;"><span>更多</span> <i class="i i-arrow-down4"></i></a> </dl> <dl class="sfilter-tag clearfix" id="industrycodeOld"> <div class="pull-left" style="width:76px;"><dt>行业门类</dt></div> <div class="pull-left" style="width:80%;"> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        农、林、牧、渔业&nbsp;(89)
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        采矿业&nbsp;(29)
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        制造业&nbsp;(2164)
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        电力、热力、燃气及水生产和供应业&nbsp;(107)
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        建筑业&nbsp;(157)
                                    </a> </dd> <dd > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        批发和零售业&nbsp;(2056)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        交通运输、仓储和邮政业&nbsp;(35)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        住宿和餐饮业&nbsp;(263)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        信息传输、软件和信息技术服务业&nbsp;(332)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        金融业&nbsp;(34)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        房地产业&nbsp;(23)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        租赁和商务服务业&nbsp;(407)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        科学研究和技术服务业&nbsp;(1238)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        水利、环境和公共设施管理业&nbsp;(17)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        居民服务、修理和其他服务业&nbsp;(170)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        教育&nbsp;(9)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        卫生和社会工作&nbsp;(1)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        文化、体育和娱乐业&nbsp;(64)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        公共管理、社会保障和社会组织&nbsp;(1)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        国际组织&nbsp;(2)
                                    </a> </dd> <dd class="industrycode-dd" style="display:none;" > <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                        其他行业&nbsp;(1702)
                                    </a> </dd> </div> <a class="btn btn-link btn-sm pull-right v3_a_more" id="show-industrycode" style="margin-top:-3px;"><span>更多</span> <i class="i i-arrow-down4"></i></a> </dl> <dl class="sfilter-tag clearfix" id="telOld"> <div class="pull-left" style="width:76px;"><dt>高级筛选</dt></div> <div class="pull-left" style="width:80%;"> <dd class="telChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">联系电话</span> <span class="caret"></span></span> </span> </dd> <dd class="phoneChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">手机号码</span> <span class="caret"></span></span> </span> </dd> <dd class="emailChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">联系邮箱</span> <span class="caret"></span></span> </span> </dd> <dd class="gwebsiteChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">官网信息</span> <span class="caret"></span></span> </span> </dd> <dd class="markChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">商标信息</span> <span class="caret"></span></span> </span> </dd> <dd class="patentChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">专利信息</span> <span class="caret"></span></span> </span> </dd> <dd class="financeChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">融资信息</span> <span class="caret"></span></span> </span> </dd> <dd class="listedChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">上市状态</span> <span class="caret"></span></span> </span> </dd> <dd class="shixinChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">失信信息</span> <span class="caret"></span></span> </span> </dd> <dd class="zzqChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">著作权</span> <span class="caret"></span></span> </span> </dd> <dd class="rjzzqChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">软件著作权</span> <span class="caret"></span></span> </span> </dd> <dd class="insuredChoose"> <span class="custom a" data-option="x"> <span class="dropdown-toggle i-s" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><span class="x">参保人数</span> <span class="caret"></span></span> </span> </dd> </div> </dl> </div> </section> <div class="hideSearchBoxWrap"> <a class="" id="hideSearchBox"><span>收起</span> <i class="i i-arrow-up4"></i></a> </div> </div> <div class="col-md-12 no-padding-right" id="ajaxlist"> <div class="panel panel-default n-s" style="padding:15px 0 45px;margin-bottom: -1px;"> <span class="font-15 text-dark pull-left m-l" id="countOld">
						    				
                            小查为您找到
                                <span class="text-danger">
                                     5000+                                 </span>
                            家符合条件的企业 
									
                       </span> </div> <section class="panel b-a n-s" style="margin-bottom: 0px;" id="searchlist"> <table class="m_srchList"> <thead> <tr id="search-tab-title"> <th width="70px">公司</th> <th></th> <th width="100px">状态</th> </tr> </thead> <tbody> <tr> <td> <img src="https://co-image.qichacha.com/CompanyImage/182249d7736fdb68960201022c19647a.jpg?x-oss-process=style/qcc_cmp" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'" alt="比一比的搜索结果" > </td> <td> <a onclick="addSearchIndex('比一比',1);" href="https://www.qichacha.com/firm_182249d7736fdb68960201022c19647a.html" target="_blank" class="ma_h1">深圳市<em><em>比一比</em></em>网络科技有限公司</a><br/> <p class="m-t-xs">
                                                                                                                                                            法定代表人：
                                                                                                                                                                                                            <a onclick="" class="text-primary" href="https://www.qichacha.com/people?name=%E6%9D%9C%E5%8D%AB%E7%BA%A2&keyno=182249d7736fdb68960201022c19647a">杜卫红</a> <span class="m-l">注册资本：1107.7417万元人民币</span> <span class="m-l">成立时间：2009-01-12</span> </p> <p class="m-t-xs">
                                     邮箱：
                                        <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                             
                                                ***@qq.com
                                                                                    </a> <span class="m-l">
                                         电话：
                                         <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                              0755-8832****
                                                                                      </a> </span> </p> <p class="m-t-xs">
                                     地址：深圳市南山区粤海街道高新技术园中区科苑大道讯美科技广场1栋3楼306
                                    </p> <p> <i class="i   i-search"></i>
                                                                        品牌/产品：深圳<em>比一比</em> </td> <td> <span class="nstatus text-success-lt m-l-xs">存续</span> </td> </tr> <tr> <td> <img src="https://qccdata.qichacha.com/AutoImage/fab0038b9ebca3b67838addd4e84e39f.jpg?x-oss-process=image/resize,w_120" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'" alt="比一比的搜索结果" > </td> <td> <a onclick="addSearchIndex('比一比',2);" href="https://www.qichacha.com/firm_fab0038b9ebca3b67838addd4e84e39f.html" target="_blank" class="ma_h1">江苏<em><em>比一比</em></em>智能科技有限公司</a><br/> <p class="m-t-xs">
                                                                                                                                                            法定代表人：
                                                                                                                                                                                                            <a onclick="" class="text-primary" href="https://www.qichacha.com/people?name=%E6%9D%8E%E6%B5%B7%E6%B4%8B&keyno=fab0038b9ebca3b67838addd4e84e39f">李海洋</a> <span class="m-l">注册资本：1000万元人民币</span> <span class="m-l">成立时间：2018-01-12</span> </p> <p class="m-t-xs">
                                     邮箱：
                                        <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                            -
                                                                                    </a> <span class="m-l">
                                         电话：
                                         <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                              -
                                                                                      </a> </span> </p> <p class="m-t-xs">
                                     地址：苏州市相城区渭塘镇爱格豪路19号中国汽车零部件产业基地研发楼7楼北侧
                                    </p> </p> </td> <td> <span class="nstatus text-success-lt m-l-xs">在业</span> </td> </tr> <tr> <td> <img src="https://qccdata.qichacha.com/AutoImage/974c7dd4cdbf47462eaee1cf5f9b3ad9.jpg?x-oss-process=image/resize,w_120" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'" alt="比一比的搜索结果" > </td> <td> <a onclick="addSearchIndex('比一比',3);" href="https://www.qichacha.com/firm_974c7dd4cdbf47462eaee1cf5f9b3ad9.html" target="_blank" class="ma_h1">杭州<em><em>比一比</em></em>电子科技有限公司</a><br/> <p class="m-t-xs">
                                                                                                                                                            法定代表人：
                                                                                                                                                                                                            <a onclick="" class="text-primary" href="https://www.qichacha.com/people?name=%E6%B1%A4%E7%BB%A7%E5%88%9A&keyno=974c7dd4cdbf47462eaee1cf5f9b3ad9">汤继刚</a> <span class="m-l">注册资本：5000万元人民币</span> <span class="m-l">成立时间：2018-04-25</span> </p> <p class="m-t-xs">
                                     邮箱：
                                        <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                            -
                                                                                    </a> <span class="m-l">
                                         电话：
                                         <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                              -
                                                                                      </a> </span> </p> <p class="m-t-xs">
                                     地址：浙江省杭州市余杭区良渚街道逸盛路169号210室
                                    </p> </p> </td> <td> <span class="nstatus text-success-lt m-l-xs">存续</span> </td> </tr> <tr> <td> <img src="https://qccdata.qichacha.com/AutoImage/21c3134b94b617e834288cb99d52b608.jpg?x-oss-process=image/resize,w_120" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'" alt="比一比的搜索结果" > </td> <td> <a onclick="addSearchIndex('比一比',4);" href="https://www.qichacha.com/firm_21c3134b94b617e834288cb99d52b608.html" target="_blank" class="ma_h1">山东农大肥业科技有限公司</a><br/> <p class="m-t-xs">
                                                                                                                                                            法定代表人：
                                                                                                                                                                                                            <a onclick="" class="text-primary" href="https://www.qichacha.com/people?name=%E9%A9%AC%E5%AD%A6%E6%96%87&keyno=21c3134b94b617e834288cb99d52b608">马学文</a> <span class="m-l">注册资本：3000万元人民币</span> <span class="m-l">成立时间：2002-06-17</span> </p> <p class="m-t-xs">
                                     邮箱：
                                        <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                             
                                                ***@163.com
                                                                                    </a> <span class="m-l">
                                         电话：
                                         <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                              0538-506****
                                                                                      </a> </span> <a class="text-primary" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">更多号码</a> </p> <p class="m-t-xs">
                                     地址：山东省泰安市肥城市高新技术开发区
                                    </p> <p> <i class="i   i-search"></i>
                                                                        商标：<em>比一比</em> BYB
                                                                                                        </td> <td> <span class="nstatus text-success-lt m-l-xs">在业</span> </td> </tr> <tr> <td> <img src="https://qccdata.qichacha.com/AutoImage/dbfdc9a90b98210c96fb3fdac613e534.jpg?x-oss-process=image/resize,w_120" onerror="this.src='https://co-image.qichacha.com/CompanyImage/default.jpg'" alt="比一比的搜索结果" > </td> <td> <a onclick="addSearchIndex('比一比',5);" href="https://www.qichacha.com/firm_dbfdc9a90b98210c96fb3fdac613e534.html" target="_blank" class="ma_h1">深圳<em><em>比一比</em></em>保险科技有限责任公司</a><br/> <p class="m-t-xs">
                                                                                                                                                            法定代表人：
                                                                                                                                                                                                            <a onclick="" class="text-primary" href="https://www.qichacha.com/people?name=%E9%AB%98%E6%AD%A6%E6%98%8E&keyno=dbfdc9a90b98210c96fb3fdac613e534">高武明</a> <span class="m-l">注册资本：500万元人民币</span> <span class="m-l">成立时间：2017-05-05</span> </p> <p class="m-t-xs">
                                     邮箱：
                                        <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                             
                                                ***@qq.com
                                                                                    </a> <span class="m-l">
                                         电话：
                                         <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">
                                                                                              1856561****
                                                                                      </a> </span> </p> <p class="m-t-xs">
                                     地址：深圳市福田区华强北街道赛格科技园四栋西9楼A座A09
                                    </p> </p> </td> <td> <span class="nstatus text-success-lt m-l-xs">存续</span> </td> </tr> </tbody> </table> </section> <div style="text-align:center;"></div> <div class="company-mengban"> <div class="company-vip-kuang"> <div class="company-vip-title m-t"> <p>亲，小查告诉你个秘密:-D</p> <p>登录后可以查看更多数据，免费获取信用报告哦！</p> </div> <a data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()" class="company-vip-btn btn btn-danger m-t">立即登录</a> <a href="https://www.qichacha.com/user_register?back=/search?key=比一比" class="company-vip-btn btn btn-primary m-t m-l">免费注册</a> </div> </div> </div> </div> <div class="col-md-3"> <div class="m-b"> <a onclick="zhugeTrack('广告-企查查小程序');" href="https://www.qichacha.com/weixin_xcx" target="_blank"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/rightxcx.png" style="width:280px;" alt="企查查"/> </a> </div> <div class="m-b"> <a onclick="zhugeTrack('广告-企查查APP');" href="https://www.qichacha.com/app" target="_blank"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/rightapp2.png" style="width:280px;" alt="企查查"/> </a> </div> <div class="m-b"> <a onclick="zhugeTrack('广告-批量导出开通VIP');" href="https://www.qichacha.com/vip" target="_blank"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/righthy2.png" style="width:280px;"/> </a> </div> <div class="m-b"> <a onclick="zhugeTrack('广告-一键查询最终受益人');" href="https://www.qichacha.com/firm_eac35f7cb2922037a2f7e0525d8cf0cb.html#syrlistpos" target="_blank"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/rightsyr.png" style="width:280px;"/> </a> </div> <div class="m-b"> <a onclick="zhugeTrack('广告-批量查询');" href="https://www.qichacha.com/more_batchsearch" target="_blank"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/rightsearch.png" style="width:280px;"/> </a> </div> <section class="panel b-a n-s" style="width:280px;margin-top:20px;"> <div class="panel-heading b-b"> <span class="font-bold font-15 text-dark" style="color:#5c5c5c;">最近浏览</span> </div> <ul class="list-group no-bg auto v3_lastview"> <a href="https://www.qichacha.com/firm_bdd5a090c2131456bd892f03a6681e99" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">全椒济源粮食饲料经营部</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 53分钟前</span> </a> <a href="https://www.qichacha.com/firm_bc76481573e02d932cc35b1fc5e00322" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">德州开创网络有限公司</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 53分钟前</span> </a> <a href="https://www.qichacha.com/firm_b72f064296a7e9daa7c8984950b16b07" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">湖南省铜官陶瓷总公司威远炻瓷厂分厂</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 53分钟前</span> </a> <a href="https://www.qichacha.com/firm_743bae7f8d19f80a9efc083da8be6665" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">平江县佳杰童装店</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 53分钟前</span> </a> <a href="https://www.qichacha.com/firm_d178c64c715b194c9af968a14692eeef" target="_blank" class="list-group-item clearfix"> <span class="font-15 clear">北京数字天域科技有限责任公司</span> <span class="text-muted text-xs clear"><i class="i i-clock"></i> 53分钟前</span> </a> </ul> </section> </div> </div> </div> <script>
    $(function () {

        //展开，收起搜索框
        $('#hideSearchBox').on('click',function(){
            $('#SearchBox').toggle();
            toggleClass($(this));
        });

        //展开，收起成立日期
        $('#show-date').on('click',function(){
            toggleClass($(this),'startdate');
        });

        //展开，收起省份地区
        $('#show-province').on('click',function(){
            toggleClass($(this),'province');
        });

        //展开，收起行业
        $('#show-industrycode').on('click',function(){
            toggleClass($(this),'industrycode');
        });

        function toggleClass(obj,option){
            var flag = arguments[1] ? true : false;
            if(flag)var optionObj = '.' + option + '-dd';
            var i    = obj.find('i');
            var span = obj.find('span');
            if(i.hasClass('i-arrow-up4')){
                if(flag)$(optionObj).hide();
                i.removeClass('i-arrow-up4');
                i.addClass('i-arrow-down4');
                if(flag){
                    span.text('更多');
                }else{
                    span.text('展开');
                }
            }else{
                if(flag)$(optionObj).show();
                i.removeClass('i-arrow-down4');
                i.addClass('i-arrow-up4');
                if(flag){
                    span.text('收起'); 
                }else{
                    span.text('收起');
                }
            }
        }
    });
</script> <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/footer.css?time=20181105" type="text/css"/> <link rel="stylesheet" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/animate.css?time=1508428800" type="text/css"/> <footer class="footer"> <div class="container"> <div class="footer-top clearfix"> <div class="about" style=""> <h4>关于我们</h4> <ul class="list-unstyled"> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'联系我们'});" href="https://www.qichacha.com/cms?id=13">联系我们</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'用户协议'});" href="https://www.qichacha.com/cms?id=14">用户协议</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'用户隐私权'});" href="https://www.qichacha.com/cms?id=15">用户隐私权</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'友情链接'});" href="https://www.qichacha.com/cms?id=16">友情链接</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'关于我们'});" href="https://www.qichacha.com/cms?id=892">关于我们</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'用户帮助'});" href="https://www.qichacha.com/cms?id=14578">用户帮助</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'名词百科'});" href="https://www.qichacha.com/cms?id=146498">名词百科</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'产品标签'});" href="https://www.qichacha.com/cms?id=146499">产品标签</a></li> <li><a onclick="zhugeTrack('主页-关于我们',{'子类名称':'更新记录'});" href="https://www.qichacha.com/cms?id=146500">更新记录</a></li> </ul> </div> <div class="contact"> <h4>联系方式</h4> <ul class="list-unstyled"> <li>企查查官方电话：400-928-2212</li> <li>官方客服QQ：<a target="_blank" href="http://wpa.b.qq.com/cgi/wpa.php?ln=1&key=XzkzODA0NDMwM180ODcyNjFfNDAwOTk4NTIxMl8yXw">4009985212</a></li> <li>客服邮箱：<a href="mailto:kf@qichacha.com">kf@qichacha.com</a></li> <li>微信客服：qccgf1234</li> <li>微信公众号：qcc365</li> <li>地址：江苏省苏州市工业园区东长路88号2.5产业园C1幢5楼</li> </ul> </div> <div class="service" style=""> <h4>查查服务</h4> <ul class="list-unstyled"> <li> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'股加加'});" href="https://www.shareplus.cn/?hmsr=%E4%BC%81%E6%9F%A5%E6%9F%A5&hmpl=&hmcu=&hmkw=&hmci=" target="_blank" >股加加</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'500强企业'});" href="https://www.qichacha.com/cms_top500" target="_blank" >500强企业</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'权查查'});" href="http://www.qccip.com/" target="_blank" >权查查</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'客找找'});" href="http://www.kezhaozhao.com/" target="_blank" >客找找</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'疫苗查查'});" href="http://ai.qichacha.com/" target="_blank" >疫苗查查</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'融资查询'});" href="https://www.qichacha.com/elib_financing" target="_blank" >融资查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企风控'});" href="http://www.qifengkong.com/a/login?source=websiteFoot" target="_blank" >企风控</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业库'});" href="http://www.qichacha.com/elib" target="_blank" >企业库</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'裁判文书查询'});" href="http://www.qichacha.com/more_wenshus" target="_blank" >裁判文书查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'新三板企业查询'});" href="http://sanban.qichacha.com" target="_blank" >新三板企业查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'上市企业查询'});" href="http://ipo.qichacha.com/" target="_blank" >上市企业查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查企业查询'});" href="https://www.qichacha.com/gongsi" target="_blank" >企查查企业查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查移动版'});" href="https://m.qichacha.com" target="_blank" >企查查移动版</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查社区'});" href="https://www.qichacha.com/dianping" target="_blank" >企查查社区</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业风险搜索'});" href="https://www.qichacha.com/more_shixins" target="_blank" >企业风险搜索</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'商标专利搜索'});" href="https://www.qichacha.com/more_brands" target="_blank" >商标专利搜索</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业网址导航'});" href="https://www.qichacha.com/daohang" target="_blank" >企业网址导航</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业高管查询'});" href="https://www.qichacha.com/boss" target="_blank" >企业高管查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业税号查询'});" href="https://www.qichacha.com/tax" target="_blank" >企业税号查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业新闻头条'});" href="https://www.qichacha.com/news" target="_blank" >企业新闻头条</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业大数据导航'});" href="https://hao.qichacha.com" target="_blank" >企业大数据导航</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查下载'});" href="https://www.qichacha.com/weixin" target="_blank" >企查查下载</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企业失信查询'});" href="https://www.qichacha.com/more_shixins" target="_blank" >企业失信查询</a> <a onclick="zhugeTrack('主页-查查服务',{'子类名称':'企查查接口平台'});" href="http://www.yjapi.com/?from=qichacha" target="_blank" rel="nofollow">企查查接口平台</a> <a href="https://www.qichacha.com/yellowpage">公司黄页</a> <a href="https://www.qichacha.com/cms_dirhot">人员名录</a> <a href="http://open.qichacha.com" target="_blank"> 开放平台</a> </li> </ul> </div> <div class="qrcode"> <div class="qrcode-item"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/v3/code_xcx.png?t=3" alt="企查查APP下载"> <span class="ma_xcx">小程序</span> </div> <div class="qrcode-item"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/v3/code_app.png?t=3" alt="企查查APP下载"> <span class="ma_app">扫码下载APP</span> </div> <div class="qrcode-item"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/v3/code_wx.png?t=3" alt="企查查微信公众号"> <span class="ma_wx">微信公众号</span> </div> </div> </div> <div class="footer-link"> <div class="footer-row clearfix"> <div class="footer-row-head">
                    数据来源：
                </div> <div class="footer-row-content"> <span class="item">全国企业信用信息公示系统</span> <span class="item">中国裁判文书网</span> <span class="item">中国执行信息公开网</span> <span class="item">国家知识产权局</span> <span class="item">商标局</span> <span class="item">版权局</span> </div> </div> <div class="footer-row clearfix"> <div class="footer-row-head">
                    热点省份：
                </div> <div class="footer-row-content"> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'安徽企业'});" href="http://ah.qichacha.com" target="_blank">安徽企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'北京企业'});" href="http://bj.qichacha.com" target="_blank">北京企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'重庆企业'});" href="http://cq.qichacha.com" target="_blank">重庆企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'福建企业'});" href="http://fj.qichacha.com" target="_blank">福建企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'甘肃企业'});" href="http://gs.qichacha.com" target="_blank">甘肃企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'广东企业'});" href="http://gd.qichacha.com" target="_blank">广东企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'广西企业'});" href="http://gx.qichacha.com" target="_blank">广西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'贵州企业'});" href="http://gz.qichacha.com" target="_blank">贵州企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'海南企业'});" href="http://hain.qichacha.com" target="_blank">海南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'河北企业'});" href="http://hb.qichacha.com" target="_blank">河北企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'黑龙江企业'});" href="http://hlj.qichacha.com" target="_blank">黑龙江企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'河南企业'});" href="http://hen.qichacha.com" target="_blank">河南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'湖北企业'});" href="http://hub.qichacha.com" target="_blank">湖北企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'湖南企业'});" href="http://hun.qichacha.com" target="_blank">湖南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'江苏企业'});" href="http://js.qichacha.com" target="_blank">江苏企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'江西企业'});" href="http://jx.qichacha.com" target="_blank">江西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'吉林企业'});" href="http://jl.qichacha.com" target="_blank">吉林企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'辽宁企业'});" href="http://ln.qichacha.com" target="_blank">辽宁企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'内蒙古企业'});" href="http://nmg.qichacha.com" target="_blank">内蒙古企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'宁夏企业'});" href="http://nx.qichacha.com" target="_blank">宁夏企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'青海企业'});" href="http://qh.qichacha.com" target="_blank">青海企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'山东企业'});" href="http://sd.qichacha.com" target="_blank">山东企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'上海企业'});" href="http://sh.qichacha.com" target="_blank">上海企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'山西企业'});" href="http://sx.qichacha.com" target="_blank">山西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'陕西企业'});" href="http://sax.qichacha.com" target="_blank">陕西企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'四川企业'});" href="http://sc.qichacha.com" target="_blank">四川企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'天津企业'});" href="http://tj.qichacha.com" target="_blank">天津企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'新疆企业'});" href="http://xj.qichacha.com" target="_blank">新疆企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'西藏企业'});" href="http://xz.qichacha.com" target="_blank">西藏企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'云南企业'});" href="http://yn.qichacha.com" target="_blank">云南企业</a> </div> <div class="item"> <a onclick="zhugeTrack('主页-热点省份',{'子类名称':'浙江企业'});" href="http://zj.qichacha.com" target="_blank">浙江企业</a> </div> </div> </div> </div> </div> <div class="footer-copy-bg"> <div class="container"> <div class="footer-copy clearfix"> <div class="pull-left"> <div class="m-t-sm">交流QQ群：
                        <span>928689619</span> <span>&nbsp;&nbsp;&nbsp;467569586(已满)</span> <span>&nbsp;369254293(已满)</span> <span>&nbsp;257048933(已满)</span> <span>&nbsp;259189047(已满)</span> <span>&nbsp;371601207(已满)</span> </div> <div class="m-t-xs"> <a href="javascript:void(0)" title="企查查">&copy;2014-2018</a> <a href="http://www.miibeian.gov.cn/" target="_blank"> 苏ICP备15042526号-4</a>
                        版权所有&nbsp;苏州朗动网络科技有限公司
                        &nbsp;增值电信业务经营许可证：<a href="http://jscainfo.miitbeian.gov.cn/state/outPortal/loginPortal.action" rel="nofollow" target="_blank">苏ICP证B2-20180251</a> </div> </div> <div class="auth"> <a href="https://ss.knet.cn/verifyseal.dll?sn=e17091132050068868mhtm000000&comefrom=trust" rel="nofollow" target="_blank"> <img class="m-l-sm" style="width: 128px" src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/dependable.png"/> </a> <a href="http://www.jsdsgsxt.gov.cn/mbm/entweb/elec/certView.shtml?siteId=2f2c5b85a5154355a56eb3dee98ad8a3" rel="nofollow" target="_blank"> <img class="m-l-sm" style="width: 50px" src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/jsdsgsxt.png"/> </a> <a href="https://v.pinpaibao.com.cn/cert/site/?site=www.qichacha.com&at=official" rel="nofollow" target="_blank"> <img class="m-l-sm" style="width: 124px;" src="https://static.anquan.org/static/outer/image/gw_124x47.png"/> </a> </div> </div> </div> </div> </footer> <div class="modal fade" id="feedModal" tabindex="-1" role="dialog" style="overflow: hidden;" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal nmodal-sm"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="myModalLabel">意见反馈</h4> </div> <div class="modal-body"> <form class="form-horizontal" role="form"> <div class="form-group"> <label for="inputEmail3" class="col-sm-2">反馈内容</label> <div class="col-sm-10"> <textarea class="form-control content" rows="5"  name="content" placeholder="亲爱的用户：请在这里直接填写您遇到的问题或意见建议，您的意见是我们前进的动力"></textarea> <span class="contentmsg text-danger"></span> </div> </div> <div class="form-group"> <label for="inputPassword3" class="col-sm-2">联系方式</label> <div class="col-sm-10"> <input type="text" class="form-control email" name="email" placeholder="请输入邮箱，方便我们联系您。"> <span class="emailmsg text-danger"></span> </div> </div> <div class="form-group"> <div class="col-sm-10 col-sm-offset-2"> <label>亲爱的顾客，您也可以直接拨打企查查官方电话：400-928-2212 或者 联系企查查官方客服QQ：4009985212，我们将及时为您解答问题。</label> </div> </div> <div class="form-group m-t-lg"> <label for="inputPassword3" class="col-sm-2"></label> <div class="col-sm-10  text-center"> <span class="btn btn-primary btn-guest btn-block">提交反馈</span> </div> </div> </form> </div> </div> </div> </div> <div style="display:none;"> <script src="https://s4.cnzz.com/z_stat.php?id=1254842228&web_id=1254842228" language="JavaScript"></script> <script>
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
  </script> </div> <script type="text/javascript">
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
</script> <link rel="stylesheet" type="text/css" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/rnav.css?timestamp=20181105"> <div id="RNav" class="visible-lg i_hide"> <div class="i_menu"> <ul class="i_bts-outer" style="bottom:69px;"> <li class="i_bt_sm i_bt_xcx"><i></i> <label>小程序</label><img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/leftnav/bg_xcx.png?t=2" alt="企查查"></li> <li class="i_bt_sm i_bt_wx"><i></i> <label>公众号</label><img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/leftnav/bg_wx.png?t=2" alt="企查查"></li> <li onclick="zhugeTrack('下载APP悬浮按钮');" class="i_bt_sm i_bt_dow"><i></i> <label>下载</label><img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/leftnav/bg_app.png?t=3" alt="企查查"></li> <script type="text/javascript" src="https://www.qichacha.com/material/js/jquery.cookie.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/js/jquery.validate.min.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/js/jquery.form.min.js"></script> <script type="text/javascript" src="https://www.qichacha.com/material/js/global.js?t=33"></script> <li id="RNBack" class="i_bt_sm i_bt_back" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><i></i> <label>反馈</label></li> <li class="i_bt_sm i_bt_kf" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"><i></i> <label>客服</label></li> <li id="RNTop" class="i_bt_sm i_bt_top"><i></i> <label>置顶</label></li> </ul> </div> <div class="i_container"> <div class="i_nodata">暂无数据</div> <div id="RNFoc" class="i_wrap"> <div class="i_title">我的关注</div> <div class="i_com-wrap"> <div style="height:1px;width:240px;"></div> </div> <div class="i_botbt"> <a href="https://www.qichacha.com/user_follow">打开全部</a> </div> </div> <div id="RNCom" class="i_wrap"> <div class="i_title">企业对比</div> <div class="i_toast">
				还可以添加<span id="ComLastCount">5</span>家企业 
				<a id="ClearCompares" class="c_a">清空</a> </div> <div class="i_com-wrap"> <div class="i_com i_addcom" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/leftnav/icon-add.png" alt="企查查"/> <a class="c_a" href="javascript:;">添加企业</a> </div> <div style="height:1px;width:240px;"></div> </div> <div class="i_botbt"> <a href="javascript:;" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">对比企业</a> </div> </div> <div id="RNRel" class="i_wrap"> <div class="i_title">找关系</div> <div class="i_toast">
				还可以添加<span id="RelLastCount">5</span>家企业 
				<a class="c_a" id="ClearRels">清空</a> </div> <div class="i_com-wrap"> <div class="i_com i_addcom" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()"> <img src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/leftnav/icon-add.png" alt="企查查"/> <a class="c_a" href="javascript:;">添加企业或个人</a> </div> <div style="height:1px;width:240px;"></div> </div> <div class="i_botbt"> <a href="javascript:;" data-toggle="modal" data-target="#loginModal" onclick="getCaptcha()">找关系</a> </div> </div> </div> <div class="modal fade" id="qaddComPanel" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content" style="width:600px;"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">添加企业</h4> </div> <div class="modal-body" style="height: 330px"> <form class="form-horizontal" role="form"> <div class="form-group"> <div class="col-sm-12 m-t-md"> <input type="text" id="qcomName" name="comName" class="form-control" value="" placeholder="请输入公司/人" autocomplete="off" oninput="qsearchCom(event,this)"/> <section class="panel hidden-xs" id="qsearchList" style="position: absolute;width: 560px;z-index: 10;display: none;"></section> </div> <div class="col-sm-12 text-center m-t-lg" style="padding-left: 18px;padding-right: 18px;"> <span id="qaddComPanelConfirm" class="btn-primary btn-guest btn-block" style="padding-top: 5px;padding-bottom: 5px;cursor:pointer;">添加企业</span> </div> </div> </form> </div> </div> </div> </div> <div class="modal fade" id="addRelPanel" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content" style="width:600px;"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title">添加企业或个人</h4> </div> <div class="modal-body" style="height: 445px"> <form class="form-horizontal" role="form"> <div class="form-group"> <div class="col-sm-12 m-t-md"> <input type="text" id="qrcomName" name="comName" class="form-control" value="" placeholder="请输入公司名称" autocomplete="off" oninput="qrsearchCom(event,this)"/> <section class="panel hidden-xs" id="qrsearchList" style="position: absolute;width: 560px;z-index: 10;display: none;"></section> </div> </div> </form> </div> </div> </div> </div> </div> <script type="text/javascript">
	 /*rightNav.js 使用变量*/
	 var personImg =  "/material/theme/chacha/cms/v2/images/leftnav/person.png";
	 var frimUrl = "";
	 var comDefaultImg = "/material/theme/chacha/cms/v2/images/company.jpg"
          
    function jumpTax(){
        window.location.href=encodeURI(INDEX_URL+"tax");
    }       
</script> <script src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/rightNav.js?timestamp=1497542400"></script> <link type="text/css" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/login.css?version=20181105" rel="stylesheet" /> <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" data-backdrop="static"> <div class="modal-dialog login-madal-dialog"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <h4 class="modal-title" id="myModalLabel">登录企查查</h4> </div> <div class="modal-body"> <div class="login-sao-panel"> <div class="title">扫码登录请使用<br> <a href="https://www.qichacha.com/app" target="_blank" class="text-primary">企查查APP</a> > 我的 > 扫一扫</div> <div class="qrcodewrap"> <div class="qrcode" id='qrcodeModalLogin'></div> <img class="qrcodets" src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/qrcode_ts.png"> </div> <div class="tip"><span></span> 扫一扫功能支持企查查 APP11.0.6 及以上版本</div> </div> <div class="login-panel" style="display: none;" id="normalLoginPanel"> <div class="login-panel-head clearfix"> <div class="login-tab"> <a href="javascript:;" id="verifyLogin">快捷登录</a> </div> <div class="login-tab"> <a href="javascript:;" class="active">密码登录</a> </div> </div> <div class="login-panel-body"> <form class="form-group login-form" role="form" id="user_login_normal"> <div class="form-group"> <input type='hidden' class='phone_prefix_input' value="+86" name='phone_prefix' /> <div class="phone-select dropdown"> <a class="phone_prefix" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"> 中国 +86<b class="caret text-primary"></b></a> <div class="phoneline"></div> <ul class="phone_prefix_ul dropdown-menu"></ul> </div> <input id="nameNormal" name="nameNormal" type="text" class="form-control form-control-error" placeholder="请输入手机号码"> <span msgfor="nameNormal"></span> </div> <div class="form-group m-t-md"> <div class="show-pwd"></div> <input id="pwdNormal" name="pwdNormal" type="password" class="form-control form-control-error" placeholder="请输入密码"> <span msgfor="pwdNormal"></span> </div> <div class="form-group m-t-md"> <div id="dom_id_one"></div> </div> <div class="checkbox m-t-md"> <label class="text-dark-lter"> <input type="checkbox" name="keep" checked="checked" value="option1"> 一周内保持登录状态
                                </label> </div> <button type="submit" class="btn btn-primary btn-block m-t-md login-btn"> <strong>立即登录</strong></button> <input type='hidden' id='csessionid_one' name='csessionid_one' /> <input type='hidden' id='sig_one' name='sig_one' /> <input type='hidden' id='token_one' name='token_one' /> <input type='hidden' id='scene_one' name='scene_one' /> <input type='hidden' name='verify_type' value="1" /> </form> <div class="login-other m-t-md"> <div class="clearfix"> <div class="pull-left"> <a href="https://www.qichacha.com/user_register" class="text-primary">账号注册</a> </div> <div class="pull-left text-dark-lt m-l-sm"> <a href="https://www.qichacha.com/user_forgetpassword">忘记密码？</a> </div> <div class="pull-right"> <a href="https://open.weixin.qq.com/connect/qrconnect?appid=wx9b26295cdfab4175&redirect_uri=http://www.qichacha.com/user_wxloginok?back=&response_type=code&scope=snsapi_login&state=#wechat_redirect" class="btn-wx"></a> <a href="https://www.qichacha.com/user_qqlogin?back=&replace=1" class="btn-qq m-l-xs"> </a> <a href="https://www.qichacha.com/user_weiboLogin" class="btn-weibo m-l-xs"> </a> </div> </div> </div> </div> </div> <div class="login-panel" id="verifyLoginPanel"> <div class="login-panel-head clearfix"> <div class="login-tab"> <a href="javascript:;" class="active">快捷登录</a> </div> <div class="login-tab"> <a href="javascript:;" id="normalLogin">密码登录</a> </div> </div> <div class="login-panel-body"> <form class="form-group login-form" role="form" id="user_login_verify"> <div class="form-group"> <input type='hidden' class='phone_prefix_input' value="+86" name='phone_prefix' /> <div class="phone-select dropdown"> <a class="phone_prefix" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"> 中国 +86<b class="caret text-primary"></b></a> <div class="phoneline"></div> <ul class="phone_prefix_ul dropdown-menu"></ul> </div> <input id="nameVerify" name="nameVerify" onkeyup="phoneKeyup()" oninput="phoneKeyup()" type="text" class="form-control form-control-error" placeholder="请输入手机号码"> <span msgfor="nameVerify"></span> </div> <div class="form-group m-t-md"> <div id="dom_id_two"></div> </div> <div class="form-group m-t-md"> <input id="vcodeNormal" maxlength="6" name="codeVerify" type="text" class="form-control form-control-error" placeholder="短信验证码"> <a href="javascript:;" class="text-primary vcode-btn get-mobile-code">
                         获取验证
                      </a> <span msgfor="codeVerify"> </span> </div> <div class="checkbox m-t-md"> <label class="text-dark-lter"> <input type="checkbox" name="keep" checked="checked" value="option1"> 一周内保持登录状态
                                </label> </div> <button type="submit" class="btn btn-primary btn-block m-t-md login-btn"> <strong>立即登录</strong></button> <input type='hidden' id='csessionid_two' name='csessionid_two' /> <input type='hidden' id='sig_two' name='sig_two' /> <input type='hidden' id='token_two' name='token_two' /> <input type='hidden' id='scene_two' name='scene_two' /> </form> <div class="login-other m-t-md"> <div class="clearfix"> <div class="pull-left"> <a onclick="" href="https://www.qichacha.com/user_register" class="text-primary">账号注册</a> </div> <div class="pull-left text-dark-lt m-l-sm"> <a onclick="" href="https://www.qichacha.com/user_forgetpassword">忘记密码？</a> </div> <div class="pull-right"> <a onclick="" href="https://open.weixin.qq.com/connect/qrconnect?appid=wx9b26295cdfab4175&redirect_uri=http://www.qichacha.com/user_wxloginok?back=&response_type=code&scope=snsapi_login&state=#wechat_redirect" class="btn-wx"></a> <a onclick="" href="https://www.qichacha.com/user_qqlogin?back=&replace=1" class="btn-qq m-l-xs"> </a> <a onclick="" routerLink="/user" class="btn-weibo m-l-xs"> </a> </div> </div> </div> </div> </div> </div> </div> </div> </div> <link type="text/css" href="https://www.qichacha.com//g.alicdn.com/sd/ncpc/nc.css?t=1520579483" rel="stylesheet" /> <script type="text/javascript" src="https://www.qichacha.com//g.alicdn.com/sd/ncpc/nc.js?t=1520579483"></script> <div id="_umfp" style="display:inline;width:1px;height:1px;overflow:hidden"></div> <script type="text/javascript" src="https://www.qichacha.com/material/theme/chacha/cms/v2/js/login.js?version=20181105"></script> <script>

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
</style> <link type="text/css" href="https://www.qichacha.com/material/theme/chacha/cms/v2/css/vip.css?version=20181105" rel="stylesheet"/> <div class="modal fade" id="vipModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> <div class="modal-dialog nmodal"> <div class="modal-content"> <div class="vip-top"> <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> <div class="vip-buy-panel"> <div class="vip-year-list clearfix"> <div data-id="17" class="vip-kuang vip-year active"> <div class="price"> <span>720元</span> <span style="color: #F9552A">/</span>
                                3年
                            </div> <div class="origin-price">原价：2160元</div> <div class="vip-rec"></div> </div> <div data-id="7" class="vip-kuang vip-year"> <div class="price"> <span>540元</span> <span style="color: #F9552A">/</span>
                                2年
                            </div> <div class="origin-price">原价：1440元</div> </div> <div data-id="6" class="vip-kuang vip-year"> <div class="price"> <span>360元</span> <span style="color: #F9552A">/</span>
                                1年
                            </div> <div class="origin-price">原价：720元</div> </div> </div> <a onclick="modalJumpVip()" class="vip-btn">立即开通</a> <div class="vip-publicity">支付后可开发票</div> </div> </div> <div class="vip-container"> <div class="table-caption"> <img style="width: 51px;" src="https://www.qichacha.com/material/theme/chacha/cms/v2/images/vip_tq@2x.png"><span>查企业、查老板、找关系</span> <a href="https://www.qichacha.com/vip" class="pull-right">查看全部></a> </div> <table class="vip-table table table-striped"> <tr> <td width="32%">功能介绍</td> <td class="vip-text-re" width="34%">VIP会员</td> <td width="34%">普通会员</td> </tr> <tr> <td class="vip-text-bl">查询结果显示条数</td> <td class="vip-text-re">5000条</td> <td>100(<a href="http://www.qichacha.com" target="_blank">Web端</a>)/40(<a href="http://www.qichacha.com/app" target="_blank">App端</a>)</td> </tr> <tr> <td class="vip-text-bl">查询结果数据下载</td> <td class="vip-text-re">10次/天（每次最多5000条）</td> <td><span class="x">×</span></td> </tr> <tr> <td class="vip-text-bl">老板查询</td> <td class="vip-text-re">不限次</td> <td><span class="x">×</span></td> </tr> <tr> <td class="vip-text-bl">历史信息</td> <td class="vip-text-re">不限次</td> <td><span class="x">×</span></td> </tr> <tr> <td class="vip-text-bl">雷达监控</td> <td class="vip-text-re">100家企业/100位人员</td> <td>100家企业</td> </tr> <tr> <td class="vip-text-bl">风险扫描</td> <td class="vip-text-re">不限次</td> <td><span class="x">×</span></td> </tr> <tr> <td class="vip-text-bl">更多号码</td> <td class="vip-text-re">不限次</td> <td><span class="x">×</span></td> </tr> </table> </div> <input name="goods_id" type="hidden" value="17"> </div> </div> </div> <script type="text/javascript">
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
</script> </body> </html>
"""
postData = {
    'html': html,  # 当type为1/2必有
    'type': 1,  # 任何情况必有，0为保留字段 1代表列表页 2代表详情页
    'cid': '',  # type2有，如果没有并且html存在，将会尝试从html中解析，如果还解析失败，将不会返回股权穿透图。
    'url': '',  # 当html存在时必有
    'companyName': '深圳市腾讯计算机系统有限公司'  # 当使用收费API时必有，如果没有并且html存在，将会尝试从html中解析，如果还解析失败，将不会返回收费API数据
}

resp = requests.post('http://121.9.245.186:9001/beyebe/parse.go', data=postData)
# resp = requests.post('http://localhost:9001/beyebe/parse.go', data=postData)

print(resp.text)
