""""
作者：blithe
时间：23.10.16
作用：自定义工具包练习
"""
# 1、创建一个自定义包，名称为: my_utils (我的工具)
# 2、str_util.py (字符串相关工具，内含:)
# 函数:str_reverse(s)，接受传入字符串，将字符串反转返回
# 函数:substr(s,x,y)，按照下标x和y，对字符串进行切片
# 3、file_util.py (文件处理相关工具，内含:)
# 函数: print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，
# 如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
# 函数: append_to_file(file_name, data)，接收文件路径以及传入数据，将数据追加写入到文件中

from my_utils.str_util import *
from my_utils.file_util import *
print(str_reverse("黑马程序员"))
print(substr("itheima",0,4))
print_file_info('F:/PythonLearn/文件操作/123.txt')
append_to_file('F:/PythonLearn/文件操作/123.txt','1231231')