""""
作者：blithe
时间：23.10.16
作用：python的模块
"""
# 模块就是一个Python文件，里面有类、函数、变量等，我们可以拿过来用(导入模块去使用)
# 模块的导入方式 [from 模块名] import [模块  类变函数] [as 别名]
"""
常用的组合形式如:
import模块名
from 模块名 import 类、变量,方法等
from 模块名import*
import 模块名as 别名
from 模块名 import 功能名as 别名
"""

# 使用import导入time模块使用sLeep功能(函数)
# import time #入Python内置的time模块 (time.py这个代码文件)
# print("hello")
# time.sleep(5)#通过.就可以使用模块内部的全部功能(类、函数
# print("hello")

#使用from导入time的sLeep功能 (函数)
# from time import sleep
# print("hello")
# sleep(5)
# print("hello")

#使用*入time模块的全部功能
# from time import *
# print("hello")
# sleep(5)
# print("hello")

#使用as给特定功能加上别名
# import time as t
# print("hello")
# t.sleep(5)
# print("hello")

from time import sleep as s
print("hello")
s(5)
print("hello")