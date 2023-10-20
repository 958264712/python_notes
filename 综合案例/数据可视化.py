""""
作者：blithe
时间：23.10.16
作用：折线图，json格式
"""
# json有什么用
# 各种编程语言存储数据的容器不尽相同,在Python中有字典dict这样的数据类型，而其它语言可能没有对应的字典
# import json
#准备列表，列表内每一个元素都是字典，将其转换为JSON
# data = [{"name":"张大山","age": 11},{"name":"王大锤","age": 13},{"name":"赵小虎","age": 16}]
# json_str = json.dumps(data)
# print(type(json_str))
# print(json_str)
#准备字典，将字典转换为JSON
# dic = '{"name":"张大山","age": 11}'
# python_str = json.loads(dic)
# print(type(python_str))
# print(python_str)
# JSON宇符申转换为Python数据类型[{k: v，k: v，{k: v，k: v}]
#将JSON字符申转换为Python数据类型{k: v，k: v}


# pyechats入门
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
#得到折线图对象
line = Line()
# #添加X轴数据l
line.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
line.add_yaxis("GDP",[30,20 ,10])# 生成图表
# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left='center',pos_bottom='1%'),
    legend_opts=(LegendOpts(is_show=True)),
    toolbox_opts=(ToolboxOpts(is_show=True)),
    visualmap_opts=(VisualMapOpts(is_show=True))
)
line.render()