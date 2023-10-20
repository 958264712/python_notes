""""
作者：blithe
时间：23.10.12
作用：综合案例
"""
# 某公司，账户余额有1W元，给20名员工发工资
# 员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
# 领工资时，财务判断员工的绩效分(1-10,随机生成)，如果低于5,不发工资，换下一位
# 如果工资发完了，结束发工资

import random


code_num = 20
money =10000
give_money = 1000

for i in range(1,code_num + 1):
    performance_points = int(random.randint(1, 10))
    if performance_points >= 5:
        money -= give_money
        print(f"员工{i}发放了1000元，账户余额还有{money}元")
    else:
        print(f"员工{i},绩效分为{performance_points},低于5，不发工资，下一位")
        continue
    if money == 0:
        break