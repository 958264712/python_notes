""""
作者：blithe
时间：23.10.13
作用：函数进阶
"""
# 返回多个返回值
def return_many():
    return 1,True,'2'
x,y,z = return_many()
print(x,y,z)

# 函数传参的多种方式
def user_info(name,age,gender):
    print(f"Your name is {name},Age is {age},Gender is {gender}")
#位置参数 - 默认使用形式
user_info('blithe',22,'Man')
# 关键字参数
user_info(age=20,name='xiaoming',gender='Woman')
# 缺省参数（默认值）只能设置到最后
def user_info(name,age,gender='Man'):
    print(f"Your name is {name},Age is {age},Gender is {gender}")
user_info('blithe',22)
# 不定长 - 位置不定长，*号
def user_info(*args):
    print(args)
user_info('blithe',22,'Man')
# 不定长 - 关键字不定长，** 号 key=value
def user_info(**kwargs):
    print(kwargs)
user_info(name='blithe',age=22,gender='Man')

# 匿名函数
# 函数作为参数传递
def test_func(compute):
    result = compute(1,2)
    print(result)
    print(type(compute))

def compute(x,y):
    return x + y;
test_func(compute)

# lambda匿名函数
# 无名称的匿名函数，只可临时使用一次
test_func(lambda x , y:x + y)
# 使用def和使用lambda，定义的函数功能完全一致，只是lambda关键字定义的函数是匿名的，无法二次使用