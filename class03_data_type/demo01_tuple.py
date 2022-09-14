# 不可变数据 tuple
tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
tup2 = ([1, 2], 2)
tup2[0][1] = 3
print(tup2.__len__())
print(tup2)
# 支持切片
print(tup1[0:1:1])
# 翻转
print('翻转')
print(tup1[1:5:1])
print(tup1[1:5:-1])
print(tup1[5:1:-1])
print(tup1[-5:-1:-1])
print(tup1[-1:-5:-1])
# 拼接
print(tup1 + tup2)
# 删除
del tup2
# 长度
print(tup1.__len__())
print(len(tup1))
