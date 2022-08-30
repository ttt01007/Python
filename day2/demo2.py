numbers_strings = ("1", "2", "3", "4", "5")


def print_str(first, *second):
    print(first)
    print(second)


print_str(*numbers_strings)  # 注意这里的*numbers_strings

# second有无*有区别
numbers_strings = ("1", "2")


def print_str(first, second):
    print(first)
    print(second)


print_str(*numbers_strings)


def printStr(**anything):
    print(anything)


printStr(first=5, second=100)


def printStr(first, **dict):
    print(str(first) + "\n")
    print(dict)


printDic = {"name": "tyson", "age": "99"}

printStr(100, **printDic)
# 等同于
printStr(100, name="tyson", age="99")

printDic1 = {'key1': {'first': 'value2', 'key3': 'value3'}}
# print(**printDic1['key1'])
printStr(**printDic1['key1'])


# *和**放到参数里面就是解包
def locator(a, b):
    print(a, b)


# *和**放到参数里面就是解包
xxx = (1, 2)
locator(*xxx)

a = [1, 2, 3, 4, 5]


def mini(a, b, c, d, e):
    print(a, b, c, d, e)


mini(*a)
