""""
作者：blithe
时间：23.10.13
作用：取出列表内的偶数
"""
# 定义一个列表，内容是:。[1,2,3,4,5,6,7,8,9,10]
# 遍历列表，取出列表内的偶数，并存入一个新的列表对象中
# 使用while循环和for循环各操作一次
list = [1,2,3,4,5,6,7,8,9,10]
new_list = []

def list_while(list,new):
    i = 0
    while len(list) > i:
        if list[i] % 2 == 0:
            new.append(list[i])
        i += 1
    return print(new)

def list_for(list,new):
    for i in list:
        if i % 2 == 0:
            new.append(i)
    return print(new)
# list_while(list,new_list)
list_for(list,new_list)
