""""
作者：blithe
时间：23.10.12
作用：for嵌套应用
"""

for i in range(1,101):
    print(f"今天是第{i}天，准备表白......")
    # 内层
    for j in range(1,11):
        print(f"送给小美第{j}只玫瑰花")
    print("小美，我喜欢你")
print(f"坚持到第{i}天，表白成功")