# class Air:
#     __brand = ''
#     __price = 0
#
#     def setBrand(self, brand):
#         self.__brand = brand
#
#     def getBrand(self):
#         return self.__brand
#
#     def setPrice(self, price: int):
#         if price >0:
#             self.__price = price
#         else:
#             print('一分钱一分货')
#
#     def getPrice(self):
#         return self.__price
#
#     def onAir(self):
#         print('空调开机了……')
#
#     def offAir(self, time: int):
#         if time < 0:
#             print('无法执行')
#         else:
#             print('空调将在', time, '分钟后自动关闭')
#
#
# a1 = Air()
# a1.setBrand('sss')
# a1.setPrice(200)
# print('空调的品牌为', a1.getBrand(), ',价格为', a1.getPrice())
# a1.onAir()
# a1.offAir(12)


# class Student:
#     __name = ''
#     __age = 0
#
#     def setName(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     def setAge(self, age: int):
#         if age > 0:
#             self.__age = age
#         else:
#             print('you ……')
#
#     def getAge(self):
#         return self.__age
#
#     def Introduce(self):
#         print('大家好，我叫', self.__name, '今年', self.__age, '岁了！')
#
#     def Compare(self, Student):
#         if Student.getAge() < self.__age:
#             return print("我比同桌大", self.__age-Student.getAge(), "岁！")
#         elif Student.getAge() > self.__age:
#             return print("我比同桌小", Student.getAge()-self.__age, "岁！")
#         else:
#             return print('我和同桌一样大')
#
#
# s1 = Student()
# s1.setName('万单')
# s1.setAge(20)
# s1.Introduce()
# s2 = Student()
# s2.setName('步区')
# s2.setAge(30)
# s2.Introduce()
# s1.Compare(s2)
# s2.Compare(s1)
# s1.Compare(s1)


class Person:
    __name = ''
    __sex = ''
    __age = 0
    __cost = 0
    __brand = ''
    __battery = 0
    __size = 0
    __standby = 0
    __integral = 0

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSex(self, sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def setAge(self, age: int):
        if age > 0:
            self.__age = age
        else:
            print('年龄不符')

    def getAge(self):
        return self.__age

    def setCost(self, cost: int):
        self.__cost = cost

    def getCost(self):
        return self.__cost

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setBattery(self, battery: int):
        if battery >0:
            self.__battery = battery
        else:
            print('这个电池没有用啊！')

    def getBattery(self):
        return self.__battery

    def setSize(self, size: int):
        if size > 0:
            self.__size = size
        else:
            print('无法使用')

    def getSize(self):
        return self.__size

    def setStandby(self, standby: int):
        self.__standby = standby

    def getStandby(self):
        return self.__standby

    def setIntegral(self, integral: int):
        self.__integral = integral

    def getIntegral(self):
        return self.__integral

    def show(self):
        print('姓名', self.__name, '\n性别', self.__sex, '\n年龄', self.__age, '\n所拥有的手机剩余话费',
              self.__cost, '元！\n手机品牌', self.__brand, '\n手机电池容量', self.__battery, '%\n屏幕大小',
              self.__size, '寸\n最大待机时长', self.__standby, '分钟\n所拥有积分：', self.__integral)

    def call(self):
        nu = input('请输入电话号码：')
        time = int(input('打电话的时间：'))
        self.__cost = self.__cost - time
        if self.__cost < 0:
            print('欠费')
            return 0
        self.__integral += 1
        print('已经打通', nu, '\n通话时间：', time, '分钟')

    def send(self, nu):
        nu = input('请输入电话号码：')
        s1 = input('请输入短信内容：')
        print('收信人：', nu, '\n短信内容：', s1)


p1 = Person()
p1.setName('李明')
p1.setSex('男')
p1.setAge(30)
p1.setCost(40)
p1.setBrand('ss')
p1.setBattery(9999)
p1.setSize(9)
p1.setStandby(90)
p1.setIntegral(89)
p1.show()
p1.call()
p1.send()
p1.show()
