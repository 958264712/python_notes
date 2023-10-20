""""
作者：blithe
时间：23.10.19
作用：数据分析案例1
"""
# 某公司，有2份数据文件，现需要对其进行分析处理，计算每日的销售额并以柱状图表的形式进行展示
# 1月份数据是普通文本，使用逗号分割数据记录，从前到后分别是 (日期，订单id，销售额，销售省份)
# 2月份数据是JSON数据，同样包含 (日期，订单id，销售额，销售省份)
import json
from typing import Union
from pyecharts.charts import Bar
from main1 import Record
from get_all_data import GetAllData
from pyecharts.options import *
# class Record:
#     def date(self):
#         """日期"""
#         pass
#     def order_id(self):
#         """订单id"""
#         pass
#     def money(self):
#         """销售额"""
#         pass
#     def province(self):
#         """销售省份"""
#         pass

flies = GetAllData('F:/PythonLearn/综合案例/2011年1月销售数据.txt')
flies1 = GetAllData('F:/PythonLearn/综合案例/2011年2月销售数据JSON.txt')

list1:list[Record] = flies.read_data()
list2:list[Record] = flies1.read_json_data()
all_data:list[Record] = list1 + list2
one_money_date:dict[str,int] = {}
one_date: list[str] = []
for i in all_data:
    try:
        if one_money_date[i.date]:
            one_money_date[i.date] += i.money
    except Exception as e:
        one_money_date[i.date] = i.money
        one_date.append(i.date)
y_data = []
for i in one_money_date:
     y_data.append(one_money_date[i])
bar = Bar()
bar.add_xaxis(one_date)
bar.add_yaxis("2011年1月与2月销售数据图",y_data,label_opts = LabelOpts(position='top'))
bar.render()
# class One_month(Record):
#     f = open("/综合案例/2011年1月销售数据.txt", "r", encoding="UTF-8")
#     data = f.readlines()
#     f.close()
#     one_date: list[str] = []
#     one_money_order_id = {}
#     one_order_id = []
#     one_money = []
#     one_province = []
#     for i in data:
#         list = i.split(',')
#         try:
#             if one_date.index(list[0]) > 0:
#                 continue
#         except Exception as e:
#             one_date.append(list[0])
#         try:
#             if one_money_order_id[list[0]]:
#                 one_money.append(list[2])
#                 one_order_id.append(list[1])
#         except Exception as e:
#             one_money = []
#             one_order_id = []
#             one_money.append(list[2])
#             one_order_id.append(list[1])
#             one_money_order_id[list[0]] = {
#                 "order_id":one_order_id,
#                 "money":one_money
#             }
#         try:
#             if one_province[list[3]]:
#                 continue
#         except Exception as e:
#             one_province.append(list[0])
#
#     def date(self):
#         """日期"""
#         return self.one_date
#     def order_id(self):
#         """订单id"""
#         return self.one_money_order_id
#     def money(self):
#         """销售额"""
#         return self.one_money_order_id
#     def province(self):
#         """销售省份"""
#         return self.one_province
#
# class Two_month(Record):
#     f = open("/综合案例/2011年2月销售数据JSON.txt", "r", encoding="UTF-8")
#     data = f.readlines()
#     f.close()
#     print(data)
#     one_date: list[str] = []
#     one_money_order_id = {}
#     one_order_id = []
#     one_money = []
#     one_province = []
#     for i in data:
#         list = i.split(',')
#         try:
#             if one_date.index(list[0]) > 0:
#                 continue
#         except Exception as e:
#             one_date.append(list[0])
#         try:
#             if one_money_order_id[list[0]]:
#                 one_money.append(list[2])
#                 one_order_id.append(list[1])
#         except Exception as e:
#             one_money = []
#             one_order_id = []
#             one_money.append(list[2])
#             one_order_id.append(list[1])
#             one_money_order_id[list[0]] = {
#                 "order_id":one_order_id,
#                 "money":one_money
#             }
#         try:
#             if one_province[list[3]]:
#                 continue
#         except Exception as e:
#             one_province.append(list[0])
#
#     def date(self):
#         """日期"""
#         return self.one_date
#     def order_id(self):
#         """订单id"""
#         return self.one_money_order_id
#     def money(self):
#         """销售额"""
#         return self.one_money_order_id
#     def province(self):
#         """销售省份"""
#         return self.one_province
