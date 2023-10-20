""""
作者：blithe
时间：23.10.18
作用：成员方法
"""
# 在类中定义成员方法和定义函数基本一致，但仍有细微区别:
# def 方法名(self,形参1,......,形参n):
#     方法体
# self为必填
"""
self关键字是成员方法定义的时候，必须填写的。
它用来表示类对象自身的意思
当我们使用类对象调用方法的是，self会自动被python传入
在方法内部，想要访问类的成员变量，必须使用self
"""

# 定义一个带有成员方法的类
class Student:
    name = None


    def say_hi(self):
        print(f"hi everybody!my name is {self.name},Please take care of me ")

    def say_hi1(self,msg):
        print(f"hello everybody! my name is {self.name},{msg}")

stu = Student()
stu.name = 'blithe'
stu.say_hi()
stu.say_hi1('thanks')
stu1 = Student()
stu1.name = 'jay'
stu1.say_hi()