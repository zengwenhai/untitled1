from xlutils.copy import copy # 只能修改xls后缀的文件格式，xlxs后缀格式在写入时会被破坏原文件
import os
import xlrd

def base_url(filename=None):
    return os.path.join(os.path.dirname(__file__), filename)


work = xlrd.open_workbook(base_url('test1.xls'))  # 实例化文件对象
print(work)

old_content = copy(work)  # 复制未信息的xls
ws = old_content.get_sheet(0)  # 通过索引获取sheet
ws.write(3, 3, 111)  # 修改新的xls文件内容
old_content.save(base_url('test1.xls'))  # 修改后保存