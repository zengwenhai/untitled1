import csv


def readCsv():
    with open('test.csv', 'r') as f:
        reader = csv.reader(f)
        # next(reader)
        # db = [item for item in reader]
        # print(list(db))
        for item in reader:
            print(item)


def readCsvDict():
    with open('test.csv', 'r') as f:
        reader = csv.DictReader(f)
        # next(reader)
        for item in reader:
            print(dict(item))

readCsvDict()