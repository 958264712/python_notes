""""
作者：blithe
时间：23.10.12
作用：Do I need to buy a ticket练习
"""
# 通过input语句获取键盘输入的高
# 判断身高是否超过120cm，并通过print给出提示信息
print("Welcome to HeiMa zoo!!!")
age = int(input("Please input your height（cm）："))
if age >= 120:
    print("If your height exceeds 120cm, a supplementary ticket of 10 yuan is required to play!")
else:
    print("If your height is under 120cm, you can play for free!")

print("Wish you a happy trip!")