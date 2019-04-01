import requests
import json


payload = {'some': 'data'}
url = 'https://api.github.com/some/endpoint'
# 方式一：将字典数据序列化为json格式的字符串类型
#r = requests.post(url=url, data=json.dumps(payload))

# 方式二：使用json参数直接传递，就会被自动编码
r = requests.post(url=url, json=payload)
print(r.text)