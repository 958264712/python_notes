""""
作者：blithe
时间：23.10.12
作用：有几个偶数练习
"""
# 定义一个数字变量num，内容随意
# 并使用range()语句，获取从1到num的序列，使用for循环遍历它
# 在遍历的过程中，统计有多少偶数出现

import random
num = random.randint(100, 1000)
sum = 0
for i in range(1,num):
    if i % 2 == 0:
        sum += 1
print(f"1到{num}(不含{num}本身)范围内，有{sum}个偶数")