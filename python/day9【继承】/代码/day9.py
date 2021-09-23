class Chef:
    __name = ''
    __age = 0

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def steamed(self):
        print(self.__name, '正在蒸饭。')


class Chef2(Chef):
    def fried(self):
        print(self.getName(), '正在炒菜。')


class Chef3(Chef2):
    def steamed(self):
        print('蒸饭')

    def fried(self):
        print('炒菜')


# C1 = Chef3()
# C1.setName('李明')
# C1.setAge(778)
# print('厨师的名字：', C1.getName(), '\n厨师的年龄：', C1.getAge())
# C1.steamed()
# C1.fried()


class Person:
    __name = ''
    __age = 0
    __sex = ''

    def setName(self, name):
        self.__name = name

    def setAge(self, age: int):
        if age < 0:
            print('输入有误！')
        else:
            self.__age = age

    def setSex(self, sex):
        self.__sex = sex

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getSex(self):
        return self.__sex


class Worker(Person):
    def work(self):
        print(self.getName(), '正在干活')


class Student(Person):
    __number = ''

    def setNumber(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number

    def learn(self):
        print(self.getName(), '正在学习。')

    def sing(self):
        print(self.getName(), '正在唱歌。')


# w1 = Worker()
# w1.setName('张三')
# w1.setAge(45)
# w1.setSex('男')
# w1.work()
# s1 = Student()
# s1.setName('七七')
# s1.setAge(9)
# s1.setSex('女')
# s1.learn()
# s1.sing()
