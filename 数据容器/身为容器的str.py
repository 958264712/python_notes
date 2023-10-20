""""
作者：blithe
时间：23.10.13
作用：再识str
"""
"""
作为数据容器，字符串有如下特点:
1.只可以存储字符串
2.长度任意取决于内存大小
3.支持下标索引
4.允许重复字符串存在
5.不可以修改(增加或删除元素等)
6.支持for循环
"""
# 字符串为无法修改的容器
my_str = "my name is blithe"

# my_str[1] ='e'
# TypeError: 'str' object does not support item assignment

#通过下标索引取值
value = my_str[2]
value1 = my_str[-2]
print(value,value1)
#index方法
ind = my_str.index('i')
print(ind)
# repLace方法
res = my_str.replace(' ','\n')
print(res)
# split方法
list_str = my_str.split(' ')
print(list_str)
# strip方法 去前后空格 类似js trim
my_str = "  my name is blithe  "
print(my_str)
print(my_str.strip())
print(my_str.lstrip())
print(my_str.rstrip())
#统计字符串中某字符串的出现次数
print(my_str.count(' '))
#统计字符串的长度
print(len(my_str))