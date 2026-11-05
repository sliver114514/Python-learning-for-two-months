# 折线统计图
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts, VisualMapOpts

line = Line()
# x 轴的坐标
line.add_xaxis(["中国", "美国", "日本"])
# y 轴的坐标
line.add_yaxis("GDP", [30, 20, 15])

# 设置全局变量配置项set_global_opts来设置
line.set_global_opts(
    title_opts = TitleOpts(title="GDP展示", pos_left="center", pos_right="1%"),
    # 是否展示:图例，工具箱，视觉映射
    legend_opts = LegendOpts(is_show=True),
    tooltip_opts = TooltipOpts(is_show=True),
    visualmap_opts = VisualMapOpts(is_show=True),
)
# 生成
line.render()
