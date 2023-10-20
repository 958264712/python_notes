""""
作者：blithe
时间：23.10.12
作用：函数的初体验
"""

# 函数的定义
# def 函数名(传入参数):
#    函数体
#    return 返回值

name = "blithe"
name1 = "blitheasdas"
name2= "blasfdfasithe"
# length = len(name)
# print(length)

def lengths(num):
    count = 0
    for i in num:
        count += 1
    print(f"字符串{num}的长度是{count}")

# lengths(name)
# lengths(name1)
# lengths(name2)
