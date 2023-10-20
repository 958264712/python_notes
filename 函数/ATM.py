""""
作者：blithe
时间：23.10.12
作用：ATM练习
"""
# 定义一个全局变量:money用来记录银行卡余额(默认5000000)
# 定义一个全局变量:name，用来记录客户姓名(启动程序时输入)
# 定义如下的函数:查询余额函数 存款函数 取款函数 主菜单函数

# 要求
# 程序启动后要求输入客户姓名
# 查询余额、存款、取款后都会返回主菜单
# 存款、取款后，都应显示一下当前余额
# 客广只有选择退出或者说输错误，程序会退出，否则一直运行

money = 5000000
give_money = 0
add_money = 0
name = input("Please enter your name:")

# 查询余额
def check_balances(money,give_money,add_money):
    # money -= give_money
    # money += add_money
    print(f"your balances is {money}")
    return menu_function(money,give_money,add_money)

# 存款函数
def deposit(money,give_money):
    add_money = int(input("Please enter you need deposit the money:"))
    money += add_money
    # money -= give_money
    print(f"Your money is {money}")
    return menu_function(money,give_money,add_money)

# 取款函数
def withdraw(money,add_money):
    give_money = int(input("Please enter You need withdraw money the money:"))
    # money += add_money
    if money - give_money >= 0:
        money -= give_money
        print(f"Your money is {money}")
    else:
        print("Sorry,Your balance is insufficient")
    return menu_function(money,give_money,add_money)
# 主菜单函数
def menu_function(money,give_money,add_money):
    if name:
        print("Please select the business you want:\n 1.Check balances\n 2.Deposit\n 3.Withdraw money\n 4.Back")
        enter = input("Please enter your select:")
        if int(enter) == 1:
            check_balances(money,give_money,add_money)
        elif int(enter) == 2:
            deposit(money,give_money)
        elif int(enter) == 3:
            withdraw(money,add_money)
        elif int(enter) == 4:
            return print("You will back menu!")
    else:
        return print("You done not enter your name! ")

menu_function(money,give_money,add_money)
