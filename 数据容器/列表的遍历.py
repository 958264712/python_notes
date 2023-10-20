""""
作者：blithe
时间：23.10.13
作用：列表的遍历
"""

"""
1.什么是遍历?
将容器内的元素依次取出，并处理，称之为遍历操作
2.如何遍历列表的元素?
可以使用while或for循环
3.for循环的语法
for 临时变量 in 数据容器对临时变量进行处理
4.for循环和while对比
for循环更简单，while更灵活
for用于从容器内依次取出元素并处理，while用以任何需要循环的场景
"""
# while循环
list = [0,1,2,3,4,5,6,7,8,9]
def list_while_func(list):
    i = 0
    while len(list) > i:
        print(list[i])
        i += 1
# for循环
def list_for_func(list):
    for i in list:
        print(i)
list_for_func(list)
# list_while_func(list)