""""
作者：blithe
时间：23.10.11
作用：字符串格式化，数字精度控制，快速格式化，表达式的格式化
"""
# 通过占位的形式，完成拼接
class_num = 57
avg_salary = 16778
name = "blithe"
address = "shenzhen"
tel = 15179265779
birthday = 3.22
message = "this is a number %s" % class_num + " and any number %s" % avg_salary
message1 = "My name is %s,I work in %s,telPhtone is %d ,date of birth %f" %(name,address,tel,birthday)
print(message);print(message1)
# My name is blithe,I work in shenzhen,telPhtone is 15179265779 ,date of birth 3.220000

"""格式化- 数字精度控制"""
message1 = "My name is %s,I work in %s,telPhtone is %11d ,date of birth %.2f" %(name,address,tel,birthday)
print(message1)
# My name is blithe,I work in shenzhen,telPhtone is 15179265779 ,date of birth 3.22

"""格式化- 快速格式化"""
message1 = f"My name is {name},I work in {address},telPhtone is {tel} ,date of birth {birthday}"
print(message1)
# My name is blithe,I work in shenzhen,telPhtone is 15179265779 ,date of birth 3.22

"""格式化- 表达式的格式化"""
print(f"My name is {name},I work in {address},telPhtone is {tel} ,date of birth {birthday},now data:{11 * 1}")
print("My name is %s"%("blithe"))
print("telPhtone is %11d "% (151 *9999))