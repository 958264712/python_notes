""""
作者：blithe
时间：23.10.18
作用：构造方法
"""
# __init__()方法为构造方法 如果传参即会自动传递给__init__方法使用

class Student:
    name = None
    age = None
    tel = None

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("student类创建一个类对象")

stu = Student("周小论",33,"15166668888")
print(stu.name)
print(stu.age)
print(stu.tel)