""""
作者：blithe
时间：23.10.17
作用：时间线柱状图
"""

from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar = Bar()
bar.add_xaxis(['cn','us','uc'])
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
bar.reversal_axis()

bar1 = Bar()
bar1.add_xaxis(['cn','us','uc'])
bar1.add_yaxis("GDP",[50,30,20],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

# 创建时间线
timeline = Timeline(
    {"theme":ThemeType.LIGHT}
)

timeline.add(bar,'2021year GDP')
timeline.add(bar1,'2022year GDP')
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_loop_play=True,
    is_auto_play=True
)
timeline.render()