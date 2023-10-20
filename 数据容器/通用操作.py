""""
作者：blithe
时间：23.10.13
作用：容器的通用操作
"""
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str ="abcdefg"
my_set = {1,2,3,4,5}
my_dict = {"key1": 1,"key2": 2,"key3": 3,"key4": 4,"key5": 5}
# Len元素个数
print(f"列表 元素个数有:{len(my_list)}")
print(f"元组 元素个数有:{len(my_tuple)}")
print(f"字符串元素个数有: {len(my_str)}")
print(f"集合 元素个数有:{len(my_set)}")
print(f"字典 元素个数有:{len(my_dict)}")
# Max最大值
print(f"列表 元素最大值:{max(my_list)}")
print(f"元组 元素最大值:{max(my_tuple)}")
print(f"字符串元素最大值: {max(my_str)}")
print(f"集合 元素最大值:{max(my_set)}")
print(f"字典 元素最大值:{max(my_dict)}")
# Min最小值
print(f"列表 元素最小值:{min(my_list)}")
print(f"元组 元素最小值:{min(my_tuple)}")
print(f"字符串元素最小值: {min(my_str)}")
print(f"集合 元素最小值:{min(my_set)}")
print(f"字典 元素最小值:{min(my_dict)}")
# 类型转换：容器转列表
print(f"列表:{list(my_list)}")
print(f"元组:{list(my_tuple)}")
print(f"字符串: {list(my_str)}")
print(f"集合 :{list(my_set)}")
print(f"字典 :{list(my_dict)}")
# 类型转换：容器转元组
print(f"列表:{tuple(my_list)}")
print(f"元组:{tuple(my_tuple)}")
print(f"字符串: {tuple(my_str)}")
print(f"集合 :{tuple(my_set)}")
print(f"字典 :{tuple(my_dict)}")
# 类型转换：容器转字符串
print(f"列表:{str(my_list)}")
print(f"元组:{str(my_tuple)}")
print(f"字符串: {str(my_str)}")
print(f"集合 :{str(my_set)}")
print(f"字典 :{str(my_dict)}")
# 类型转换：容器转集合
print(f"列表:{set(my_list)}")
print(f"元组:{set(my_tuple)}")
print(f"字符串: {set(my_str)}")
print(f"集合 :{set(my_set)}")
print(f"字典 :{set(my_dict)}")
# sorted排序 sorted(容器，reverse = True)
print(f"列表:{sorted(my_list,reverse = True)}")
print(f"元组:{sorted(my_tuple,reverse = True)}")
print(f"字符串: {sorted(my_str,reverse = True)}")
print(f"集合 :{sorted(my_set,reverse = True)}")
print(f"字典 :{sorted(my_dict,reverse = True)}")

