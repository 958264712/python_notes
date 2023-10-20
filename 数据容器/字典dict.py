""""
作者：blithe
时间：23.10.13
作用：字典dict
"""
#定义字典
my_dict = {"王力鸿": 99,"周杰轮": 88,"林俊节": 77}
#定义空宇典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是: {my_dict}，类型: {type(my_dict)}")
print(f"字典2的内容是: {my_dict2}，类型:{type(my_dict2)}")
print(f"字典3的内容是: {my_dict3}，类型:{type(my_dict3)}")
#定义重复Key的字典
my_dict1 = {"王力鸿": 99,"王力鸿": 88,"林俊节": 77}
print(f"字典1的内容是: {my_dict1}")
# 从字典中基FKey获取VaLue
score = my_dict1["王力鸿"]
print(score)
#定义嵌套字典
my_dict4 = {"王力鸿": {"语文": 99,"数学": 88,"英语": 77},"周杰轮": {"语文": 99,"数学": 88,"英语": 77},"林俊节": {"语文": 99,"数学": 88,"英语": 77}}
print(my_dict4)
#从嵌套字典中获取数据
score = my_dict4["王力鸿"]["语文"]
print(score)

#新增
my_dict4["陈奕讯"] = {"语文": 99,"数学": 66,"英语": 88}
print(my_dict4)
# 更新
my_dict4["陈奕讯"]["数学"] =  77
print(my_dict4)
# 删除
my_dict4.pop("陈奕讯")
print(my_dict4)
# 清空
# my_dict4.clear()
# print(my_dict4)
# 获取全部的key
my_keys = my_dict4.keys()
print(my_keys)
# 遍历字典
for i in my_keys:
     print(i,my_dict4[i])
#统计字典内的元素数量
print(len(my_dict4))