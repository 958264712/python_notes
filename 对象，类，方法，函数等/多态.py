""""
作者：blithe
时间：23.10.19
作用：多态
"""
# 多态，指的是:多种状态，即完成某个行为时，使用不同的对象会得到不同的状态。
# 抽象类:含有抽象方法的类称之为抽象类
# 抽象方法:方法体是空实现的 (pass)称之为抽象方法
# 1.什么是多态?
# 多态指的是，同一个行为，使用不同的对象获得不同的状态。
# 如，定义函数(方法)，通过类型注解声明需要父类对象，实际传入子类对象进行工作，从而获得不同的工作状态
# 2.什么是抽象类 (接口)
# 包含抽象方法的类，称之为抽象类。抽象方法是指: 没有具体实现的方法 (pass)称之为抽象方法
# DX
# 3.抽象类的作用
# 多用于做顶层设计(设计标准)，以便子类做具体实现。
# 也是对子类的一种软性约束，要求子类必须复写(实现)父类的一些方法
# 并配合多态使用，获得不同的工作状态
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

# 抽象类
class Ph:
    def photo_pixels(self):
        """拍照像素"""
        pass
    def battery_capacity(self):
        """电池容量"""
        pass
    def communication_signal(self):
        """通信信号"""
        pass

class Hw(Ph):
    def photo_pixels(self):
        """拍照像素"""
        print("4k像素，1w倍拍摄")
    def battery_capacity(self):
        """电池容量"""
        print("超大容量，380w快充")
    def communication_signal(self):
        """通信信号"""
        print("5g信号，遥遥领先")

class Ip(Ph):
    def photo_pixels(self):
        """拍照像素"""
        print("1080像素，5倍拍摄")
    def battery_capacity(self):
        """电池容量"""
        print("4080容量，20w快充")
    def communication_signal(self):
        """通信信号"""
        print("5g信号，虚假信号")

def user(ph:Ph):
    ph.photo_pixels()
    ph.battery_capacity()
    ph.communication_signal()

hw = Hw()
ip = Ip()

user(hw)
user(ip)