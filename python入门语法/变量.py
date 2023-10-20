""""
作者：blithe
时间：23.10.11
作用：演示python中变量的相关操作
"""

# 定义一个变量，用来记录钱包余额
money =50
# 通过print输出变量记录的内容
print("钱包还有：",money)

# 买了一个冰淇淋，花费10元
money -= 10
print("钱包还有：",money)

# 假设，每隔一小时，输出钱包的余额
time = 10

print("现在是下午",time,"点，钱包余额还有",money,"元")