""""
作者：blithe
时间：23.10.17
作用：柱状图
"""

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar = Bar()
bar.add_xaxis([1,2,3])
bar.add_yaxis("GDP",[999,222,1555],label_opts=LabelOpts(
    position='top'
))
bar.render()