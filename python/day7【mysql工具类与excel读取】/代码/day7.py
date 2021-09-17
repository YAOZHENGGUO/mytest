import xlrd
import xlwt
wb = xlrd.open_workbook(r'../\\数据\\2020年每个月的销售情况.xls')


# 月销售额
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


# 销售（件数）占比
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
for q in range(12):
    q += 1
    a = '{}'.format(q) + '月'
    print(q, '月：', mother_sale(q))
mother = 0
for i in range(1, 13):
    mother += moth(i)
print('年销售总额：', round(mother, 1))
y = year_sale()
per_sale(y)
max_sale(y)
min_sale(y)
