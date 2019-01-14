from bean.companyBean import CompanyBean

if __name__ == '__main__':
    company = CompanyBean()
    company.companyName = 'test'  # 爬虫对item赋值
    item = company.getDict()  # object转dict
    company2 = CompanyBean()
    company2.__dict__ = item  # dict转object
    print(company2.__dict__)
