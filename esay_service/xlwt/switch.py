import xlrd
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['xlrd']
col = db['qichacha']
# for task in range(1,12):
#     path = r'C:\Users\yun\Desktop\Downloads\{}.xls'.format(task)
#     workbook = xlrd.open_workbook(path)
#     Data_sheet = workbook.sheets()[0]
#     rowNum = Data_sheet.nrows  # sheet行数
#     colNum = Data_sheet.ncols  # sheet列数
#     for row in range(1, rowNum):
#         if Data_sheet.row_values(row)[0] is '':
#             QiYeMingCheng = None
#         else:
#             QiYeMingCheng = Data_sheet.row_values(row)[0]
#         if Data_sheet.row_values(row)[1] is '':
#             ShengFen = None
#         else:
#             ShengFen = Data_sheet.row_values(row)[1]
#         if Data_sheet.row_values(row)[2] is '':
#             ChengShi = None
#         else:
#             ChengShi = Data_sheet.row_values(row)[2]
#         if Data_sheet.row_values(row)[3] is '':
#             TongYiSheHuiXinYongDaiMa = None
#         else:
#             TongYiSheHuiXinYongDaiMa = Data_sheet.row_values(row)[3]
#         if Data_sheet.row_values(row)[4] is '':
#             FaDingDaiBiaoRen = None
#         else:
#             FaDingDaiBiaoRen = Data_sheet.row_values(row)[4]
#         if Data_sheet.row_values(row)[5] is '':
#             QiYeLeiXing = None
#         else:
#             QiYeLeiXing = Data_sheet.row_values(row)[5]
#         if Data_sheet.row_values(row)[6] is '':
#             ChengLiRiQi = None
#         else:
#             ChengLiRiQi = Data_sheet.row_values(row)[6]
#         if Data_sheet.row_values(row)[7] is '':
#             ZhuCeZiBen = None
#         else:
#             ZhuCeZiBen = Data_sheet.row_values(row)[7]
#         if Data_sheet.row_values(row)[8] is '':
#             DiZhi = None
#         else:
#             DiZhi = Data_sheet.row_values(row)[8]
#         if Data_sheet.row_values(row)[9] is '':
#             YouXiang = None
#         else:
#             YouXiang = Data_sheet.row_values(row)[9]
#         if Data_sheet.row_values(row)[10] is '':
#             JingYingFanWei = None
#         else:
#             JingYingFanWei = Data_sheet.row_values(row)[10]
#         if Data_sheet.row_values(row)[11] is '':
#             WangZhi = None
#         else:
#             WangZhi = Data_sheet.row_values(row)[11]
#         if Data_sheet.row_values(row)[12] is '':
#             DianHuaHaoMa = None
#         else:
#             DianHuaHaoMa = Data_sheet.row_values(row)[12]
#         if Data_sheet.row_values(row)[13] is '':
#             GengDuoHaoMa = None
#         else:
#             GengDuoHaoMa = Data_sheet.row_values(row)[13]
#         col.insert({'QiYeMingCheng': QiYeMingCheng, 'ShengFen': ShengFen, 'ChengShi': ChengShi,
#                     'TongYiSheHuiXinYongDaiMa': TongYiSheHuiXinYongDaiMa, 'FaDingDaiBiaoRen': FaDingDaiBiaoRen,
#                     'QiYeLeiXing': QiYeLeiXing, 'ChengLiRiQi': ChengLiRiQi, 'ZhuCeZiBen': ZhuCeZiBen, 'DiZhi': DiZhi,
#                     'YouXiang': YouXiang, 'JingYingFanWei': JingYingFanWei, 'WangZhi': WangZhi,
#                     'DianHuaHaoMa': DianHuaHaoMa, 'GengDuoHaoMa': GengDuoHaoMa})

col.ensure_index()