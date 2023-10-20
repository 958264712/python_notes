""""
作者：blithe
时间：23.10.12
作用：continue and break
"""

# continue跳过 break结束所在的循环
# for i in range(1,6):
#     print("语句1")
#     continue
#     print("语句2")
    # 语句1
    # 语句1
    # 语句1
    # 语句1
    # 语句1

# for i in range(1):
#     print("语句1")
#     for i in range(1):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")
    # 语句1
    # 语句2
    # 语句4

# for i in range(1,101):
#     print("yuju1")
#     break
#     print("yuju2")
# print("yuju3")
# yuju1
# yuju3


for i in range(1,3):
    print("yuju1")
    for i in range(1):
        print("yuju2")
        break
        print("yuju3")
    print("yuju4")
print("yuju5")