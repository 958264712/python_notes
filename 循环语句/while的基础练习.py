""""
作者：blithe
时间：23.10.12
作用：while基础练习
"""
#设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
#无限次机会，直到猜中为止
# 每一次猜不中，会提示大了或小了
# 猜完数字后，提示猜了几次

import random
num = random.randint(1,100)
sum = 1
guess_num = int(input("Please enter your guess the number:"))

while guess_num != num:
    if guess_num > num:
        print("No,The number you guessed the large than in though")
    elif guess_num < num:
        print("No,The number you guessed the samll than in though")
    guess_num = int(input("Please enter your guess the number:"))
    sum += 1

print(f"The number is {num},You guessed {sum} times in total ")
