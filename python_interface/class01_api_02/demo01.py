import json

import requests

# 基本用法
# requests.get('https://api.github.com/events')
# requests.post('http://httpbin.org/post', data={'key': 'value'})

# 传递url参数 - GET 请求
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)

# 响应内容
# r = requests.get('https://api.github.com/events')
# print(r.text)
# print(type(r.text))

# json 响应内容
# r = requests.get('https://api.github.com/events')
# json_data = r.json()
# print(type(json_data))

# 通过json模块来进行转换
# r = requests.get('https://api.github.com/events')
# json_data = json.loads(r.text)
# print(type(json_data))

# 稍微复杂的表单提交请求
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post('http://httpbin.org/post', data=payload)
# print(type(r.text))
# print(r.text)
# print(r.json())

# json请求
# 在调用post方法时，给json关键字参数赋值python字典
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post('http://httpbin.org/post', json=payload)
# print(r.text)

# 在调用post方法时，给data关键字参数赋值json字符串
# payload = {'key1': 'value1', 'key2': 'value2'}
# 将字典转换成json字符串
# payload_json = json.dumps(payload)
# print(type(payload_json))
# r = requests.post('http://httpbin.org/post', data=payload_json)
# print(r.text)

# 打印响应码
# r.status_code
# 增加请求头
# headers = {'Content-Type':'application/json'}
# r = requests.post('http://httpbin.org/post', data=payload_json , headers = headers)

# 三种方式发送post请求
# data=字典 自动添加默认请求头，请求数据用&连接
# json=字典 自动添加json格式请求头，请求数据json格式
# data=json.dumps(字典) 无默认请求头，请求数据字符串，类似json格式