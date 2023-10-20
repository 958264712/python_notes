""""
作者：blithe
时间：23.10.19
作用：通过传进的地址进行操作返回一个list
"""
import json
from main1 import Record

class Address:
    def read_data(self) -> list[Record]:
        pass

class GetAllData(Address):
    # ,date,order_id,money,province
    def __init__(self,path):
        self.path = path
        # self.date = date
        # self.order_id = order_id
        # self.money = money
        # self.province = province

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        data = f.readlines()
        f.close()
        list: list[Record] = []
        for i in data:
            i = i.strip().split(',')
            record = Record(i[0], i[1], int(i[2]), i[3])
            list.append(record)
        return list
    def read_json_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        data = f.readlines()
        f.close()
        list:list[Record] = []
        for i in data:
            i = json.loads(i)
            record = Record(i["date"],i["order_id"],int(i["money"]),i["province"])
            list.append(record)
        return list



if __name__ == '__main__':
    flies = GetAllData('F:/PythonLearn/综合案例/2011年1月销售数据.txt')
    flies1 = GetAllData('F:/PythonLearn/综合案例/2011年2月销售数据JSON.txt')
    list1 = flies.read_data()
    list2 = flies1.read_json_data()
