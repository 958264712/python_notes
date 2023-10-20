""""
作者：blithe
时间：23.10.19
作用：类型注解，变量的类型注解的使用
"""
import json
from random import random

# 基础语法：变量:类型 var_1: int = 10
# 容器类型详细注解： my_list: list[int] = [1,2] my_tuple: tuple[str,int,bool] = ("1",2,False) my_set: set[int] = {1,2,3} my_dict: dict[str,int] = {"1,":2}
# 元组类型设置类型详细注解，需要将每一个元素都标记出来
# 字典类型设置类型详细注解，需要2个类型，第一个是key第二个是value

# 基础数据类型注解
var_1: int = 10
var_2: str = '10'
var_3: bool = True

# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
my_list: list = [1,2]
my_tuple: tuple = ("1",2,False)
my_set: set = {1,2,3}
my_dict: dict = {"1,":2}
# 容器类型详细注解
my_list1: list[int] = [1,2]
my_tuple1: tuple[str,int,bool] = ("1",2,False)
my_set1: set[int] = {1,2,3}
my_dict1: dict[str,int] = {"1,":2}

# 在注解中进行类型注解
# var_11 = random.randint(1,10)   #type: # int
var_12 = json.loads('{"name":"zhangsan"}') #type:dict[str,str]
def func():
    return 10
var_13 = func()  #type: int
# 类型注解的限制

# 函数（方法）的类型注解 - 形参注解
# 对形参进行类型注解
def add(x:int,y:int):
    return x + y
add(1,2)

# 对返回值进行类型注解
def func(data:list) -> list :
    return data
print(func(1))