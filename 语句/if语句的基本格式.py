""""
作者：blithe
时间：23.10.12
作用：if的基本格式,if语句，if else语句，if elif else语句
"""
# if 要判断的条件: 条件成立时，要做的事情
# elif: 多条件成立时，要做的事情
# else: 条件不成立时，要做的事情
# 定义变量
# age =11
# if age >= 22: print("可以打结婚证了！！！")
# else: print("不可以打结婚证!!!")
#
# if age >= 18:
#     print("你已经成年了")
#     print("你可以做一下成年人的事情")
#
# print("end...")
height = int(input("请输入你的身高（cm）："))
vip_level = int(input("请输入你的VIP等级（1-5）："))

if height < 120:
    print("身高小于120cm，可以免费。")
elif vip_level > 3:
    print("vip级别大于3，可以免费。")
else:
    print("两个条件都不满足，需要买票10元。")