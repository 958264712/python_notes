""""
作者：blithe
时间：23.10.17
作用：折线图
"""
import json
from pyecharts.charts import Line
from pyecharts.options import LabelOpts,TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

# 处理数据
f_us = open('F:/PythonLearn/综合案例/美国.txt','r',encoding='UTF-8')
us_data = f_us.read()
f_jp = open('F:/PythonLearn/综合案例/日本.txt','r',encoding='UTF-8')
jp_data = f_jp.read()
f_in = open('F:/PythonLearn/综合案例/印度.txt','r',encoding='UTF-8')
in_data = f_in.read()

def new_data(data):
    new_data = data.split('(')
    data1 = new_data[1].split(');')
    return json.loads(data1[0])['data'][0]['trend']['updateDate'][:314],json.loads(data1[0])['data'][0]['trend']['list'][0]['data'][:314]

# 处理数据
us_x_data,us_y_data = new_data(us_data)
jp_x_data,jp_y_data = new_data(jp_data)
in_x_data,in_y_data = new_data(in_data)

line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis('美国确诊人数',us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('日本确诊人数',jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('印度确诊人数',in_y_data,label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="2020三国确诊人数对比图",pos_left='center',pos_bottom='1%'),
    legend_opts=(LegendOpts(is_show=True)),
    toolbox_opts=(ToolboxOpts(is_show=True)),
    # visualmap_opts=(VisualMapOpts(is_show=True))
)
line.render()

f_in.close()
f_jp.close()
f_us.close()