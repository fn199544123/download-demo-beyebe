import copy
import json

import datetime
from datetime import date


class CompanyBean:
    def __init__(self):
        self.cid = None
        self.tou_bu_xin_xi = self.TouBuXinXi()
        self.gong_shang_xin_xi = self.GongShangXinXiBean()
        self.gu_dong_xin_xi = self.GuDongXinXiBean()
        self.lstGuDongXiXin = []
        self.zhu_yao_ren_yuan = self.ZhuYaoRenYuanBean()
        self.lstZhuYaoRenYuan = []
        self.bian_geng_ji_lu = self.BianGengJiLuBean()
        self.lstBianGengJiLu = []
        self.xing_zheng_xu_ke = self.XingZhengXuKeBean()
        self.di_kuai_gong_shi = self.DiKuaiGongShiBean()
        self.gou_di_xin_xi = self.GouDiXinXiBean()
        self.tu_di_zhuan_rang = self.TuDiZhuanRangBean()
        self.xing_zheng_chu_fa = self.XingZhengChuFaBean()
        self.gu_quan_chu_zhi = self.GuQuanChuZhiBean()
        self.dong_chan_di_ya = self.DongChanDiYaBean()
        self.tu_di_di_ya = self.TuDiDiYaBean()
        self.jing_ying_yi_chang = self.JingYingYiChangBean()
        self.lstJingYingYiChang = []
        self.shang_biao_xin_xi = self.ShangBiaoXinXiBean()
        self.lstShangBiaoXinXi = []
        self.zhuan_li_xin_xi = self.ZhuanLiXinXiBean()
        self.lstZhuanLiXinXi = []
        self.ruan_jian_zhu_zuo_quan = self.RuanJianZhuZuoQuanBean()
        self.lstRuanJianZhuZuoQuan = []
        self.qi_ye_nian_bao_ji_ben_xin_xi = self.QiYeNianBao_JiBenXinXiBean()
        self.qi_ye_nian_bao_wang_zhan = self.QiYeNianBao_WangZhanBean()
        self.lstQiYeNianBao_WangZhan = []
        self.qi_ye_nian_bao_gu_dong_fa_qi_ren = self.QiYeNianBao_GuDongFaQiRenBean()
        self.lstQiYeNianBao_GuDongFaQiRen = []
        self.qi_ye_nian_bao_qi_ye_zi_chan = self.QiYeNianBao_QiYeZiChanBean()
        self.gu_quan_bian_geng = self.GuQuanBianGengBean()
        self.lstGuQuanBianGeng = []
        self.qi_ye_nian_bao_she_bao_xin_xi = self.QiYeNianBao_SheBaoXinXiBean()
        self.qi_ye_nian_bao_xiu_gai_xin_xi = self.QiYeNianBao_XiuGaiXinXi()
        self.lstXiuGaiXinXi = []
        self.wang_zhan_xin_xi = self.WangZhanXinXiBean()
        self.fen_zhi_ji_gou = self.FenZhiJiGouBean()
        self.lstFenZhiJiGou = []
        self.biao_tou_qi_ye_ji_ben_xin_xi = self.BiaoTou_QiYeJiBenXinXiBean()
        self.zhao_pin_xin_xi = self.ZhaoPinXinXI()
        self.lstZhaoPinXinXI = []

    # 头部信息
    class TouBuXinXi:
        def __init__(self):
            self.legalRepresentative = None      #法人代表
            self.survivalStatus = None   #公司存续状态
            self.phone = None    #电话号码
            self.website = None    #官网
            self.companyName = None      #公司名
            self.address = None      #公司地址
            self.Email = None      #公司邮箱
            self.logo = None       #logo

    # 工商信息
    class GongShangXinXiBean:
        def __init__(self):
            self.legalRepresentative = None   #法人代表
            self.companyName = None  # 公司名
            # self.companyId = None  # 公司ID
            self.registerId = None  # 注册号
            self.societyId = None  # 统一社会信用代码
            self.taxpayerId = None  # 纳税人识别号
            self.orgCode = None  # 组织机构代码
            self.entType = None  # 公司类型
            self.industry = None  # 所属行业
            self.busStatus = None  # 经营状态
            self.allMoney = None  # 注册资本
            self.canUseMoney = None  # 实缴资本
            self.regTime = None  # 成立日期
            self.optPeriod = None  # 营业期限
            self.busScope = None  # 经营范围
            self.regAuthority = None  # 登记机关
            self.appDate = None  # 核准日期
            self.busPlace = None  # 企业地址
            self.admArea = None  # 所属地区
            self.englishName = None  # 英文名
            self.usedName = None  # 曾用名
            self.contributorsSize = None  # 参保人数
            self.staffSize = None  # 人员规模

    # 股东信息
    class GuDongXinXiBean:
        def __init__(self):
            self.shName = None  # 股东
            self.percentInfo = None  # 持股比例
            self.subMoney = None  # 认缴出资额（万元）
            self.subDate = None  # 认缴出资日期
            self.actMoney = None  # 实缴出资额
            self.actDate = None  # 实缴出资日期

    # 主要人员
    class ZhuYaoRenYuanBean:
        def __init__(self):
            self.personName = None  # 姓名
            self.position = None  # 职务

    # 变更记录
    class BianGengJiLuBean:
        def __init__(self):
            self.changeProject = None  # 变更项目
            self.beforeChangeDetail = None  # 变更前
            self.afterChangeDetail = None  # 变更后
            self.changeDate = None  # 变更日期

    # 行政许可
    class XingZhengXuKeBean:
        def __init__(self):
            self.fileNum = None  # 许可文件编号
            self.fileName = None  # 许可文件名称
            self.fileOpenTime = None  # 有效期自
            self.fileEndTime = None  # 有效期至
            self.fileDiv = None  # 许可机关
            self.fileContent = None  # 许可内容

    # 地块公示
    class DiKuaiGongShiBean:
        def __init__(self):
            self.tdPosition = None  # 地块位置
            self.tdAuthority = None  # 发布机关
            self.tdArea = None  # 行政区
            self.tdDate = None  # 发布日期

    # 购地信息
    class GouDiXinXiBean:
        def __init__(self):
            self.gdPosition = None  # 土地坐落
            self.gdUse = None  # 土地用途
            self.totalArea = None  # 总面积公顷
            self.gdArea = None  # 行政区
            self.gdSupply = None  # 供应方式
            self.signDate = None  # 签订日期

    # 土地转让
    class TuDiZhuanRangBean:
        def __init__(self):
            self.gdPosition = None  # 土地坐落
            self.gdArea = None  # 行政区
            self.oriUser = None  # 原土地使用权人
            self.nowUser = None  # 现有土地使用权人

    # 行政处罚
    class XingZhengChuFaBean:
        def __init__(self):
            self.punNumber = None  # 决定书文号
            self.punType = None  # 违法行为类型
            self.punDetail = None  # 行政处罚内容
            self.punOfficeName = None  # 决定机关
            self.punDate = None  # 决定日期
            self.noticeDate = None  # 公示日期

    # 股权出质
    class GuQuanChuZhiBean:
        def __init__(self):
            self.equNumber = None  # 等级编号
            self.equInvestor = None  # 出质人
            self.equPledgee = None  # 质权人
            self.equAmount = None  # 出质股权数额
            self.regDate = None  # 设立登记日期
            self.equStatus = None  # 状态

    # 动产抵押
    class DongChanDiYaBean:
        def __init__(self):
            self.regNumber = None  # 登记编号
            self.regDate = None  # 登记日期
            self.regAuthority = None  # 登记机关
            self.chaAmount = None  # 被担保债权数额
            self.chaStatus = None  # 状态

    # 土地抵押
    class TuDiDiYaBean:
        def __init__(self):
            self.gdPosition = None  # 土地抵押
            self.morPeriod = None  # 起止时间
            self.gdArea = None  # 行政区
            self.morArea = None  # 抵押面积公顷
            self.morUsage = None  # 抵押土地用途

    # 经营异常
    class JingYingYiChangBean:
        def __init__(self):
            self.inDate = None  # 列入日期
            self.inReason = None  # 列入经营异常名录原因
            self.regAuthority = None  # 作出决定机关
            self.outDate = None  # 移除日期
            self.outReason = None  # 移除经营异常名录原因
            self.outAuthority = None  # 移除决定机关

    # 商标信息
    class ShangBiaoXinXiBean:
        def __init__(self):
            self.traName = None  # 商标名
            self.appDate = None  # 申请时间
            self.regNumber = None  # 注册号
            self.traType = None  # 国际分类
            self.processStatus = None  # 状态

    # 专利信息
    class ZhuanLiXinXiBean:
        def __init__(self):
            self.appDate = None  # 公开公告日期
            self.patName = None  # 名称
            self.patPublicNumber = None  # 公开公告号
            self.classNumber = None  # 专利类型
            self.patentAbstract = None   #摘要
            self.patentInventor = None    #发明人

    # 软件著作权
    class RuanJianZhuZuoQuanBean:
        def __init__(self):
            self.regDate = None  # 登记批准日期
            self.softName = None  # 软件名称
            self.simpleName = None  # 软件简称
            self.regNumber = None  # 登记号
            self.version = None  # 版本号
            self.pubDate = None  # 发布日期

    # 企业年报-基本信息
    class QiYeNianBao_JiBenXinXiBean:
        def __init__(self):
            self.regNumber = None  # 注册号
            self.companyName = None  # 公司名
            self.busStatus = None  # 企业经营状态
            self.phonenumber = None  # 企业联系电话
            self.isChange = None  # 有限责任本公司。。。
            self.isInvest = None  # 企业是否有投资。。。
            self.email = None  # 电子邮箱
            self.location = None  # 企业通信地址
            self.allPeople = None  # 从业人数
            self.postcode = None  # 邮政编码
            self.webSite = None    #是否有网站或网点

    # 企业年报-网站或网店信息
    class QiYeNianBao_WangZhanBean:
        def __init__(self):
            self.shopType = None  # 类型
            self.shopName = None  # 名称
            self.shopUrl = None  # 网址
            self.yearNumber = None  # 年度

    # 企业年报-股东发起人出资信息
    class QiYeNianBao_GuDongFaQiRenBean:
        def __init__(self):
            self.shareholders = None  # 发起人
            self.subMoney = None  # 认缴出资额（万元）
            self.subTime = None  # 认缴出资时间
            self.subType = None  # 认缴出资方式
            self.actMoney = None  # 实缴出资额（万元）
            self.actTime = None  # 实缴出资时间
            self.actType = None  # 实缴出资方式
            self.yearNumber = None  # 年度

    # 企业年报-企业资产状况信息
    class QiYeNianBao_QiYeZiChanBean:
        def __init__(self):
            self.proSummary = None  # 资产总额
            self.proOwn = None  # 所有者权益合计
            self.saleSummary = None  # 营业总收入
            self.profitsSummary = None  # 利润总额
            self.mainPercent = None  # 营业总收入中主营业务收入
            self.netProfits = None  # 净利润
            self.taxSummay = None  # 纳税总额
            self.debitSummary = None  # 负债总额
            self.yearNumber = None  # 年度

    # 股权变更
    class GuQuanBianGengBean:
        def __init__(self):
            self.shName = None  # 股东
            self.beforeRatio = None  # 变更前股权比例
            self.afterRatio = None  # 变更后股权比例
            self.changeDate = None  # 股权变更日期
            self.year = None      #年份

    # 企业年报-社保信息
    class QiYeNianBao_SheBaoXinXiBean:
        def __init__(self):
            self.endowmentInsAmount = None  # 城镇职工基本养老保险
            self.medicalInsAmount = None  # 职工基本医疗保险
            self.meternityInsAmount = None  # 生育保险
            self.injuryInsAmount = None  # 工伤保险
            self.unemployInsAmount = None  # 失业保险
            self.endowmentInsBase = None  # 单位参加城镇职工基本养老保险缴费基数
            self.medicalInsBase = None  # 单位参加职工基本医疗保险缴费基数
            self.meternityInsBase = None  # 单位参加生育保险缴费基数
            self.injuryInsBase = None  # 单位参加工伤保险缴费基数
            self.unemployInsBase = None  # 单位参加失业保险缴费基数
            self.endowmentInsAct = None  # 参加城镇职工基本养老保险本期实际缴费金额
            self.medicalInsAct = None  # 参加职工基本医疗保险本期实际缴费金额
            self.meternityInsAct = None  # 参加生育保险本期实际缴费金额
            self.injuryInsAct = None  # 参加工伤保险本期实际缴费金额
            self.unemployInsAct = None  # 参加失业保险本期实际缴费金额
            self.endowmentInsOwe = None  # 单位参加城镇职工基本养老保险累计欠缴金额
            self.medicalInsOwe = None  # 单位参加职工基本医疗保险累计欠缴金额
            self.meternityInsOwe = None  # 单位参加生育保险累计欠缴金额
            self.injuryInsOwe = None  # 单位参加工伤保险累计欠缴金额
            self.unemployInsOwe = None  # 单位参加失业保险累计欠缴金额
            self.yearNumber = None  # 年度

    # 企业年报-修改信息
    class QiYeNianBao_XiuGaiXinXi:
        def __init__(self):
            self.befoRerevise = None     #修改前
            self.afterRerevise = None  #修改后
            self.changeContent = None   #修改内容
            self.changeDate = None  # 股权变更日期
            self.year = None  # 年份

    # 招聘信息
    class ZhaoPinXinXI:
        def __init__(self):
            self.companyName = None      #公司名
            self.jobTitle = None         #职位名称
            self.type = None             #职能类别
            self.salaryRange = None      #薪资范围
            self.qzEmployQuery = None    #工作性质
            self.welfare = None          #福利
            self.yearsReq = None         #年限要求
            self.eduReq = None           #学历要求
            self.count = None            #招聘人数
            self.duty = None             #岗位职责
            self.des = None              #职位描述
            self.city = None             #工作城市
            self.address = None          #工作详细地址
            self.phone = None            #联系电话
            self.publicDate = None       #发布日期
            self.updateTime = None       #更新日期

    # 网站信息
    class WangZhanXinXiBean:
        def __init__(self):
            self.webURL = None  # 网址
            self.webName = None  # 网站名称
            self.webDomain = None  # 域名
            self.webPermission = None  # 网站备案/许可证号
            self.checkDate = None  # 审核时间

    # 分支机构
    class FenZhiJiGouBean:
        def __init__(self):
            self.companyName = None  # 分支公司名

    # 表头-企业基本信息
    class BiaoTou_QiYeJiBenXinXiBean:
        def __init__(self):
            self.companyName = None  # 公司名称
            self.companyTel = None  # 电话
            self.status = None  # 状态
            self.workPerson = None  # 企业法人
            self.companyEmail = None  # 邮箱
            self.hasNetshop = None  # 网站
            self.companyAddress = None  # 公司地址
            self.otherCompany = None  # 曾用名

    #股权穿透图
    # class GuQuanChuanTouTu:
    #     def __init__(self):
    #         self.companyName = None      #公司名
    #         self.KeyNo = None      #股东id
    #         self.Name = None      #股东名
    #         self.CompanyCode = None      #机构代码
    #         self.Percent = None      #持股比
    #         self.PercentTotal = None      #总百分比
    #         self.Level = None      #
    #         self.Org = None      #
    #         self.ShouldCapi = None      #认缴出资额
    #         self.StockRightNum = None      #
    #         self.DetailCount = None      #
    #         self.Tags = None      #
    #         self.DetailList = None      #

    # MMP-encoder
    class MMPEncoder(json.JSONEncoder):
        def default(self, obj):
            strType = str(type(obj))
            if 'Bean' in strType:
                return obj.__dict__.copy()
            elif isinstance(obj, datetime.datetime):
                return int(obj.timestamp())
            elif isinstance(obj, date):
                raise Exception("百度将date变成时间戳")
            else:
                return super(CompanyBean.MMPEncoder, self).default(obj)

    def getDictAll(self):
        """
        将对象序列化成字典
        :return:
        """
        return json.loads(json.dumps(self, cls=CompanyBean.MMPEncoder))

    def getDictWithoutNone(self):
        """
        将对象序列化成不含None的字典
        :return:
        """

        itemDict = json.loads(json.dumps(self, cls=self.MMPEncoder))
        keyList = list(itemDict.keys())
        for key in keyList:
            if type(itemDict[key]) == type({}):
                keyList2 = list(itemDict[key].keys())
                for key2 in keyList2:
                    if not itemDict[key][key2]:
                        itemDict[key].pop(key2)
            if type(itemDict[key]) == type([]):
                for item in itemDict[key]:
                    keyList2 = list(item.keys())
                    for key2 in keyList2:
                        if not item[key2]:
                            item.pop(key2)
            if not itemDict[key]:
                itemDict.pop(key)
        return itemDict

    @staticmethod
    def IDEncodeDecode(str):
        strA = str[0]
        strB = str[-1]
        strMid = str[1:len(str) - 1]
        return strA + strMid[::-1] + strB

if __name__ == '__main__':
    # 塞数组数据范例
    companyBean = CompanyBean()
    gudongxinxi1 = CompanyBean.GuDongXinXiBean()
    gudongxinxi1.shName = "方楠大股东"
    gudongxinxi2 = CompanyBean.GuDongXinXiBean()
    gudongxinxi2.shName = "谢云大股东"
    companyBean.lstGuDongXiXin.append(gudongxinxi1)
    companyBean.lstGuDongXiXin.append(gudongxinxi2)
    # print(companyBean.getDictWithoutNone())
    # print(companyBean.getDictAll())
