""""
作者：blithe
时间：23.10.16
作用：python的自定义模块
"""
# 演示自定义模块
#导入自定义模块使用
# import my_module1

# 导入不同文件但同名功能
# from my_module1 import  compute
# from my_module2 import  compute
#
# num = compute(1,99)

# print(num)

# __main__变量
from my_module1 import  compute
# '__main__'

# __all__变量
from my_module1 import  *
compute(1,2)
# compute2(1,2)
# NameError: name 'compute2' is not defined. Did you mean: 'compute'?