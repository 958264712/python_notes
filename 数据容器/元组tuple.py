""""
作者：blithe
时间：23.10.13
作用：元组tuple
"""
# 不能被修改的列表
# 3.元组的注意事项
# 不可修改内容(可以修改内部list的内部元素)
# 4.元组的特点
# 和list基本相同(有序、任意数量元素、允许重复元素)，唯一不同在于不可修改
# 支持for循环
tuple1 = (1,"hello",True)
tuple2 = ()
tuple3 = tuple()
print(tuple1)
print(tuple2)
print(tuple3)
# 定义单个元素的元组
tuple4 = ("hello")
tuple5 = ("hello",)
print(type(tuple4))
print(type(tuple5))
# <class 'str'>
# <class 'tuple'>

# 元组的嵌套
tuple6 = (3,(1,2),3,(4,5,6),2,3)
print(type(tuple6),tuple6)

# 下标索引去取出内容
num = tuple6[3][2]
print(num)

# index查找方法
ind = tuple6.index((1,2))
print(ind)
# count统计方法
count = tuple6.count(3)
print(count)
# len函数
length = len(tuple6)
print(length)

# 元组的遍历while
i = 0
while length > i:
    print(tuple6[i])
    i += 1
# 元组的遍历for
for i in tuple6:
    print(i)

# 修改元组的内容
# tuple6[0] = 1

# 定义一个元组
t9 = (1,2,["a","b"])
print(t9)
t9[2][1] = "bbb"
print(t9)
