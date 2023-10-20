""""
作者：blithe
时间：23.10.18
作用：初识对象
"""
# 设计一个类
class Student:
    name = None         #姓名
    gender = None        #性别
    nationality = None    #国籍
    native_place = None   #籍贯
    age = None           #年龄
# 创建一个对象
stu_1 = Student()
# 对象属性进行赋值
stu_1.name = 'blithe'
stu_1.gender = 'man'
stu_1.nationality = 'china'
stu_1.native_place = 'jiangxi'
stu_1.age = '22'
# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)

