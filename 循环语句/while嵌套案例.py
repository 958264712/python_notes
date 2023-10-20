""""
作者：blithe
时间：23.10.12
作用：while嵌套案例
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

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t",end='')
        j += 1
    i += 1
    print()