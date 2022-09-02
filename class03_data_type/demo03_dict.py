# 字典
dict1 = {'name': 'abc', 'age': 15}
# 获取字典的值
print(dict1['name'])
# 增加字典数据
dict1['sex'] = 'nv'
print(dict1)
# 修改字典数据
dict1['name'] = 'bcd'
print(dict1)
# 删除字典数据 pop(指定键删除) popiten()删除最后一个 del[]指定删除
dict1.pop('age')
print(dict1)
dict1.popitem()
print(dict1)
del dict1['name']
print(dict1)
# 两个dict增加
dict2 = {'name2': 'abc', 'age2': 15}
dict3 = {'name3': 'abc', 'age2': 16}
dict2.update(dict3)
print(dict2)
# 字典转字符串
print(str(dict2), type(str(dict2)))
# 字符串转字典
dict4 = "{'name2': 'abc', 'age2': 16, 'name3': 'abc'}"
print(eval(dict4), type(eval(dict4)))
list1 = '[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]'
print(eval(list1), type(eval(list1)))
# 循环字典
for i, j in dict2.items():
    print(i, j)

# 创建新字典,fromkeys(键,值)
list2 = ['name', 'age']
dict5 = dict()
dict6 = dict5.fromkeys(list2, 1)
print(dict6)
