""""
作者：blithe
时间：23.10.16
作用：异常的操作
"""
# 1.什么是异常:
# 异常就是程序运行的过程中出现了错误
# 2.bug是什么意思
# bug就是指异常的意思，因为历史因为小虫子导致计算机失灵的案例，所以延续至今，bug就代表软件出现错误。

# 捕获常规异常基本语法：
# try: 可能发生错误的代码
# except：如果出现异常执行的代码
# try:
#     f = open('F:/PythonLearn/异常/abc.txt','r',encoding='UTF-8')
# except:
#     print("出现异常了，因为文件不存在，我将open的模式，改为w模式去打开")
#     f = open("F:/PythonLearn/异常/abc.txt","w", encoding = "UTF-8")

# 捕获指定的异常
# try:
#     print(name)
# # 1 /0
# except NameError as e:
#     print(e)

# 捕获多个异常
# try:
#     1 / 0
#     print(name)
# except (NameError,ZeroDivisionError) as e:
#     print(e)

# 捕获到所有异常
# try:
#     # 1/0
#     # print(name)
#     f=open('D:/123.txt','r')
# except Exception as e:
#     print(e)

# 异常的finally
try:
    f = open('F:/PythonLearn/异常/123.txt','r',encoding='UTF-8')
except Exception as e:
    print(e)
    f = open("F:/PythonLearn/异常/123.txt","w", encoding = "UTF-8")
else:
    print('No Error')
finally:
    print('my name is finally')
    f.close()

