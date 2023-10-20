""""
作者：blithe
时间：23.10.17
作用：江西疫情地图
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
data_children = []
for i in children:
    if i['name'] == '江西':
        data_children = i['children']

for i in data_children:
    data.append((i['name'] + '市',i['total']['confirm']))

map.add('江西省内疫情发布图',data,'江西')
map.set_global_opts(
    title_opts=TitleOpts(title="江西省内疫情发布图"),
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

map.render()
f_map.close()