""""
作者：blithe
时间：23.10.17
作用：地图
"""

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ("北京",99),
    ("上海",199),
    ("江西",299),
    ("台湾",399),
    ("广东",499)
]

map.add("测试地图",data,"china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
            {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
            {"min":100,"max":499,"label":"100-499","color":"#990033"},
            {"min":500,"max":999,"label":"500-999","color":"#668866"},
            {"min":1000,"max":9999,"label":"1000-9999","color":"#338822"},
            {"min":10000,"label":"10000以上","color":"#555555"},
        ]
                                 )
)

map.render()