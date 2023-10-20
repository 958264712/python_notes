# 函数:str_reverse(s)，接受传入字符串，将字符串反转返回
# 函数:substr(s,x,y)，按照下标x和y，对字符串进行切片
def str_reverse(s):
    """
    将字符串反转返回
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s,x,y):
    """
    按照下标x和y，对字符串进行切片
    :param s:即将被切片的字符串
    :param x:切片的开始下标
    :param y:切片的结束下标
    :return:切片完成后的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse('123456'))
    print(substr('123456',1,3))

