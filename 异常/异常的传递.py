""""
作者：blithe
时间：23.10.16
作用：异常的传递
"""
# 异常是具有传递性的
def func1():
    print("func1 开始执行")
    num = 1 /0
    print("func1 结束执行")

def func2():
    print("func2 开始执行")
    func1()
    print("func2 结束执行")

def main():
    try:
        func2()
    except Exception as e:
        print(e)
main()