""""
作者：blithe
时间：23.10.17
作用：全国疫情地图
"""

import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts,TitleOpts

map = Map()

f_map = open('F:/PythonLearn/综合案例/疫情.txt','r',encoding='UTF-8')
map_data = f_map.read()
data_dict = json.loads(map_data)
children = data_dict["areaTree"][0]["children"]
data = []
def  handle_data(children):
    name = ''
    if children["name"] == '新疆':
        name = '新疆维吾尔自治区'
    elif  children["name"] == '西藏':
        name = '西藏自治区'
    elif  children["name"] == '内蒙古':
        name = '内蒙古自治区'
    elif  children["name"] == '宁夏':
        name = '宁夏回族自治区'
    elif  children["name"] == '广西':
        name = '广西壮族自治区'
    elif children["name"] == '北京':
        name = '北京市'
    elif children["name"] == '天津':
        name = '天津市'
    elif children["name"] == '上海':
        name = '上海市'
    elif children["name"] == '重庆':
        name = '重庆市'
    elif children["name"] == '香港':
        name = '香港特别行政区'
    elif children["name"] == '澳门':
        name = '澳门特别行政区'
    else:
        name = children["name"] + '省'
    return name,children["total"]["confirm"]

for i in children:
    name,confirm = handle_data(i)
    data.append((name,confirm))

map.add("全国各省疫情分布图",data)
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF66"},
            {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#CC3333"},
            {"min": 10000, "label": "100000以上", "color": "#990033"},
        ]
    )
)

map.render('全国疫情地图.html')
f_map.close()
