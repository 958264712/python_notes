""""
作者：blithe
时间：23.10.18
作用：理解封装的概念，掌握私有成员的使用
"""
# 面向对象包含3大主要特性：封装，继承，多态
# 定义私有成员的方式非常简单，只需要私有成员变量:变量名以 __开头 (2个下划线私有成员方法:方法名以开头 (2个下划线)即可完成私有成员的设置

# 定义一个类，内含私有成员变量和私有成员方法
class Phone:
    __current_voltage = 0.5  #当前设计运行电压
    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电。")


phone = Phone()
# phone.__keep_single_core()
phone.call_by_5g()
