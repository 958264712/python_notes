""""
作者：blithe
时间：23.10.12
作用：判断语句的嵌套
"""
# 简单嵌套
print("Welcome to HeiMa Zoo!")
if int(input("You height is:")) > 120:
    print("If your height exceeds the limit, you will not be free of charge ")
    print("But,If the VIP level is greater than 3, it is free ")
    if int(input("Please Enter your the Vip level(1-5)")) >= 3:
        print("Your the Vip level is greater than 3,So it is free")
    else:
        print("Sorry,You need the buy a ticket")
else:
    print("Children Welcome, Free to play ")