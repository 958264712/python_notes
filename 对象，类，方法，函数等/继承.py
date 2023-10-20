""""
作者：blithe
时间：23.10.18
作用：继承的基础语法，掌握继承的使用，掌握pass的使用
"""
# 语法class 类名(父类名): 类内容体

# 单继承
class Phone:
    IMEI = None
    producer = 'HM'

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = "10001"   #面部识别id
    def call_by_5g(self):
        print("2022年新功能：5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_5g()
# 多继承  语法class 类名(父类1,父类2,父类3...父类n): 类内容体
class NFCReader:
    nfc_type ="第五代"
    producer ="HM1"
    def read_card(self):print("读取NFC卡")
    def write_card(self):print("写入NFC卡")
class RemoteContro1:
    rc_type ="红外遥控"
    def contro1(self):print("红外遥控开启")
class MyPhone(Phone,NFCReader,RemoteContro1):
    pass
# pass用来补全语法，表示空
# my_phone = MyPhone()
# print(my_phone.rc_type)
# print(my_phone.nfc_type)
# print(my_phone.producer)
# my_phone.read_card()

# 复写和使用父类成员
# 复写
# 子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写即:在子类中重新定义同名的属性或方法即可
class MyPhone1(Phone,NFCReader,RemoteContro1):
    producer = "HM1"
    def call_by_4g(self):
        print('父类',super().producer)
        super().call_by_4g()
        print("5g通话")


my_phone = MyPhone1()
my_phone.call_by_4g()
print(my_phone.producer)
