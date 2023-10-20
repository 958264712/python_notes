""""
作者：blithe
时间：23.10.13
作用：元组的基本操作
"""
# 定义一个元组，内容是:周杰轮',11,['football，music'])，记录的是一个学生的信息(姓名、年龄、爱好)
# 请通过元组的功能(方法)，对其进行
# 1.查询其年龄所在的下标位置
# 2.查询学生的姓名
# 3.删除学生爱好中的football
# 4.增加爱好:coding到爱好list内

new_tuple = ('周杰轮',11,['football','music'])

age = new_tuple[1]
name = new_tuple[0]
del new_tuple[2][0]
new_tuple[2].append('coding')
print(age,name,new_tuple)