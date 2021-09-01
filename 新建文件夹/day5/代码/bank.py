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

bank = {'yzg': {
    'account': '12345678',
    "password": 123456,
        "country": 'a',
        "province": 'b',
        "street": 'c',
        "door": '4',
        "money": 10000,
        "bank_name": "狼腾测试猿银行"}}      # 创建一个字典
bank_name = "狼腾测试猿银行"    # 银行


# 用户信息
def bank_adduser(account, username, password, country, province, street, door):
    if len(bank) > 100:
        return 3
    if username in bank:            # 如变量在容器内执行下面的代码
        return 2
    bank[username] = {
        "account": account,          #
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": 0,
        "bank_name": bank_name
    }
    return 1


# 开户
def adduser():         # 定义了一个方法
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account = random.randint(10000000, 99999999)
    stast = bank_adduser(account, username, password, country, province, street, door)
    #        调用方法   （元素，，，，，，，，，）
    if stast == 3:
        print("你去别的银行吧")
    elif stast == 2:
        print("开户失败，你别重复")
    elif stast == 1:
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))


# 取钱
def quqian():
    ac = input("你的账号：")
    for key in bank.keys():
        if ac == bank[key]['account']:
            pa = int(input("你的密码："))
            if pa == bank[key]['password']:
                money = int(input("输入你要取出的金额："))
                if money > bank[key]['money']:
                    print("该账户没有足够的钱")
                    break
                    return 3
                else:
                    bank[key]['money'] -= money
                    print("您取出了{}。当前余额为{}".format(money, bank[key]['money']))
                    break
            else:
                print("密码输入错误")
                break
                return 2
    else:
        print("没有该账户")
        return 1


# 存钱
def cunqian():
    ac = input("你的账号：")
    for key in bank.keys():
        if ac == bank[key]['account']:
            pa = int(input("你的密码："))
            if pa == bank[key]['password']:
                money = int(input("输入你要存入的金额："))
                bank[key]['money'] += money
                print("您存入了{}。当前余额为{}".format(money, bank[key]['money']))
                break
            else:
                print("密码输入错误")
                break
                return 2
    else:
        print("没有该账户")
        return 1


# 转账
def zhuangzhang():
    chuac = input('转出的账号：')
    for k1 in bank.keys():
        if chuac == bank[k1]['account']:
            ruac = input('转入的账号：')
            for k2 in bank.keys():
                if ruac == bank[k2]['account']:
                    chupa = int(input('请输入密码：'))
                    if chupa == bank[k1]['password']:
                        money = int(input('输入转账金额：'))
                        if money > bank[k1]['money']:
                            print('您的账户余额不足！')
                            break
                            return 3
                        else:
                            bank[k1]['money'] -= money
                            bank[k2]['money'] += money
                            print('您转账{}到{}账户\n当前余额：{}'.format
                                  (money, bank[k2]['account'], bank[k1]['money']))
                            break
                    else:
                        print('密码错误')
                        break
                        return 2
            else:
                print('转入账户不存在')
                break
                return 1
    else:
        print('账户不存在')
        return 1


# 查询
def chaxun():
    ac = input('请输入账户：')
    for key in bank.keys():
        if bank[key]['account'] == ac:
            pa = int(input('请输入密码：'))
            if bank[key]['password'] == pa:
                info = '''
                                    ------------个人信息------------
                                    用户名:%s
                                    账号：%s
                                    密码：*****
                                    国籍：%s
                                    省份：%s
                                    街道：%s
                                    门牌号：%s
                                    余额：%s
                                    开户行名称：%s
                                '''
                print(info % (key,
                              bank[key]['account'],
                              bank[key]['country'],
                              bank[key]['province'],
                              bank[key]['street'],
                              bank[key]['door'],
                              bank[key]["money"],
                              bank[key]['bank_name']))
                break
            else:
                print('密码错误！')
                break
    else:
        print('账户不存在！')


# 运行业务
while True:
    begin = input("请输入业务选项：")       # 选择业务
    if begin == "1":
        adduser()
    elif begin == "2":
        quqian()
    elif begin == "3":
        cunqian()
    elif begin == "4":
        zhuangzhang()
    elif begin == "5":
        chaxun()
    else:
        print("再见")
        break
