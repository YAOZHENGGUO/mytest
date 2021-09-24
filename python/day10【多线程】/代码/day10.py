from threading import Thread, Lock
import time


count = 0
lock = Lock()


class Chef(Thread):
    def run(self):
        global count
        while True and 1:
            if count <= 500:
                count += 1
                print('蛋挞数量：', count)
            else:
                print('已经装满')
                time.sleep(3)


class Customer(Thread):
    __money = 3000
    __buy = 0

    def run(self):
        global count
        while self.__money >= 2:
            if count > 0:
                count -= 1
                self.__buy += 1
                self.__money -= 2
                print('蛋挞数量：', count)
            else:
                print('蛋挞不足')
                time.sleep(2)
        print('没钱了')


chef1 = Chef()
chef2 = Chef()
chef3 = Chef()
customer1 = Customer()
customer2 = Customer()
customer3 = Customer()
customer4 = Customer()
customer5 = Customer()
chef1.start()
chef2.start()
chef3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()

