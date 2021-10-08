import xlrd
import xlwt
wb = xlrd.open_workbook(filename=r"../\\数据\\2020年每个月的销售情况.xls")
sheet = wb.sheet_by_name("12月")
rows = sheet.nrows
cols = sheet.ncols

# 练习xlwt
lx = xlwt.Workbook('utf-8')
sh1 = lx.add_sheet('my_xlwt', False)
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Time New Roman'
font.bold = True
font.underline = False
font.italic = True
style.font = font
sh1.write(0, 0, 'no style')
sh1.write(1, 0, 'style', style)
lx.save('../\\数据\\style.xls')