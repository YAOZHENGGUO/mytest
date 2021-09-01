import random

money = 100  # 初始资金100
i = 0  # 计数器
number = random.randint(0, 100)  # 随机生成一个0~100的数字
while money >= 10:
    i += 1
    print('第{}次'.format(i))
    print('你的资金：{}'.format(money))
    number1 = int(input("请输入你猜的数字："))
    money -= 10  # 猜一次资金减少10
    if number1 == number:
        print("你赢了")
        money += 30  # 猜对后奖励资金30
        number = random.randint(0, 100)  # 为number重新随机赋值
    elif number1 > number:
        print("猜大了")
    elif number1 < number:
        print("猜小了")
    else:
        print("输入错误")
print("累计猜测次数:{}".format(i))
print("资金剩余:{0}".format(money))
print("游戏结束，再见")
