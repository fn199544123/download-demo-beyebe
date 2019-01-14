import copy


class CompanyBean:
    def __init__(self):
        self.gongShangXinXi = self.GongShangXinXi()
        self.companyName = None  # 公司名
        self.companyId = None  # 公司ID
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
    class GongShangXinXi:
        def __init__(self):
            self.test = None
    def getDict(self):
        itemDict = copy.deepcopy(self.__dict__)
        keyList = list(itemDict.keys())
        for key in keyList:
            if itemDict[key] is None:
                itemDict.pop(key)
                continue
            if 'class' in str(type(itemDict[key])):
                itemDict[key] = itemDict[key].__dict__.copy()
        return itemDict


if __name__ == '__main__':
    a = CompanyBean()
    a.gongShangXinXi.test = 1
    print(a.getDict())
    print(CompanyBean().gongShangXinXi.test)
    print(CompanyBean().getDict())