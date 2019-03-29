import json

dict1 = {'name': 'zengwenhai', 'age': 29, 'address': '宝安区'}
print('未序列化前的数据类型为:', type(dict1))
print('序列化前的数据:', dict1)

# 对dict1数据进行序列化的处理
dict_xu = json.dumps(dict1, ensure_ascii=False)
print('序列化后的数据类型为:', type(dict_xu))
print('序列化后的数据为:', dict_xu)

# 对dict_xu进行反序列化的处理
dict_fan = json.loads(dict_xu)
print("======================================")
print('反序列化的数据类型为:', type(dict_fan))
print('反序列化后的数据为:', dict_fan)