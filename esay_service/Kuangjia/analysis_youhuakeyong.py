# 收费API-企业年报-基本信息
@staticmethod  # todo
def parse_QYNB_JiBenXinXI(companyName=None):
    if companyName:
        try:
            resp = requests.get('http://121.9.245.186:9030/api/companyNBDetail?companyKey={}&isBuffer=7776000'
                                .format(companyName), timeout=5).text
            resp = json.loads(resp)
            assert resp.get('message') == 'request success'
            companybean = CompanyBean()
            if resp.get('data'):
                if resp.get('data').get('result'):
                    resp = resp.get('data').get('result').get('nbInfo')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.regNumber = resp.get('regNumber')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.companyName = resp.get('companyName')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.busStatus = resp.get('runStatus')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.phonenumber = resp.get('phone')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.isChange = '是' if resp.get('shareTransfer') == '0' else '否'
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.isInvest = '是' if resp.get('otherShare') == '0' else '否'
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.email = resp.get('mail')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.location = resp.get('address')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.allPeople = resp.get('members')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.postcode = resp.get('postCode')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.yearNumber = resp.get('year')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.webSite = '是' if resp.get('webSite') == '0' else '否'
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.totalAssets = resp.get('totalAssets')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.toalProfit = resp.get('toalProfit')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.totalEquity = resp.get('totalEquity')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.totalIncome = resp.get('totalIncome')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.mainIncome = resp.get('mainIncome')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.netProfit = resp.get('netProfit')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.totalTax = resp.get('totalTax')
                    companybean.qi_ye_nian_bao_ji_ben_xin_xi.totalDebt = resp.get('totalDebt')
                    return companybean.getDictWithoutNone()
                else:
                    return {'qi_ye_nian_bao_ji_ben_xin_xi': 'null'}
            else:
                return {'qi_ye_nian_bao_ji_ben_xin_xi': 'null'}
        except AssertionError:
            return {'error': ['企业年报-基本信息;message:' + resp.get('message')]}
        except requests.exceptions.ConnectTimeout:
            return {'error': ['企业年报-基本信息:连接超时']}
        except ConnectionError:
            return {'error': ['企业年报-基本信息:连接异常']}


# 收费API-企业年报-股东发起人出资信息
@staticmethod  # todo
def parse_QYNB_GuDongFaQiRen(companyName=None):
    if companyName:
        try:
            resp = requests.get('http://121.9.245.186:9030/api/companyNBDetail?companyKey={}&isBuffer=7776000'
                                .format(companyName), timeout=5).text
            resp = json.loads(resp)
            assert resp.get('message') == 'request success'
            companybean = CompanyBean()
            qiyenianbao_gudongchuzixinxi = companybean.QiYeNianBao_GuDongFaQiRenBean()
            if resp.get('data'):
                if resp.get('data').get('result'):
                    resp = resp.get('data').get('result').get('gdCzInfoList')
                    for _ in resp:
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
                    return companybean.getDictWithoutNone()
                else:
                    return {'lstQiYeNianBao_GuDongFaQiRen': 'null'}
            else:
                return {'lstQiYeNianBao_GuDongFaQiRen': 'null'}
        except AssertionError:
            return {'error': ['企业年报-网站信息;message:' + resp.get('message')]}
        except requests.exceptions.ConnectTimeout:
            return {'error': ['企业年报-网站信息:连接超时']}
        except ConnectionError:
            return {'error': ['企业年报-网站信息:连接异常']}


# 收费API-企业年报-网站信息
@staticmethod  # todo
def parse_QYNB_WangZhanXinXi(companyName=None):
    if companyName:
        try:
            resp = requests.get('http://121.9.245.186:9030/api/companyNBDetail?companyKey={}&isBuffer=7776000'
                                .format(companyName), timeout=5).text
            resp = json.loads(resp)
            assert resp.get('message') == 'request success'
            companybean = CompanyBean()
            qiyenianbao_wangzhan = companybean.QiYeNianBao_WangZhanBean()
            if resp.get('data'):
                if resp.get('data').get('result'):
                    resp = resp.get('data').get('result').get('wwInfoList')
                    for _ in resp:
                        qiyenianbao_wangzhan.shopName = _.get('name')
                        qiyenianbao_wangzhan.shopType = _.get('type')
                        qiyenianbao_wangzhan.shopUrl = _.get('webSite')
                        qiyenianbao_wangzhan.yearNumber = _.get('year')
                        companybean.lstQiYeNianBao_WangZhan.append(qiyenianbao_wangzhan)
                        qiyenianbao_wangzhan = companybean.QiYeNianBao_WangZhanBean()
                    return companybean.getDictWithoutNone()
                else:
                    return {'lstQiYeNianBao_WangZhan': 'null'}
            else:
                return {'lstQiYeNianBao_WangZhan': 'null'}
        except AssertionError:
            return {'error': ['企业年报-网站信息;message:' + resp.get('message')]}
        except requests.exceptions.ConnectTimeout:
            return {'error': ['企业年报-网站信息:连接超时']}
        except ConnectionError:
            return {'error': ['企业年报-网站信息:连接异常']}