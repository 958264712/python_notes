""""
作者：blithe
时间：23.10.18
作用：其他内置方法
"""
# 魔术方法
# __init__ 构造方法
# __str__ 字符串方法
# __lt__ 小于、大于符号比较方法
# __le__ 小于等于、大于等于符号比较方法
# __eq__ ==符号比较方法

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"学生名字是{self.name},年龄是{self.age}"
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age
    def __eq__(self, other):
        return  self.age == other.age
stu = Student("周小论",33)
stu1 = Student("周大论",35)
print(stu >= stu1)
