""""
作者：blithe
时间：23.10.12
作用：Guess the number in your mind练习
"""
# 1.定义一个变量，数字类型，内容随意
# 2.基于input语句输入猜想的数字，通过if和多次elif的组合，判断猜想数字是否和心里数字一致
mind_number = 6
if int(input("Please enter the number for your first guess:")) == mind_number:
    print("Yes, you guessed the same thing as me!")
elif int(input("No,Guess again:")) == mind_number:
    print("Yes, you guessed the same thing as me!")
elif int(input("No,the end guess again:")) == mind_number:
    print("Yes, you guessed the same thing as me!")
else:
    print("Sorry,All guessed false,I guessed is %d"%mind_number)