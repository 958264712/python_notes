""""
作者：blithe
时间：23.10.16
作用：文件的相关操作
"""
# 操作主要包括：打开，读写，关闭
# open()打开函数 open(name,mode,encoding)
# name:是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
# mode:设置打开文件的模式(访问模式): 只读(r)、写入(w)、追加(a)等
# encoding:编码格式(推荐使用UTF-8)
# 打开文件
# f = open('F:/PythonLearn/文件操作/test.txt','r',encoding='UTF-8')
# print(type(f))
# <class '_io.TextIOWrapper'>

# read()读取函数 文件对象.read(num) 有num读取num字节的结果，没有num读取全部内容
# print(f.read(10))
# print(f.read())

# readlines()读取文件的全部行，封装到列表中，会被read函数影响
# lines = f.readlines()
# print(type(lines))
# print(lines)

# readline()读取文件的一行，调用一次读取一行
# line = f.readline()
# line1 = f.readline()
# print(line)
# print(line1)

# for循环读取文件行
# for i in f:
#     print(i)

# close()关闭文件函数
# f.close()

# with open语法操作文件,会自动close
# with open('F:/PythonLearn/文件操作/test.txt','r',encoding='UTF-8') as f:
#     for i in f:
#         print(i)

# write()写入函数
# flush()内容刷新，当调用flush的时候，内容会真正写入文件
# f = open('F:/PythonLearn/文件操作/noLive.txt','w',encoding='UTF-8')
# f.write("hello world")
# f.flush()
# f.close()
# f.write("当文件存在时，会将原本内容清空！！！")
# f.flush()
# f.close()

# 追加写入 a
f = open('F:/PythonLearn/文件操作/noLive.txt','a',encoding='UTF-8')
# f.write("hello world")
# f.flush()
# f.close()
f.write("\na模式进行追加，不会清空原本内容！！")
f.flush()
f.close()