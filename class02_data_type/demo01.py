# 可变数据类型：字典dict 列表list 集合set
# 不可变数据类型：数字number 字符串string 元组tuple
# 打印内存地址 id()

# 数字number 整数 int 小数 float 布尔：True 1 False 0
# 数字运算 + - * / %取余数 **乘方 //除（取整）

# 比较符 == != <= >= < > 结果只有True和False

# 赋值运算符 = += -= *= /=

# 数据类型转换

a = 1
int(a)
float(a)
abs(a)

# 向上取整 ceil
# 向下取整 floor
import math

math.ceil(a)
math.floor(a)

# 保留小数位数 round(数字，保留位数)
round(a, 2)

# 随机数 random() 0-1  randint(a,b) 区间,只能是整数
import random

random.random()
random.randint(1, 10)

# 字符串切片 大的字符串切成小的字符串
str1 = '1234567890'
print(str1[0:5])
# 最后一个字符
print(str1[-1])
# 最后三个字符
print(str1[-3:])
# 隔一个，取值
print(str1[::2])
# 字符串反转
print(str1[::-1])
# 字符串中的运算符 + 拼接 * 复制
print(str1 + '123')
print(str1 * 2)
# 字符串反斜杠 \\ r
# 字符串格式化 %s %d %f
print('%s%d%f' % ('123', 456, 7.89))
# format插入{}中，也可以指定顺序
print('{}'.format(123))
print('{}{}'.format(123, 456))
print('{0}{1}'.format(123, 456))
print('{1}{0}'.format(123, 456))
# f-string format格式的改良版
name = 1
age = 2
print(f'{name}{age}')
# 分隔符 split 连接符 join
# split() 默认根据\n \t 进行分割
print(str1.split())
# split('',1) 分割次数，这里是1次
print(str1.split('4', 1))

# replace 替换
print(str1.replace('123', '456'))

# 查找字符串 find(str,开始索引，结束索引) 找不到返回-1
print(str1.find('3', 0, 9))
# 判断是不是数字
print(str1.isnumeric())
# 判断是不是小写
print(str1.islower())
# 判断是不是大写
print(str1.isupper())

# 转换大写,小写
print(str1.upper(), str1.lower())
