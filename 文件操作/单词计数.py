""""
作者：blithe
时间：23.10.16
作用：单词计数练习
"""
with open('F:/PythonLearn/文件操作/word.txt','r',encoding='UTF-8') as f:
    num = 0
    # 1.
    for i in f:
        ind = i.strip()
        words = ind .split(" ")
        for w in words:
            if w == 'itheima':
                num += 1
    # 2.
    # num = f.read().count("itheima")
    print(f'itheima单词出现的次数为{num}次')
