""""
作者：blithe
时间：23.10.18
作用：设计带有私有成员的手机练习
"""
# 私有变量:__is_5g_enable,类型bool,True表示开启5g，False反之
# 私有方法:__check_5g(),会判断__is_5g_enable的值 true打印5g开启，false5g关闭，使用4g网络
# 公开方法:call_by_5g() 调用__check_5g() 打印通话中

class Phone:
    __is_5g_enable = False
    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()