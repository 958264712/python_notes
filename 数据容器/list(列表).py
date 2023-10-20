""""
作者：blithe
时间：23.10.13
作用：数据容器入门，list列表
"""
 # 1.什么是数据容器?
# 一种可以存储多个元素的Python数据类型
# 2.Python有哪些数据容器?
# list(列表)、tuple(元组)、str(字符串)、set(集合)、dict(字典)
# 它们各有特点，但都满足可容纳多个元素的特性

list = [1,2,3,'4,5',66,'1',7.7,True,['a',',b']]
print(list)
print(type(list))
# for i in list:
#     print(i)

# 下标索引
print(list[8][0])
print(list[-8])

# list的方法
# 1.查询功能：查找指定元素在列表的下标，如果找不到，报错ValueError
res = list.index(1)
print(res)
# 2.修改特定位置(索引)的元素值:
# 语法:列表[下标]=值
list[0] = 999
print(list)
# 3.插入元素：列表.insert(下标,元素)，在指定的下标位置，插入指定的元素
list.insert(5,66666)
list.insert(-1,-1)
print(list)
# 4.追加元素：列表.append(元素)，将指定元素，追加到列表的尾部
list.append('666')
print(list)
# 5.列表.extend(其它数据容器),将其它数据容器的内容取出，依次追加到列表尾部,类似js中concat合并
list.extend([0,9,8,7])
print(list)
# 6.删除指定下标元素
# 6.1 del 列表[下标]
del list[0]
print(list)
# 6.1 列表.pop(下标)
list.pop(-1)
list.pop(6)
print(list)
# 7.删除某元素在列表中的第一个匹配项
list.append(3)
list.insert(4,3)
list.insert(7,3)
print(list)
list.remove(3)
print(list)
# 8.清空列表内容，语法: 列表.clear()
# list.clear()
# print(list)
# 9.统计列表内某个元素的数量
count = list.count(3)
print(count)
# 10.统计列表内全部的元素数量
length =len( list)
print(length)

"""
[1, 2, 3, '4,5', 66, '1', 7.7, True, ['a', ',b']]
<class 'list'>
a
2
0
[999, 2, 3, '4,5', 66, '1', 7.7, True, ['a', ',b']]
[999, 2, 3, '4,5', 66, 66666, '1', 7.7, True, -1, ['a', ',b']]
[999, 2, 3, '4,5', 66, 66666, '1', 7.7, True, -1, ['a', ',b'], '666']
[999, 2, 3, '4,5', 66, 66666, '1', 7.7, True, -1, ['a', ',b'], '666', 0, 9, 8, 7]
[2, 3, '4,5', 66, 66666, '1', 7.7, True, -1, ['a', ',b'], '666', 0, 9, 8, 7]
[2, 3, '4,5', 66, 66666, '1', True, -1, ['a', ',b'], '666', 0, 9, 8]
[2, 3, '4,5', 66, 3, 66666, '1', 3, True, -1, ['a', ',b'], '666', 0, 9, 8, 3]
[2, '4,5', 66, 3, 66666, '1', 3, True, -1, ['a', ',b'], '666', 0, 9, 8, 3]
3
15
"""