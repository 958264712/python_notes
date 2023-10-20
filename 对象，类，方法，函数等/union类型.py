""""
作者：blithe
时间：23.10.19
作用：union类型
"""
from typing import Union
my_list: list[Union[int,str]] = [1,'2']
my_dict: dict[str,Union[int,str]] = {"name":"blithe","age":18}

def func(data:Union[int,str]) -> Union[int,str]:
    pass