""""
作者：blithe
时间：23.10.12
作用：函数的返回值定义语法
"""

def sum(x,y):
    return x + y

num = sum(22,33)
# print(num)

def say_hi():
    print("hello")

result = say_hi()
print({type(result)})
print(result)