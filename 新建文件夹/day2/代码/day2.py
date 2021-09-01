# import random

# 输入10个数字，打印10个数的求和结果
# i = 0
# num = 0
# while i < 10:
#     i += 1
#     num1 = int(input('请输入第{}个数字:'.format(i)))
#     num += num1
# print("结果为 {}".format(num))

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
# i = 0
# max_num = 0
# s = 0
# while i < 10:
#     i += 1
#     num = int(input('请输入第{}个数字：'.format(i)))
#     s += num
#     if i == 1:
#         max_num = num
#     else:
#         if max_num < num:
#             max_num = num
#         else:
#             max_num = max_num
# print("最大的数：{0}\n10个数的和：{1}\n平均数为：{2}".
#       format(max_num, s, s/10))

# 使用random模块，如何产生50~150之间的数
# print(random.randint(50, 150))

# 从键盘输入任意三边，判断是否能形成三角形，若可以，判断形成什么三角形
# a = int(input('第一条边长：'))
# b = int(input('第二条边长：'))
# c = int(input('第三条边长：'))
# if a+b > c and a+c > b and b+c > a:
#     print("可以构成三角形")
#     if a == b == c:
#         print('等边三角形')
#     elif a == b != c or a == c != b or b == c != a:
#         print('等边三角形')
#     elif a*a+b*b == c*c or b*b+c*c == a*a or c*c+a*a == b*b:
#         print('直角三角形')
#     else:
#         print('普通三角形')
# else:
#     print('不能构成三角形')

# 使用+，—号实现两个数的调换
# A, B = 56, 78
# print('A:{},B:{}'.format(A, B))
# A = A + B
# B = A - B
# A = A - B
# print('A:{},B:{}'.format(A, B))

# 实现登录系统的三次密码输入错误锁定功能（用户名：root，密码：admin）
# user = 'root'
# password = 'admin'
# for i in range(10):
#     if i == 3:
#         print('locking')
#         break
#     else:
#         u = input('root:')
#         p = input('password:')
#         if u == user and p == password:
#             pass
#         else:
#             print('error')

# 打印图形
# for i in range(7):
#     print(" "*(6-i), end="")
#     print("* "*(i+1))

# 使用while循环实现99乘法表的打印
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print("{} * {} = {}".format(i, j, i*j), end=" ")
#         j += 1
#     print("")
#     i += 1

# 倒叙打印99乘法表
# i = 9
# while i >= 1:
#     j = 1
#     while j <= i:
#         print("%d*%d=%2d" % (i, j, i*j), end=' ')
#         j += 1
#     print()
#     i -= 1

# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，
# 问第几天能出来？请编程求出
# i = 0
# h = 0
# while 1:
#     i += 1
#     if h+3 >= 20:
#         print("come out")
#         break
#     else:
#         h = 1*i
# print('第{}天出来了'.format(i))

# 20以内的阶乘
# i = 1
# re = 0
# while i < 20:
#     j = 1
#     e = 1
#     while j <= i:
#         e = j*e
#         j += 1
#     re += e
#     print('{}!+'.format(i), end='')
#     i += 1
#     while i == 19:
#         i += 1
#         print('{}!='.format(i))
# print(re)

# 判断下列变量命名是否合法
# char = 1
# # Cy%ty = 1    #非法变量
# Oax_li = 1
# # $123 = 1     #非法变量
# fLul = 1
# # 3_3 = 1      #非法变量
# BYTE = 1
# T_T = 1
