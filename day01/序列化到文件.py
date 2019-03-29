import json

dict1 = {'name': 'zengwenhai', 'age': 29}
json.dump(dict1, open('name.json', 'w'))
temp = open(r'C:\Users\Administrator\PycharmProjects\untitled1\day01\name.json', 'r', encoding='UTF-8')
print(temp)