import xlrd,xlwt  # 该库有个缺点，会把原来的内容删除再进行写入
import os
import xlutils


def base_url(filename=None):
    return os.path.join(os.path.dirname(__file__), filename)


work = xlrd.open_workbook(base_url('test1.xls'))
sheet = work.sheet_by_name('Sheet1')  # 获取sheet对象
print(sheet.nrows)  # 查看数据表有多少行
print(sheet.get_rows())  # 获取行数据，返回的是一个迭代器
for i in sheet.get_rows():
    print(i)

print(sheet.cell_value(1, 2))  # 获取单元格的数据，传入行号、列号
print(sheet.row_values(1))  # 获取任意一行的数据