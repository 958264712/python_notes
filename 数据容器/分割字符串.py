""""
作者：blithe
时间：23.10.13
作用：分割字符串练习
"""
# 给定一个字符串:itheima itcast boxuegu
# 统计字符串内有多少个"it"字符
# 将字符串内的空格，全部替换为字符"|"
# 并按照”|"进行字符串分割，得到列表

str = "itheima itcast boxuegu"
it_str = str.count("it")
res = str.replace(" ","|")
new_list = res.split("|")
print(it_str,res,new_list)