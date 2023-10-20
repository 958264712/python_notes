""""
作者：blithe
时间：23.10.16
作用：python的自定义包
"""
# 快速入门
# 步骤如下:
# 新建包my_package
# 新建包内模块: my_modulel 和 mymodule2.

#导入自定义的包中的模块，并使用
import my_Package.my_module1 as m1
import my_Package.my_module2 as m2

m1.compute(1,2)
m2.compute(1,2)

# from my_Package import *
# my_module1.compute(1,2)

#通过__aLL__变量，控制import *
