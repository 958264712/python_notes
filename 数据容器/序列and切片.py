""""
作者：blithe
时间：23.10.13
作用：什么是序列，序列的切片操作
"""
# 序列是指:内容连续、有序，可使用下标索引的一类数据容器
# 列表、元组、字符串，均可以可以视为序列
# 语法: 序列[起始下标:结束下标:步长]
# 序列支持切片，即: 列表、元组、字符串，均支持进行切片操作
# 切片: 从一个序列中，取出一个子序列
"""
起始可以省略，省略从头开始
结束可以省略，省略到尾结束
步长可以省略，省略步长为1 (可以为负数，表示倒序执行)
"""

#对list进行切片，从1开始，4结束，步长1
my_list = [0,1,2,3,4,5,6]
step = my_list[1:4] #步长默认是1，所以可以省略不写
print(step)
#tuple进行切片，从头开始，到最后结束，步长1
my_tuple = (0,1,2,3,4,5,6)
step1 = my_tuple[:] #起始和结束不写表示从头到尾，步长为1可以省略
print(step1)
#对str进行切片，从头开始，到最后结束，步长2
my_str = '01234567'
step2 = my_str[::2]
print(step2)
#str进行切片，从头开始，到最后结束，步长-1
step3 = my_str[::-1] #等同于将序列反转了
print(step3)
#对列表进行切片，从3开始，到1结束，步长-1
step4 = my_list[3:1:-1]
print(step4)
#对元组进行切片，从头开始，到尾结束，步长-2
step5 = my_tuple[::-2]
print(step5)