# -*- coding:utf-8 -*-
import traceback
from urllib.parse import quote
import urllib
from bs4 import BeautifulSoup
import re
import datetime
from CompanyBean import CompanyBean
import requests
import json


class analysize():
    # 详情页基本信息解析
    @staticmethod
    def parse_jibenxinxi(html=None):
        if html:
            soup = BeautifulSoup(html, 'lxml')
            companybean = CompanyBean()
            cid = urllib.parse.quote(soup.find('link').attrs['href'])
            cid = cid.split('_')[1].split(".")[0]
            cid = companybean.IDEncodeDecode(cid)
            companybean.cid = cid
            """头部信息"""
            if soup.find('div', id = 'company-top'):
                toubu = soup.find('div', id='company-top').find('div', class_="content")
                try:
                    companybean.tou_bu_xin_xi.survivalStatus = soup.find('div', class_="row tags").text.strip().split(
                        ' ')
                except:
                    companybean.tou_bu_xin_xi.survivalStatus = None
                companybean.tou_bu_xin_xi.legalRepresentative = soup.find('a', class_='bname').text.strip().replace(' ', '').replace('\n', '')
                companybean.tou_bu_xin_xi.companyName = soup.find('div', class_="row title").text.strip()
                companybean.tou_bu_xin_xi.logo = soup.find('div', class_="logo").find('img').attrs['src']
                for _ in toubu.find_all('div', class_="row"):
                    if re.search('电话：\s*(.*?)\s', _.text.replace('\n', '')):
                        companybean.tou_bu_xin_xi.phone = re.search('电话：\s*(.*?)\s', _.text.replace('\n', '')).group(1)
                    if re.search('邮箱：\s*(.*?)\s', _.text.replace('\n', '')):
                        companybean.tou_bu_xin_xi.Email = re.search('邮箱：\s*(.*?)\s', _.text.replace('\n', '')).group(1)
                    if re.search('地址：\s*(.*?)\s', _.text.replace('\n', '')):
                        companybean.tou_bu_xin_xi.address = re.search('地址：\s*(.*?)\s', _.text.replace('\n', '')).group(
                            1)
                if not companybean.tou_bu_xin_xi.phone:
                    companybean.tou_bu_xin_xi.phone = '-'
                if not companybean.tou_bu_xin_xi.Email:
                    companybean.tou_bu_xin_xi.Email = '-'
                if not companybean.tou_bu_xin_xi.address:
                    companybean.tou_bu_xin_xi.address = '-'
                guanwang = ''.join([str(_) for _ in toubu.find_all('span', class_="cvlu")])
                if '进入官网' in guanwang:
                    companybean.tou_bu_xin_xi.website = re.search('title="进入官网">\s*(.*?)<', guanwang).group(1)
                else:
                    companybean.tou_bu_xin_xi.website = '-'

            """工商信息"""
            if soup.find('section', id='Cominfo'):
                name = soup.find('h1').text
                name = {'GongSiMing': name}
                farendaibiao = soup.find('a', class_='bname').text.strip().replace(' ', '').replace('\n', '')
                companybean.gong_shang_xin_xi.legalRepresentative = farendaibiao
                crude_gongshangxinxi = soup.find('section', id='Cominfo').find_all('table', class_='ntable')[1]
                tr = crude_gongshangxinxi.find_all('tr')
                td_1 = ['ZhuCeZiBen', 'ShiJiaoZiBen', 'JingYingZhuangTai', 'ChengLiRiQi', 'XinYongDaiMa', 'ShiBieHao',
                        'ZhuCeHao', 'ZuZhiJiGouDaiMa', 'GongSiLeiXing', 'SuoShuHangYe', 'HeZhunRiQi', 'DengJiJiGuan',
                        'SuoShuDiQu', 'YingWenMing', 'CengYongMing', 'CanBaoRenYuan', 'RenYuanGuiMo', 'YingYeQiXian',
                        'QiYeDiZhi', 'JingYingFanWei']
                td_2 = []
                for _ in tr:
                    for i in _.find_all('td', class_=''):
                        # i = None if i.text.strip().replace('\n', '').replace(' ', '') == '-' \
                        #     else i.text.strip().replace('\n', '').replace(' ', '')
                        i = i.text.strip().replace('\n', '').replace(' ', '')
                        td_2.append(i)
                gongshangxinxi = dict(zip(td_1, td_2))
                gongshangxinxi.update(name)
                companybean.gong_shang_xin_xi.companyName = gongshangxinxi.get('GongSiMing')
                # companybean.gong_shang_xin_xi.companyId = re.search('firm_(.*?)\.',
                #                                                     soup.find('link').attrs['href']).group(1)
                companybean.gong_shang_xin_xi.registerId = gongshangxinxi.get('ZhuCeHao')
                companybean.gong_shang_xin_xi.societyId = gongshangxinxi.get('XinYongDaiMa')
                companybean.gong_shang_xin_xi.taxpayerId = gongshangxinxi.get('ShiBieHao')
                companybean.gong_shang_xin_xi.orgCode = gongshangxinxi.get('ZuZhiJiGouDaiMa')
                companybean.gong_shang_xin_xi.entType = gongshangxinxi.get('GongSiLeiXing')
                companybean.gong_shang_xin_xi.industry = gongshangxinxi.get('SuoShuHangYe')
                companybean.gong_shang_xin_xi.busStatus = gongshangxinxi.get('JingYingZhuangTai')
                companybean.gong_shang_xin_xi.allMoney = gongshangxinxi.get('ZhuCeZiBen')
                companybean.gong_shang_xin_xi.canUseMoney = gongshangxinxi.get('ShiJiaoZiBen')
                if gongshangxinxi.get('ChengLiRiQi') == '-':
                    companybean.gong_shang_xin_xi.regTime = '-'
                else:
                    companybean.gong_shang_xin_xi.regTime = datetime.datetime.strptime(
                        gongshangxinxi.get('ChengLiRiQi'), "%Y-%m-%d")
                companybean.gong_shang_xin_xi.optPeriod = gongshangxinxi.get('YingYeQiXian')
                companybean.gong_shang_xin_xi.busScope = gongshangxinxi.get('JingYingFanWei')
                companybean.gong_shang_xin_xi.regAuthority = gongshangxinxi.get('DengJiJiGuan')
                if gongshangxinxi.get('HeZhunRiQi') == '-':
                    companybean.gong_shang_xin_xi.appDate = '-'
                else:
                    companybean.gong_shang_xin_xi.appDate = datetime.datetime.strptime(gongshangxinxi.get('HeZhunRiQi'),
                                                                                       "%Y-%m-%d")
                companybean.gong_shang_xin_xi.busPlace = gongshangxinxi.get('QiYeDiZhi').replace('查看地图', '').replace('附近公司', '')
                companybean.gong_shang_xin_xi.admArea = gongshangxinxi.get('SuoShuDiQu')
                companybean.gong_shang_xin_xi.englishName = gongshangxinxi.get('YingWenMing')
                companybean.gong_shang_xin_xi.usedName = gongshangxinxi.get('CengYongMing')
                if gongshangxinxi.get('CanBaoRenYuan') == '-':
                    companybean.gong_shang_xin_xi.contributorsSize = '-'
                else:
                    companybean.gong_shang_xin_xi.contributorsSize = int(gongshangxinxi.get('CanBaoRenYuan'))
                companybean.gong_shang_xin_xi.staffSize = gongshangxinxi.get('RenYuanGuiMo')

            """股东信息"""
            if soup.find('section', id='Sockinfo'):
                gudongxinxi = []
                gudongxinxi_title = []
                crude_gudongxinxi_title = [_.text for _ in soup.find('section', id='Sockinfo') \
                    .find('table', class_="ntable ntable-odd").find_all('th')]
                for _ in crude_gudongxinxi_title:
                    if '股东' in _:
                        gudongxinxi_title.append('shName')
                    if '持股比例' in _:
                        gudongxinxi_title.append('percentInfo')
                    if '认缴出资额' in _:
                        gudongxinxi_title.append('subMoney')
                    if '认缴出资日期' in _:
                        gudongxinxi_title.append('subDate')
                    if '实缴出资额' in _:
                        gudongxinxi_title.append('actMoney')
                    if '实缴出资日期' in _:
                        gudongxinxi_title.append('actDate')
                crude_gudongxinxi = [_ for _ in soup.find('section', id='Sockinfo')
                    .find('table', class_="ntable ntable-odd").find_all('tr', recursive=False)]
                for _ in crude_gudongxinxi:
                    if _.find_all('td'):
                        # i = [None if i.text.replace('\n', ' ').replace(' ', '').replace('>', '') == '-'
                        #      else i.text.replace('\n', ' ').replace(' ', '').replace('>', '')
                        #      for i in _.find_all('td')]
                        i = [i.text.replace('\n', ' ').replace(' ', '').replace('>', '') for i in _.find_all('td', recursive=False)]
                        gudongxinxi.append(i)
                for _ in gudongxinxi:
                    _.pop(0)
                    for num, i in enumerate(_):
                        if i is None:
                            continue
                        if '他关联' in i:
                            _[num] = re.sub('他关联.*', '', i)

                gudongxinxi1 = companybean.GuDongXinXiBean()
                for i in gudongxinxi:
                    for num, _ in enumerate(gudongxinxi_title):
                        if 'shName' == _:
                            if i[num]:
                                gudongxinxi1.shName = i[num]
                        if 'percentInfo' == _:
                            if i[num]:
                                gudongxinxi1.percentInfo = i[num]
                        if 'subMoney' == _:
                            if i[num] == '-':
                                gudongxinxi1.subMoney = '-'
                            elif i[num]:
                                gudongxinxi1.subMoney = float(i[num])
                        if 'subDate' == _:
                            if i[num] == '-':
                                gudongxinxi1.subDate = '-'
                            elif i[num]:
                                gudongxinxi1.subDate = datetime.datetime.strptime(i[num], "%Y-%m-%d")
                        if 'actMoney' == _:
                            if i[num] == '-':
                                gudongxinxi1.actMoney = '-'
                            elif i[num]:
                                gudongxinxi1.actMoney = float(i[num])
                        if 'actDate' == _:
                            if i[num] == '-':
                                gudongxinxi1.actDate = '-'
                            elif i[num]:
                                gudongxinxi1.actDate = datetime.datetime.strptime(i[num], "%Y-%m-%d")
                    companybean.lstGuDongXiXin.append(gudongxinxi1)
                    gudongxinxi1 = companybean.GuDongXinXiBean()

            """主要人员"""
            if soup.find('section', id='Mainmember'):
                zhuyaorenyuan = []
                zhuyaorenyuan_title = []
                crude_zhuyaorenyuan_title = [_.text.replace('\n', '').replace(' ', '')
                                             for _ in soup.find('section', id='Mainmember')
                                                 .find('table', class_="ntable ntable-odd").find_all('th')]
                crude_zhuyaorenyuan = [_.find_all('td') for _ in
                                       soup.find('section', id='Mainmember')
                                           .find('table', class_="ntable ntable-odd").find_all('tr')]
                for _ in crude_zhuyaorenyuan_title:
                    if '姓名' in _:
                        zhuyaorenyuan_title.append('personName')
                    if '职务' in _:
                        zhuyaorenyuan_title.append('position')
                for _ in crude_zhuyaorenyuan:
                    if _:
                        zhuyaorenyuan.append([i.text.replace('\n', '').replace(' ', '') for i in _])
                for _ in zhuyaorenyuan:
                    _.pop(0)
                    for num, i in enumerate(_):
                        if i is None:
                            continue
                        if '他关联' in i:
                            _[num] = re.sub('他关联.*', '', i)
                        # if '-' == i:
                        #     _[num] = None

                zhuyaorenyuan1 = companybean.ZhuYaoRenYuanBean()
                for i in zhuyaorenyuan:
                    for num, _ in enumerate(zhuyaorenyuan_title):
                        if 'personName' == _:
                            if i[num]:
                                zhuyaorenyuan1.personName = i[num]
                        if 'position' == _:
                            if i[num]:
                                zhuyaorenyuan1.position = i[num]
                    companybean.lstZhuYaoRenYuan.append(zhuyaorenyuan1)
                    zhuyaorenyuan1 = companybean.ZhuYaoRenYuanBean()

            """变更记录"""
            if soup.find('section', id='Changelist'):
                biangengjilu = []
                biangengjilu_title = []
                crude_biangengjilu_title = [_.text for _ in
                                            soup.find('section', id='Changelist').find('table',
                                                                                       class_="ntable").find_all('th')]
                for _ in crude_biangengjilu_title:
                    if '变更日期' in _:
                        biangengjilu_title.append('changeDate')
                    if '变更项目' in _:
                        biangengjilu_title.append('changeProject')
                    if '变更前' in _:
                        biangengjilu_title.append('beforeChangeDetail')
                    if '变更后' in _:
                        biangengjilu_title.append('afterChangeDetail')

                crude_biangengjilu = [_.find_all('td') for _ in
                                      soup.find('section', id='Changelist').find('table', class_="ntable").find_all(
                                          'tr')]
                for _ in crude_biangengjilu:
                    if _:
                        biangengjilu.append([i.text.replace(' ', '') for i in _])
                for _ in biangengjilu:
                    _.pop(0)
                    for num, i in enumerate(_):
                        if i is None:
                            continue
                        # if '-' == i:
                        #     _[num] = None

                biangengjilu1 = companybean.BianGengJiLuBean()
                for i in biangengjilu:
                    for num, _ in enumerate(biangengjilu_title):
                        if 'changeDate' == _:
                            if i[num] == '-':
                                biangengjilu1.changeDate = '-'
                            elif i[num]:
                                biangengjilu1.changeDate = datetime.datetime.strptime(i[num], "%Y-%m-%d")
                        if 'changeProject' == _:
                            if i[num]:
                                biangengjilu1.changeProject = i[num]
                        if 'beforeChangeDetail' == _:
                            if i[num]:
                                biangengjilu1.beforeChangeDetail = i[num]
                        if 'afterChangeDetail' == _:
                            if i[num]:
                                biangengjilu1.afterChangeDetail = i[num]
                    companybean.lstBianGengJiLu.append(biangengjilu1)
                    biangengjilu1 = companybean.BianGengJiLuBean()

            """分支机构"""
            if soup.find('section', id="Subcom"):
                _fenzhijigou = [_ for _ in soup.find('section', id="Subcom").find_all('td')]
                _fenzhijigou = [_.text.strip() for _ in _fenzhijigou]
                fenzhijigou1 = companybean.FenZhiJiGouBean()
                for num, _ in enumerate(_fenzhijigou):
                    if num % 2 == 1:
                        fenzhijigou1.companyName = _
                        companybean.lstFenZhiJiGou.append(fenzhijigou1)
                    fenzhijigou1 = companybean.FenZhiJiGouBean()
            return {'jibenxinxi': companybean.getDictWithoutNone()}

    # 详情页基本信息—股权架构图补全
    @staticmethod
    def parseGuQuanJiaGouTu(cid=None):
        try:
            if cid:
                _jiagoutu = {}
                header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
                # url = "http://192.168.10.101:7681/beyebe/platform/get.go?url=" \
                #       "https://www.qichacha.com/cms_guquanmap3?keyNo={}&isBuffer=7776000".format(urllib.parse.quote(cid))
                url = "https://www.qichacha.com/cms_guquanmap3?keyNo={}&isBuffer=7776000".format(urllib.parse.quote(cid))
                try:
                    if not requests.get(url, headers=header, timeout=5).text == 'null':
                        resp = requests.get(url, headers=header, timeout=5)
                        resp = json.loads(resp.text)
                        print("解析对象:")
                        print(resp.text)
                        gudong = {'gudong': resp.get('gudong')}
                        touzi = {'touzi': resp.get('touzi')}
                        syr = {'syr': resp.get('syr')}
                        kg = {'kg': resp .get('kg')}
                        kzr = {'kzr': resp.get('kzr')}
                        _jiagoutu.update(gudong)
                        _jiagoutu.update(touzi)
                        _jiagoutu.update(syr)
                        _jiagoutu.update(kg)
                        _jiagoutu.update(kzr)
                        jiagoutu = {'jiagoutu': _jiagoutu}
                        return jiagoutu
                except requests.exceptions.ConnectTimeout:
                    pass
                except ConnectionError:
                    pass
                else:
                    return {}
        except:
            traceback.print_exc()
            return {}
    # 收费API-法律诉讼-裁判文书
    @staticmethod
    def parse_FLSS_CaiPanWenShu(companyName=None):
        if companyName:
            try:
                resp = requests.get('http://121.9.245.186:9030/api/judgeQuery?input={}&isBuffer=7776000'
                                    .format(companyName), timeout=5).text
                resp = json.loads(resp)
                assert resp.get('message') == 'request success'
                if resp.get('data'):
                    FLSS_panjueshu = {'FLSS_panjueshu': resp.get('data').get('result')}
                else:
                    FLSS_panjueshu = {}
                return FLSS_panjueshu
            except AssertionError:
                return {'error': ['法律诉讼-裁判文书;message:' + resp.get('message')]}
            except requests.exceptions.ConnectTimeout:
                return {'error': ['法律诉讼-裁判文书:连接超时']}
            except ConnectionError:
                return {'error': ['法律诉讼-裁判文书:连接异常']}

    # 收费API-经营风险-经营异常
    @staticmethod
    def parse_JYFX_JingYingYiChang(companyName=None):
        if companyName:
            try:
                companybean = CompanyBean()
                resp = requests.get('http://121.9.245.186:9030/api/getAbnormalOperatingCompanyInfos?companyName={}&isBuffer=7776000'
                                    .format(companyName), timeout=5).text
                resp = json.loads(resp)
                assert resp.get('message') == 'request success'
                if resp.get('data'):
                    jingyingyichang1 = companybean.JingYingYiChangBean()
                    for _ in resp.get('data').get('result'):
                        jingyingyichang1.inDate = _.get('listDate') if _.get('listDate') else '-'
                        jingyingyichang1.outDate = _.get('removeDate') if _.get('removeDate') else '-'
                        jingyingyichang1.inReason = _.get('putReason') if _.get('putReason') else '-'
                        jingyingyichang1.outReason = _.get('removeReason') if _.get('removeReason') else '-'
                        jingyingyichang1.regAuthority = _.get('listAdministration') if _.get(
                            'listAdministration') else '-'
                        jingyingyichang1.outAuthority = _.get('removeAdministration') if _.get(
                            'removeAdministration') else '-'
                        companybean.lstJingYingYiChang.append(jingyingyichang1)
                        jingyingyichang1 = companybean.JingYingYiChangBean()
                    return companybean.getDictWithoutNone()
                else:
                    return {}
            except AssertionError:
                return {'error': ['经营风险-经营异常;message:' + resp.get('message')]}
            except requests.exceptions.ConnectTimeout:
                return {'error': ['经营风险-经营异常:连接超时']}
            except ConnectionError:
                return {'error': ['经营风险-经营异常:连接异常']}

    # 收费API-招聘信息
    @staticmethod
    def parse_ZhaoPinXinXi(companyName=None):
            if companyName:
                try:
                    resp = requests.get('http://121.9.245.186:9030/api/qzEmployQuery?companyKey={}&isBuffer=7776000'
                        .format(companyName), timeout=5).text
                    resp = json.loads(resp)
                    assert resp.get('message') == 'request success'
                    companybean = CompanyBean()
                    if resp.get('data'):
                        if resp.get('data').get('result'):
                            """招聘信息"""
                            zhaopinxinxi = companybean.ZhaoPinXinXI()
                            if resp.get('data').get('result').get('companyStations'):
                                resp_zhao_pin_xin_xi = resp.get('data').get('result').get('companyStations')
                                for _ in resp_zhao_pin_xin_xi:
                                    zhaopinxinxi.companyName = resp.get('data').get('result').get('companyName')
                                    zhaopinxinxi.jobTitle = _.get('jobTitle')
                                    zhaopinxinxi.type = _.get('type')
                                    zhaopinxinxi.salaryRange = _.get('salaryRange')
                                    zhaopinxinxi.qzEmployQuery = _.get('qzEmployQuery')
                                    zhaopinxinxi.welfare = _.get('welfare')
                                    zhaopinxinxi.yearsReq = _.get('yearsReq')
                                    zhaopinxinxi.eduReq = _.get('eduReq')
                                    zhaopinxinxi.count = _.get('count')
                                    zhaopinxinxi.duty = _.get('duty')
                                    zhaopinxinxi.des = _.get('des')
                                    zhaopinxinxi.city = _.get('city')
                                    zhaopinxinxi.address = _.get('address')
                                    zhaopinxinxi.phone = _.get('phone')
                                    zhaopinxinxi.publicDate = _.get('publicDate')
                                    zhaopinxinxi.updateTime = _.get('updateTime')
                                    companybean.lstShangBiaoXinXi.append(zhaopinxinxi)
                                    zhaopinxinxi = companybean.ZhaoPinXinXI()
                        return companybean.getDictWithoutNone()
                    else:
                        return {}
                except AssertionError:
                    return {'error': ['招聘信息;message:' + resp.get('message')]}
                except requests.exceptions.ConnectTimeout:
                    return {'error': ['招聘信息:连接超时']}
                except ConnectionError:
                    return {'error': ['招聘信息:连接异常']}

    #收费API-企业年报
    @staticmethod
    def parse_QYNB(companyName=None):
        if companyName:
            try:
                resp = requests.get('http://121.9.245.186:9030/api/companyNBDetail?companyKey={}&isBuffer=7776000'
                                    .format(companyName), timeout=5).text
                resp = json.loads(resp)
                assert resp.get('message') == 'request success'
                companybean = CompanyBean()
                if resp.get('data'):
                    if resp.get('data').get('result'):
                        """基本信息"""
                        resp_ji_ben_xin_xi = resp.get('data').get('result').get('nbInfo')
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.regNumber = resp_ji_ben_xin_xi.get('regNumber')
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.companyName = resp_ji_ben_xin_xi.get('companyName')
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.busStatus = resp_ji_ben_xin_xi.get('runStatus')
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.phonenumber = resp_ji_ben_xin_xi.get('phone')
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.isChange = '是' if resp_ji_ben_xin_xi.get('shareTransfer') == '0' else '否'
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.isInvest = '是' if resp_ji_ben_xin_xi.get('otherShare') == '0' else '否'
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.email = resp_ji_ben_xin_xi.get('mail')
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.location = resp_ji_ben_xin_xi.get('address')
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.allPeople = resp_ji_ben_xin_xi.get('members')
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.postcode = resp_ji_ben_xin_xi.get('postCode')
                        companybean.qi_ye_nian_bao_ji_ben_xin_xi.webSite = '是' if resp_ji_ben_xin_xi.get('webSite') == '0' else '否'
                        """企业资产状况信息"""
                        companybean.qi_ye_nian_bao_qi_ye_zi_chan.proSummary = resp_ji_ben_xin_xi.get('totalAssets')
                        companybean.qi_ye_nian_bao_qi_ye_zi_chan.proOwn = resp_ji_ben_xin_xi.get('totalEquity')
                        companybean.qi_ye_nian_bao_qi_ye_zi_chan.saleSummary = resp_ji_ben_xin_xi.get('totalIncome')
                        companybean.qi_ye_nian_bao_qi_ye_zi_chan.profitsSummary = resp_ji_ben_xin_xi.get('toalProfit')
                        companybean.qi_ye_nian_bao_qi_ye_zi_chan.mainPercent = resp_ji_ben_xin_xi.get('mainIncome')
                        companybean.qi_ye_nian_bao_qi_ye_zi_chan.netProfits = resp_ji_ben_xin_xi.get('netProfit')
                        companybean.qi_ye_nian_bao_qi_ye_zi_chan.taxSummay = resp_ji_ben_xin_xi.get('totalTax')
                        companybean.qi_ye_nian_bao_qi_ye_zi_chan.debitSummary = resp_ji_ben_xin_xi.get('totalDebt')
                        companybean.qi_ye_nian_bao_qi_ye_zi_chan.yearNumber = resp_ji_ben_xin_xi.get('year')
                        """网站信息"""
                        qiyenianbao_wangzhan = companybean.QiYeNianBao_WangZhanBean()
                        resp_wangzhan = resp.get('data').get('result').get('wwInfoList')
                        for _ in resp_wangzhan:
                            qiyenianbao_wangzhan.shopName = _.get('name')
                            qiyenianbao_wangzhan.shopType = _.get('type')
                            qiyenianbao_wangzhan.shopUrl = _.get('webSite')
                            qiyenianbao_wangzhan.yearNumber = _.get('year')
                            companybean.lstQiYeNianBao_WangZhan.append(qiyenianbao_wangzhan)
                            qiyenianbao_wangzhan = companybean.QiYeNianBao_WangZhanBean()
                        """股东出资信息"""
                        qiyenianbao_gudongchuzixinxi = companybean.QiYeNianBao_GuDongFaQiRenBean()
                        resp_gu_dong_chu_zi_xin_xi = resp.get('data').get('result').get('gdCzInfoList')
                        for _ in resp_gu_dong_chu_zi_xin_xi:
                            qiyenianbao_gudongchuzixinxi.shareholders = _.get('gd')
                            qiyenianbao_gudongchuzixinxi.subMoney = _.get('rjczeM')
                            qiyenianbao_gudongchuzixinxi.subTime = _.get('rjczsj')
                            qiyenianbao_gudongchuzixinxi.subType = _.get('rjczfs')
                            qiyenianbao_gudongchuzixinxi.actMoney = _.get('sjczeM')
                            qiyenianbao_gudongchuzixinxi.actTime = _.get('czsj')
                            qiyenianbao_gudongchuzixinxi.actType = _.get('czfs')
                            qiyenianbao_gudongchuzixinxi.yearNumber = _.get('year')
                            companybean.lstQiYeNianBao_GuDongFaQiRen.append(qiyenianbao_gudongchuzixinxi)
                            qiyenianbao_gudongchuzixinxi = companybean.QiYeNianBao_GuDongFaQiRenBean()
                        """股权变更"""
                        qiyenianbao_guquanbiangeng = companybean.GuQuanBianGengBean()
                        resp_gu_quan_bian_geng = resp.get('data').get('result').get('gqbgInfoList')
                        for _ in resp_gu_quan_bian_geng:
                            qiyenianbao_guquanbiangeng.shName = _.get('gd')
                            qiyenianbao_guquanbiangeng.beforeRatio = _.get('qgqbl')
                            qiyenianbao_guquanbiangeng.afterRatio = _.get('hgqbl')
                            qiyenianbao_guquanbiangeng.changeDate = _.get('bgsj')
                            qiyenianbao_guquanbiangeng.year = _.get('year')
                            companybean.lstGuQuanBianGeng.append(qiyenianbao_guquanbiangeng)
                            qiyenianbao_guquanbiangeng = companybean.GuQuanBianGengBean()
                        """修改信息,数据源异常"""
                        # qiyenianbao_xiugaixinxi = companybean.QiYeNianBao_XiuGaiXinXi()
                        # resp_xiu_gai_xin_xi = resp.get('data').get('result').get('xgjlInfoList')
                        # for _ in resp_xiu_gai_xin_xi:
                        #     qiyenianbao_xiugaixinxi.befoRerevise = _.get('xgq')
                        #     qiyenianbao_xiugaixinxi.afterRerevise = _.get('xgh')
                        #     qiyenianbao_xiugaixinxi.changeContent = _.get('xgsx')
                        #     qiyenianbao_xiugaixinxi.changeDate = _.get('xgsj')
                        #     qiyenianbao_xiugaixinxi.year = _.get('year')
                        #     companybean.lstXiuGaiXinXi.append(qiyenianbao_xiugaixinxi)
                        #     qiyenianbao_xiugaixinxi = companybean.QiYeNianBao_XiuGaiXinXi()

                        return companybean.getDictWithoutNone()
                    else:
                        return {}
                else:
                    return {}
            except AssertionError:
                return {'error': ['企业年报;message:' + resp.get('message')]}
            except requests.exceptions.ConnectTimeout:
                return {'error': ['企业年报:连接超时']}
            except ConnectionError:
                return {'error': ['企业年报:连接异常']}

    #收费API-知识产权-商标信息
    @staticmethod
    def parse_ZSCQ_ShangBiaoXinXi(companyName=None):
        if companyName:
            try:
                resp = requests.get('http://121.9.245.186:9030/api/orgCompanyBrandList?companyKey={}&isBuffer=7776000'
                                    .format(companyName), timeout=5).text
                resp = json.loads(resp)
                assert resp.get('message') == 'request success'
                companybean = CompanyBean()
                if resp.get('data'):
                    if resp.get('data').get('result'):
                        """商标信息"""
                        zhishichanquan_shangbiaoxinxi = companybean.ShangBiaoXinXiBean()
                        resp_shang_biao_xin_xi = resp.get('data').get('result')
                        for _ in resp_shang_biao_xin_xi:
                            zhishichanquan_shangbiaoxinxi.traName = _.get('name')
                            zhishichanquan_shangbiaoxinxi.appDate = _.get('applicationDate')
                            zhishichanquan_shangbiaoxinxi.regNumber = _.get('regNo')
                            zhishichanquan_shangbiaoxinxi.traType = _.get('branType')
                            zhishichanquan_shangbiaoxinxi.processStatus = _.get('brandProcess')
                            companybean.lstShangBiaoXinXi.append(zhishichanquan_shangbiaoxinxi)
                            zhishichanquan_shangbiaoxinxi = companybean.ShangBiaoXinXiBean()
                    return companybean.getDictWithoutNone()
                else:
                    return {}
            except AssertionError:
                return {'error': ['知识产权-商标信息;message:'+resp.get('message')]}
            except requests.exceptions.ConnectTimeout:
                return {'error': ['知识产权-商标信息:连接超时']}
            except ConnectionError:
                return {'error': ['知识产权-商标信息:连接异常']}

    #收费API-知识产权-专利信息
    @staticmethod
    def parse_ZSCQ_ZhuanLiXinXi(companyName=None):
        if companyName:
            try:
                resp = requests.get('http://121.9.245.186:9030/api/orgCompanyPatentList?companyKey={}&isBuffer=7776000'
                                    .format(companyName), timeout=5).text
                resp = json.loads(resp)
                assert resp.get('message') == 'request success'
                companybean = CompanyBean()
                if resp.get('data'):
                    if resp.get('data').get('result'):
                        """专利信息"""
                        zhishichanquan_zhuanlixinxi = companybean.ZhuanLiXinXiBean()
                        resp_zhuan_li_xin_xi = resp.get('data').get('result')
                        for _ in resp_zhuan_li_xin_xi:
                            zhishichanquan_zhuanlixinxi.appDate = _.get('patentOpenDate')
                            zhishichanquan_zhuanlixinxi.patName = _.get('patentName')
                            zhishichanquan_zhuanlixinxi.patPublicNumber = _.get('patentOpen')
                            zhishichanquan_zhuanlixinxi.classNumber = _.get('patentType')
                            zhishichanquan_zhuanlixinxi.patentAbstract = _.get('patentAbstract')
                            zhishichanquan_zhuanlixinxi.patentInventor = _.get('patentInventor')
                            companybean.lstZhuanLiXinXi.append(zhishichanquan_zhuanlixinxi)
                            zhishichanquan_zhuanlixinxi = companybean.ZhuanLiXinXiBean()
                    return companybean.getDictWithoutNone()
                else:
                    return {}
            except AssertionError:
                return {'error': ['知识产权-专利信息;message:'+resp.get('message')]}
            except requests.exceptions.ConnectTimeout:
                return {'error': ['知识产权-专利信息:连接超时']}
            except ConnectionError:
                return {'error': ['知识产权-专利信息:连接异常']}

    #收费API-知识产权-软件著作权
    @staticmethod
    def parse_ZSCQ_RuanJianZhuZuoQuan(companyName=None):
        if companyName:
            try:
                resp = requests.get('http://121.9.245.186:9030/api/softwareCopyrightList?companyKey={}&isBuffer=7776000'
                                    .format(companyName), timeout=5).text
                resp = json.loads(resp)
                assert resp.get('message') == 'request success'
                companybean = CompanyBean()
                if resp.get('data'):
                    if resp.get('data').get('result'):
                        """软件著作权"""
                        zhishichanquan_ruanjianzhuzuoquan = companybean.RuanJianZhuZuoQuanBean()
                        resp_ruan_jian_zhu_zuo_quan = resp.get('data').get('result')
                        for _ in resp_ruan_jian_zhu_zuo_quan:
                            zhishichanquan_ruanjianzhuzuoquan.regDate = _.get('successDate')
                            zhishichanquan_ruanjianzhuzuoquan.softName = _.get('softName')
                            zhishichanquan_ruanjianzhuzuoquan.simpleName = _.get('shortName')
                            zhishichanquan_ruanjianzhuzuoquan.regNumber = _.get('regId')
                            zhishichanquan_ruanjianzhuzuoquan.version = _.get('version')
                            zhishichanquan_ruanjianzhuzuoquan.pubDate = '未知' if _.get('firstDate') == '1900-01-01' else _.get('firstDate')
                            companybean.lstRuanJianZhuZuoQuan.append(zhishichanquan_ruanjianzhuzuoquan)
                            zhishichanquan_ruanjianzhuzuoquan = companybean.RuanJianZhuZuoQuanBean()
                    return companybean.getDictWithoutNone()
                else:
                    return {}
            except AssertionError:
                return {'error': ['知识产权-软件著作权;message:'+resp.get('message')]}
            except requests.exceptions.ConnectTimeout:
                return {'error': ['知识产权-软件著作权:连接超时']}
            except ConnectionError:
                return {'error': ['知识产权-软件著作权:连接异常']}


    @staticmethod
    #列表页
    def next_list(html=None):
        if html:
            companybean = CompanyBean()
            data_list = []
            soup = BeautifulSoup(html, 'lxml')
            for _ in soup.find('table', class_='m_srchList').find_all('tr'):
                if _.find('a', class_='text-primary'):
                    name = _.find('a', class_="ma_h1").text
                    farendaibiao = _.find('a', class_='text-primary').text
                    try:
                        cid = urllib.parse.quote(_.find('a', class_="ma_h1").attrs['href'])
                        cid = cid.split('_')[1].split(".")[0]
                        cid = companybean.IDEncodeDecode(cid)
                    except KeyError:
                        cid = None
                    content_list = [_.text.replace('\n', '').replace(' ', '') for _ in _.find_all('span', class_='m-l')]
                    if re.search('注册资本：(.*?) ', ' '.join(content_list)):
                        zhuceziben = re.search('注册资本：(.*?) ', ' '.join(content_list)).group(1)
                    if re.search('股本：(.*?) ', ' '.join(content_list)):
                        zhuceziben = re.search('股本：(.*?) ', ' '.join(content_list)).group()
                    chenglishijian = re.search('成立时间：(.*?) ', ' '.join(content_list)).group(1)
                    dianhua = re.search('电话：(.*)', ' '.join(content_list)).group(1)
                    youxiang = re.search('邮箱：\s*(.*?)\s', _.text.replace(' ', '').replace('\n', ' ')).group(1)
                    dizhi = re.search('地址：(.*?)\s', _.text.replace(' ', '').replace('\n', ' ')).group(1)
                    logo = _.find('img').attrs['src']
                    cunxuzhuangtai = _.find('span', class_='nstatus text-success-lt m-l-xs').text \
                        if _.find('span', class_='nstatus text-success-lt m-l-xs') else None
                    content_dict = {'name': name, 'farendaibiao': farendaibiao, 'cid': cid, 'zhuceziben': zhuceziben,
                                    'chenglishijian': chenglishijian, 'dianhua': dianhua, 'youxiang': youxiang,
                                    'dizhi': dizhi, 'cunxuzhuangtai': cunxuzhuangtai, 'logo': logo}
                    if content_dict.get('cid'):
                        data_list.append(content_dict)
                else:
                    continue
            return data_list
