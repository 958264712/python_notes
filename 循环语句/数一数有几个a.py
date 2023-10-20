""""
作者：blithe
时间：23.10.12
作用：数一数有几个a练习
"""
name = "itheima is a brand if itcast"
sum = 0
for i in name:
    if i == "a":
        sum += 1

print(f"{name} contains a total of:{sum} letter a")