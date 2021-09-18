import xlrd
import xlwt
wb = xlrd.open_workbook(r'../\\数据\\2020年每个月的销售情况.xls')


# 月销售统计
def cloth_per_moth(x):
    sheet = wb.sheet_by_name("{}月".format(x))
    rows = sheet.nrows
    tj = {}
    for i in range(1, rows):
        data = sheet.row_values(i)
        s = data[2]*data[4]
        if data[1] in tj:
            tj[data[1]] += round(s)
        else:
            tj[data[1]] = round(s)
    print("{}月份销售：{}".format(x, tj))
    return tj


# 月销售总额
def moth(x):
    sheet = wb.sheet_by_name("{}月".format(x))
    rows = sheet.nrows
    su = 0
    for i in range(1, rows):
        data = sheet.row_values(i)
        su = su + data[2] * data[4]
    print("{}月份销售总额：".format(x), round(su, 2))
    return su


# 月销售
def mother_sale(x):
    sheet = wb.sheet_by_name('{}月'.format(x))
    rows = sheet.nrows
    per = {}
    a = list(set(sheet.col_values(1, 1)))
    for x in a:
        y = 0
        for i in range(1, rows):
            data = sheet.row_values(i)
            if data[1] == x:
                y += data[4]
        per[x] = int(y)
    return per


# 年销售
def year_sale():
    year = {}
    y2 = {}
    for i in range(12):
        i += 1
        a = '{}'.format(i)+'月'
        year[a] = mother_sale(i)
    for value in year.values():
        for k, v in value.items():
            if k in y2:
                y2[k] += v
            else:
                y2[k] = v
    return y2


# 销售最多
def max_sale(a):
    max_v = 0
    for k, v in a.items():
        if v > max_v:
            max_v = v
            i = k
    print('销售最多的是{}，为{}件'.format(i, a[i]))


# 销售最少
def min_sale(a):
    min_v = 0
    for k, v in a.items():
        if v < min_v or min_v == 0:
            min_v = v
            i = k
    print('销售最少的是{}，为{}件'.format(i, a[i]))


# 销售占比
def per_sale(a):
    per = {}
    su = sum(a.values())
    for k, v in a.items():
        per[k] = a[k]/su
    print('销售占比')
    for k1, v1 in per.items():
        print('{}:{}'.format(k1, round(v1 * 100, 2)), '%')
    return per


# 执行
# 全年销售总额
mother = 0
for i in range(1, 13):
    mother += moth(i)
print('年销售总额：', round(mother, 1))
# 每件衣服的销售（件数）占比
y = year_sale()
print('每件衣服的销售（件数）占比')
per_sale(y)
# 每件衣服的月销售占比
print('每种衣服每月销售多少件')
for q in range(12):
    q += 1
    print(q, '月：')
    per_sale(mother_sale(q))
# 每件衣服的销售额占比
for m1 in range(1, 13):
    per_sale(cloth_per_moth(m1))
# 最畅销的衣服
print('全年最畅销的衣服')
max_sale(y)
# 每个季度最畅销的衣服
first_quartely = {}
mo1 = {}
for i in [2, 3, 4]:
    mo1[i] = mother_sale(i)
    for k, v in mo1[i].items():
        if k in first_quartely:
            first_quartely[k] += v
        else:
            first_quartely[k] = v
print('第一季度')
max_sale(first_quartely)
second_quartely = {}
mo2 = {}
for i in [5, 6, 7]:
    mo2[i] = mother_sale(i)
    for k, v in mo2[i].items():
        if k in second_quartely:
            second_quartely[k] += v
        else:
            second_quartely[k] = v
print('第二季度')
max_sale(second_quartely)
third_quartely = {}
mo3 = {}
for i in [8, 9, 10]:
    mo3[i] = mother_sale(i)
    for k, v in mo3[i].items():
        if k in third_quartely:
            third_quartely[k] += v
        else:
            third_quartely[k] = v
print('第三季度')
max_sale(third_quartely)
forth_quartely = {}
mo4 = {}
for i in [10, 11, 12]:
    mo4[i] = mother_sale(i)
    for k, v in mo4[i].items():
        if k in forth_quartely:
            forth_quartely[k] += v
        else:
            forth_quartely[k] = v
print('第四季度')
max_sale(forth_quartely)
# 全年销量最低的衣服
print('全年销售最少')
min_sale(y)
