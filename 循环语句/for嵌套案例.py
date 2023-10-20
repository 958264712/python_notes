""""
作者：blithe
时间：23.10.12
作用：for嵌套案例
"""
# end = '' 不换行 \t字符对齐
# left_num = 1
# right_num = 1
# sum = 0
# while sum != 81:
#     sum = left_num * right_num
#     if left_num == right_num:
#         print(f"{left_num} * {right_num} = {sum}\t")
#         right_num += 1
#         left_num = 1
#     elif left_num < right_num:
#         print(f"{left_num} * {right_num} = {sum}",end=' ')
#         left_num += 1

for i in range(1,10):
    for j in range(1,i +1):
        print(f"{j} * {i} = { i * j }\t",end='')
    print()