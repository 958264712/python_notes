""""
作者：blithe
时间：23.10.13
作用：集合set
"""
# 不支持元素重复，没有规律,不支持下标索引访问
sets1={1,2,3,3,2,2,5,4,1,3,5,6,2,1}
sets = set()
print(type(sets),type(sets1),sets1)

# 添加
sets.add(1)
print(sets)
# 移除
sets1.remove(2)
print(sets1)
# 随机取出一个元素
sets2 = sets1.pop()
print(sets1)
print(sets2)
# 清空
# sets.clear()
# print(sets)
# 取出2个集合的差集
# 语法: 集合1.difference(集合2)，功能: 取出集合1和集合2的差集 (集合1有而集合2没有的)
# set3 = sets1.difference(sets)
# print(set3)
# 消除2个集合的差集
set4 = sets1.difference_update(sets)
print(sets1)
print(sets)
# 2个集合合并
set5 = sets1.union(sets)
print(set5)
print(len(set5))
# 集合的遍历
# 集合不支持下标索引，不能使用while循环
for i in set5:
    print(i)