""""
作者：blithe
时间：23.10.12
作用：实战案例
"""
# 案例需求:
# 定义一个数字(1~10,随机产生)，通过3次判断来猜出来数字
# 案例要求:
# 数字随机产生，范围1-10
# 有3次机会猜测数字，通过3层嵌套判断实现
# 每次猜不中，会提示大了或小了

# 提示，通过如下代码，可以定义一个变量num，变量内存储随机数字
import random
num = random.randint(1,10)
guess_num = int(input("Please enter your guess the number:"))

if guess_num != num:
    if guess_num >= num:
        print("The number you guessed is large than I though")
    elif guess_num < num:
        print("The number you guessed is smaller than I though")
    guess_num = int(input("Please enter your guess the number again:"))
    if guess_num != num:
        if guess_num >= num:
            print("The number you guessed is large than I though")
        elif guess_num < num:
            print("The number you guessed is smaller than I though")
        guess_num = int(input("Please the end again enter your guess the number:"))
        if guess_num != num:
            if guess_num >= num:
                print("The number you guessed is large than I though")
            elif guess_num < num:
                print("The number you guessed is smaller than I though")
            print(f"I guessed the number is {num}")
        else:
            print("Yes,Your guess the same thing as me")
    else:
        print("Yes,Your guess the same thing as me")
else:
    print("Yes,Your guess the same thing as me")


