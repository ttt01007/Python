# 可变数据类型 数列 列表 list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# 支持切片
print(list1[1:5:1])
# 增 append() 末尾增加单个元素
list1.append(10)
print(list1)
# insert() 指定位置增加单个元素
list1.insert(5, 11)
print(list1)
# extend() 末尾增加可迭代对象
list1.extend(list1)
print(list1)
# 修改 索引进行修改
list1[11] = 12
print(list1)
# 删除 pop通过索引删除
list1.pop(5)
print(list1)
# 不填写默认删除最后一位
list1.pop()
print(list1)
# remove指定数据删除
list1.remove(2)
print(list1)
# del删除一个或者连续几个元素或者整个元素删除 支持切片删除
del list1[2]
print(list1)
del list1[1:3]
print(list1)
del list1

# 推导式
list1 = ['python', 'test1', 'test2']
list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
print(list2)
print('python'.title())
# 推导式,双循环
list_jianyu = ['jianyu1', 'jianyu2', 'jianyu3']
list_xiaojianjian = ['jianjian1', 'jianjian2', 'jianjian3']
# print(list_xiaojianjian.index('jianjian2',0,len(list_xiaojianjian)))
agrs_xiaojianjian = {key: value for key in list_jianyu if key.__contains__('jianyu') for value in list_xiaojianjian
                     if list_xiaojianjian.index(value,0,len(list_xiaojianjian))==list_jianyu.index(key,0,len(list_jianyu)) }
print(agrs_xiaojianjian)
print(dict(zip(list_jianyu,list_xiaojianjian)))
# 题目：删除重复数据
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 1]
# 统计重复的元素
print(list2.count(1))
# 找到1的下表进行删除，找1  可以用find和index(找的值,开始索引,结束索引)
# 区别: find没找到返回-1 index没找到会报错
print(list2.index(1, 0, len(list2)))
print(list2.pop(0))
print(list2)

# 简单方法 set去重
lists = [1, 1, 2, 3, 4, 6, 6, 2, 2, 9]
lists = list(set(lists))
print(lists)
# 比较然后删除,冒泡差不多
lists = [1, 1, 2, 3, 4, 6, 9, 6, 2, 2]
lists.sort()
t = lists[-1]
for i in range(len(lists) - 2, -1, -1):
    # print(i)
    if t == lists[i]:
        # del lists[i]
        lists.remove(lists[i])
    else:
        t = lists[i]
print(lists)
