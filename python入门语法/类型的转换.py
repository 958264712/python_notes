""""
作者：blithe
时间：23.10.11
作用：类型的转换
"""

""""
强类型的转换
int(x) 将x转为整数
str(x) 将x转为字符串
float(x) 将x转为浮点数
"""

# 例子
num = 10
print(type(num))
print(type(str(num)) )
""""
<class 'int'>
<class 'str'>
"""

floats = 3.1415926
print(type(floats))
print(type(str(floats)) )
print(type(int(floats)) )
floats = int(floats)
print(floats)

""""
<class 'float'>
<class 'str'>
<class 'int'>
3
"""

string = "字符串"

print(type(string))
# print(type(int(string))) 没有数字会报错
strNum = "3.14315"
print(type(strNum))
print(type(float(strNum)))
# print(type(int(strNum))) 不是整数即会报错
""""
<class 'str'>
<class 'float'>
"""
strInt = "6"
print(type(strInt))
print(type(int(strInt)))
print(type(float(strInt)))
""""
<class 'str'>
<class 'int'>
<class 'float'>
"""