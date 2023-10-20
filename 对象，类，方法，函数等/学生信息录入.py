""""
作者：blithe
时间：23.10.18
作用：学生信息录入练习
"""
# 开学了有一批学生信息需要录入系统，请设计一个类，记录学生的姓名、年龄、地址，这3类信息

class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

for i in range(0,2):
    print(f"当前录入第{i + 1}位学生信息，总共需录入10位学生信息")
    name = input("请输入学生姓名:")
    age = int(input("请输入学生年龄:"))
    address = input("请输入学生地址:")
    stu = {}
    stu[name] = Student(name,age,address)
    print(f"学生{i + 1}信息录入完成，信息为:[学生姓名: {name}，年龄:{age}，地址:{address}]")


