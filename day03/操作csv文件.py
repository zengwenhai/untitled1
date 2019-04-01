import csv

def readCsv():
    with open('test.csv', 'r') as f:  # 使用上下文打开csv文件
        reader = csv.reader(f)  # 创建csv阅读器对象
        # next(reader)
        # 方式一：通过将读取的数据用列表生成式返回
        # db = [item for item in reader]  # 列表生成式，将读取到的数据放在列表中
        # print(type(db))

        # 方式二：循环读取文件数据
        for item in reader:
            print(item)


def readCsvDict():  # 操作字典那样读取数据，把表头的第一行作为key
    with open('test.csv', 'r') as f:
        reader = csv.DictReader(f)
        # next(reader)
        for item in reader:
            print(item)


def writeCsv():
    with open('test1.csv', 'a', newline='') as f:  # newline=''指定该参数，表示不写入空行
        row = ['3', 'www.sofu.com']
        # write = csv.writer(f)  # 创建csv写入器对象
        # 方式一：一次写入一行
        # write.writerow(row)

        # 方式二：一次写入多行
        # data = [['4', 'www.12306.com'],
        #         ['5', 'www.jd.com']]
        # for row in data:
        #     write.writerow(row)

        # 方式三：使用DictWriter类，将内容以字典形式写入
        headers = ['caseID', 'URL']  # 数据表头
        datas = [{'caseID': '6', 'URL': 'www.albb.com'},
                 {'caseID': '7', 'URL': 'www.vip.com'}]
        writer = csv.DictWriter(f, headers)  # 这里传入表头，作为第一行的数据
        writer.writeheader()
        # for row in datas:
        #     writer.writerow(row)

        writer.writerows(datas)  # 一次写入多行
        print("写入完成!")


# readCsvDict()
# readCsv()
writeCsv()