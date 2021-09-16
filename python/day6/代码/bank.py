import pymysql
import random


print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")


db = pymysql.connect(host="localhost", user="root", password="", database='bank')
cursor = db.cursor()

# 取钱
def take_Money():
    ac = input("请输入你的账号：")
    cursor.execute("select * from u_infor where ac = {};".format(ac))
    data = cursor.fetchall()
    if len(data) != 1:
        return print('error')
    pw = int(input("请输入你的密码"))
    if data[0][2] != pw:
        return print('error')
    tamo = int(input("你取出的金额："))
    if tamo > data[0][6]:
        return print('error')
    cursor.execute("update u_infor set mo=mo-{} where ac={}".format(tamo, ac))
    db.commit()
    print('{}取出{}￥'.format(ac, tamo))
    return 0


while True:
    begin = input("请输入业务选项：")       # 选择业务
    if begin == "1":
        pass
    elif begin == "2":
        take_Money()
    elif begin == "3":
        pass
    elif begin == "4":
        pass
    elif begin == "5":
        pass
    else:
        print("再见")
        db.close()
        break
