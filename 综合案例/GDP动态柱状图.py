""""
作者：blithe
时间：23.10.18
作用：GDP动态时间线柱状图
"""
# 列表的sort方法
# 列表.sort(key=函数,reverse=True/False)
my_list = [["a",33],["b",22],["c",55]]

def sort_list(item):
    return item[1]
# 具名
# my_list.sort(key=sort_list,reverse=True)
# 匿名
my_list.sort(key=lambda item:item[1],reverse=False)

import json
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

f = open('F:/PythonLearn/综合案例/1960-2019全球GDP数据.csv','r',encoding='GB2312')
data = f.readlines()
f.close()
data.pop(0)

data_dict = {}
for i in data:
    year = int(i.split(',')[0])    #年份
    country = i.split(',')[1]      #国家
    gdp = float(i.split(',')[2])   #GDP数据
    # 判断有没有key
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])


# 添加时间线
timeline = Timeline({"theme":ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())

for y in sorted_year_list:
    data_dict[y].sort(key=lambda item:item[1],reverse=True)
    # 取出本年份前8的国家
    year_data = data_dict[y][0:8]
    x_data = []
    y_data = []
    for c in year_data:
        x_data.append(c[0])    #x轴添加国家
        y_data.append(c[1] / 100000000)     #y轴添加GDP
    x_data.reverse()
    y_data.reverse()
    #  构建柱状图
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(亿)',y_data,label_opts=LabelOpts(position='right'))
    # 反转
    bar.reversal_axis()
    timeline.add(bar,str(y))
    bar.set_global_opts(
        title_opts=TitleOpts(
            title=f'{y}年全球前八GDP数据'
        )
    )

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)


timeline.render('1960-2019年全球GDP前8排行.html')