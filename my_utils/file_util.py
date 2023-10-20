# 函数: print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，
# 如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
# 函数: append_to_file(file_name, data)，接收文件路径以及传入数据，将数据追加写入到文件中
def print_file_info(file_name):
    """
    功能是:将给定路径的文件内容输出到控制台中
    :param file_name: 即将读取的文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name,'r',encoding='UTF-8')
        print(f.read())
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    """
    功能:将指定的数据追加到指定的文件中
    :param file_name: 指定的文件的路径
    :param data: 指定的数据
    :return: None
    """
    f = None
    try:
        f = open(file_name,'a',encoding='UTF-8')
        f.write(f'{data}\n')
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    print_file_info('F:/PythonLearn/文件操作/123.txt')
    append_to_file('F:/PythonLearn/文件操作/123.txt','1231231')